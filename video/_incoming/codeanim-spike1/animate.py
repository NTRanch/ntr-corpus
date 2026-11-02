#!/usr/bin/env python3
"""Deterministic code animator — codeanim spike v1.

Renders one clip from one still + one job JSON. Every motion value is a
closed-form function of frame index or a fixed-timestep simulation;
nothing reads the wall clock, the environment, or an unseeded RNG.

Primitives (composed in a single sampling pass, then a camera crop):
  breath  - sinusoidal bob + scale about an anchor, integer cycles
  spring  - spring-damper point mass (semi-implicit Euler, fixed dt,
            warmed up to its periodic steady state) warping an
            elliptical region with smoothstep falloff
  camera  - Ken Burns crop: smoothstep ping-pong zoom + pan

Outputs: PNG frame sequence in <workdir>/frames (the mp4/gif encode is
done by the runner with ffmpeg -bitexact), plus <clip>.results.json
with per-clip measurements (spring seam residual, loop seam metric).
The job JSON is copied verbatim to <clip>.params.json by the runner:
params.json + animate.py == the clip, regenerable exactly.
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

SIM_DT_DENOM = 240  # spring sim rate Hz, fixed


def lcg_phases(seed):
    """Deterministic phases from the master seed (32-bit LCG, Numerical
    Recipes constants). Returns (phase_x, phase_y) in radians."""
    state = (int(seed) * 2654435761 + 1013904223) & 0xFFFFFFFF
    out = []
    for _ in range(2):
        state = (1664525 * state + 1013904223) & 0xFFFFFFFF
        out.append((state / 4294967296.0) * 2.0 * math.pi)
    return out[0], out[1]


def smoothstep(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3.0 - 2.0 * x)


def spring_track(job, n_frames, fps):
    """Simulate the spring; return (disp array [n_frames,2] float64,
    seam_residual float). Displacement in pixels at region center."""
    sp = job["spring"]
    period = float(sp["drive_period_s"])
    k = float(sp["stiffness"])
    c = float(sp["damping"])
    amp = sp["drive_amp_px"]
    phx, phy = lcg_phases(job["seed"])
    dt = 1.0 / SIM_DT_DENOM
    dur = n_frames / fps
    steps_per_frame = int(round(SIM_DT_DENOM / fps))
    total_steps = int(round(dur / dt))
    warm_steps = int(round(float(sp["warmup_periods"]) * period / dt))

    def target(t):
        w = 2.0 * math.pi / period
        return (amp[0] * math.sin(w * t + phx), amp[1] * math.sin(w * t + phy))

    x = np.zeros(2)
    v = np.zeros(2)
    t = 0.0
    for _ in range(warm_steps):
        a = -k * (x - target(t)) - c * v
        v = v + a * dt
        x = x + v * dt
        t += dt
    state0 = x.copy()
    disp = np.zeros((n_frames, 2))
    step = 0
    for f in range(n_frames):
        disp[f] = x
        for _ in range(steps_per_frame):
            a = -k * (x - target(t)) - c * v
            v = v + a * dt
            x = x + v * dt
            t += dt
            step += 1
    assert step == total_steps, (step, total_steps)
    seam = float(np.max(np.abs(x - state0)))
    return disp, seam


def render(job, out_frames_dir):
    src = Image.open(job["input"]).convert("RGB")
    W, H = src.size
    arr = np.asarray(src).astype(np.float32)
    pad = 24
    arrp = np.pad(arr, ((pad, pad), (pad, pad), (0, 0)), mode="reflect")
    n = int(job["frames"])
    fps = float(job["fps"])

    br = job.get("breath", {})
    br_on = br.get("enabled", False)
    br_period = float(br.get("period_s", 3.0))
    bob_px = float(br.get("bob_px", 0.0))
    scale_amp = float(br.get("scale_amp", 0.0))
    anchor = br.get("anchor", [0.5, 1.0])
    ax, ay = anchor[0] * (W - 1), anchor[1] * (H - 1)
    if br_on:
        cyc = (n / fps) / br_period
        assert abs(cyc - round(cyc)) < 1e-9, "breath must complete integer cycles"

    sp_on = job.get("spring", {}).get("enabled", False)
    disp = np.zeros((n, 2))
    seam = 0.0
    fall = None
    if sp_on:
        disp, seam = spring_track(job, n, fps)
        reg = job["spring"]["region"]
        cx, cy = reg["cx"] * (W - 1), reg["cy"] * (H - 1)
        rx, ry = reg["rx"] * (W - 1), reg["ry"] * (H - 1)
        gy, gx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((gx - cx) / rx) ** 2 + ((gy - cy) / ry) ** 2)
        fall = (1.0 - (r * r * (3.0 - 2.0 * r))).astype(np.float32)
        fall[r >= 1.0] = 0.0
        fall[r <= 0.0] = 1.0

    cam = job.get("camera", {})
    cam_on = cam.get("enabled", False)

    gy, gx = np.mgrid[0:H, 0:W].astype(np.float32)
    outdir = Path(out_frames_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    prev = None
    diffs = []
    first = None
    last = None
    t0 = time.perf_counter()
    for f in range(n):
        t = f / fps
        if br_on:
            w = 2.0 * math.pi / br_period
            bob = bob_px * math.sin(w * t)
            scale = 1.0 + scale_amp * math.sin(w * t + math.pi / 2.0)
        else:
            bob, scale = 0.0, 1.0
        # inverse breath transform: figure -> source coords
        sx = ax + (gx - ax) / scale
        sy = ay + (gy - ay - bob) / scale
        if sp_on:
            dx, dy = float(disp[f][0]), float(disp[f][1])
            sx = sx - dx * fall
            sy = sy - dy * fall
        sx = np.clip(sx + pad, 0, W + 2 * pad - 2)
        sy = np.clip(sy + pad, 0, H + 2 * pad - 2)
        x0 = np.floor(sx).astype(np.int32)
        y0 = np.floor(sy).astype(np.int32)
        fx = (sx - x0)[..., None]
        fy = (sy - y0)[..., None]
        Ia = arrp[y0, x0]
        Ib = arrp[y0, x0 + 1]
        Ic = arrp[y0 + 1, x0]
        Id = arrp[y0 + 1, x0 + 1]
        img = (Ia * (1 - fx) * (1 - fy) + Ib * fx * (1 - fy)
               + Ic * (1 - fx) * fy + Id * fx * fy)
        frame = Image.fromarray(np.rint(img).astype(np.uint8), "RGB")
        if cam_on:
            u = f / n
            e = smoothstep(2 * u) if u < 0.5 else smoothstep(2 - 2 * u)
            zoom = cam["zoom_from"] + (cam["zoom_to"] - cam["zoom_from"]) * e
            pan = cam.get("pan", [0.0, 0.0])
            cw, ch = W / zoom, H / zoom
            ccx = W / 2 + pan[0] * (W - cw) * e
            ccy = H / 2 + pan[1] * (H - ch) * e
            box = (int(round(ccx - cw / 2)), int(round(ccy - ch / 2)),
                   int(round(ccx + cw / 2)), int(round(ccy + ch / 2)))
            frame = frame.crop(box).resize((W, H), Image.LANCZOS)
        fa = np.asarray(frame).astype(np.float32)
        if prev is not None:
            diffs.append(float(np.mean(np.abs(fa - prev))))
        if first is None:
            first = fa
        last = fa
        prev = fa
        frame.save(outdir / f"f{f:03d}.png")
    wall = time.perf_counter() - t0
    seam_metric = float(np.mean(np.abs(last - first))) if n > 1 else 0.0
    return {
        "frames": n, "fps": fps, "size": [W, H],
        "render_wall_s": round(wall, 3),
        "spring_seam_residual_px": round(seam, 6) if sp_on else None,
        "loop_seam_meanabsdiff": round(seam_metric, 4),
        "median_interframe_meanabsdiff": round(float(np.median(diffs)), 4) if diffs else None,
    }


def main():
    job_path, frames_dir, results_path = sys.argv[1], sys.argv[2], sys.argv[3]
    job = json.loads(Path(job_path).read_text())
    res = render(job, frames_dir)
    res["job"] = str(job_path)
    Path(results_path).write_text(json.dumps(res, indent=1))
    print(json.dumps(res))


if __name__ == "__main__":
    main()
