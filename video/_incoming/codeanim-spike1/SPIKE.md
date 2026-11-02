# SPIKE — Deterministic code animation for NTR corpus media

Date: 2026-10-22 (America/Los_Angeles). Internal evidence only. Nothing was uploaded anywhere.
Spike dir: `~/ntr-corpus/video/_incoming/codeanim-spike1/`
Counterpart: the Wan 2.2 I2V spike (`~/ntr-corpus/video/_incoming/spike1/SPIKE.md`) — same
headline still (img-cov-029), generative baseline 771 s/clip on the A6000, publish tier
license-blocked by its LoRA.

**Question:** can animation produced entirely by deterministic code — fixed timestep,
fixed seeds, parameterized motion, no generative model in the loop — serve our NSFW
media, and where?

**Short answer:** yes for loops, no for action. Code animation is byte-identical
reproducible (proven below), ~30× cheaper than the Wan render, carries zero license
surface, and is good enough — today, with three primitives — for idle/ambient/attract
material. It cannot create contact action, and nothing in this report pretends
otherwise.

## 1. Method

Animator: `animate.py` (SHA-256
`6093ed87d523c6058eaeeb801fab6a1251de07ddf67c81310190c9b06b756e99`, copied into the
spike dir). Python 3.14.8 + PIL 13.0.0 + numpy 2.5.4, system install on primo; encode
via ffmpeg n9.0.2 / libx264. CPU-only, single-threaded by env pin
(`PYTHONHASHSEED=0`, BLAS threads 1). No GPU, no service touched (rose untouched).

Primitives, composed in one bilinear sampling pass per frame, then a camera crop:

1. **Breath/sway** — whole-figure sinusoidal bob (3 px) + scale breathing (0.8%)
   about a bottom-center anchor, 3 s period, integer cycles per clip by assertion.
2. **Camera** — Ken Burns crop: zoom 1.00→1.07…1.09 with pan, smoothstep ping-pong
   (out and back inside one clip, so the loop point is the start framing).
3. **Spring layer** — a 2D spring-damper point mass (semi-implicit Euler, fixed
   dt = 1/240 s, stiffness 25, damping 3.5, ζ ≈ 0.35), target driven on a 3 s
   sinusoid whose phases derive from the clip seed via a recorded LCG. Warps an
   elliptical region (smoothstep falloff) — chest region on all three stills. The
   sim is warmed up 12 drive periods before frame 0 so it starts in its periodic
   steady state.

Every constant lives in a per-clip job JSON, copied verbatim to
`<clip>.params.json`: **params.json + animate.py regenerate the clip exactly**
(proven in §2). Region ellipses were authored by eye per still and are data, not
code — that fact matters in §6.

Clips: 96 frames @ 16 fps = 6.0 s, native aspect. img-cov-029 (832×1216; the Wan
still) got each primitive alone plus the composite; img-cov-014 (1216×832,
tentacle restraint scene) and img-hyp-004 (832×1216, hypnosis scene) got the
composite, to prove the pipeline is not tuned to one image.

## 2. Determinism proof — PASS

The full pipeline (7 renders incl. the GIF pass, all encodes) ran **twice** from
identical inputs into `clips-run1/` and `clips-run2/`. SHA-256 of every media and
params output compared — **13/13 byte-identical**, `diff` empty
(`hashes_run1.txt` == `hashes_run2.txt`; verdict in `determinism.txt`).

| SHA-256 (run1 == run2) | File |
|---|---|
| `5ae119c40756aaaae600…` | cov029_attract.mp4 |
| `bd88b0dfc0d1b726c461…` | cov029_attract.gif |
| `bbe886c2a14c09d4df6f…` | cov029_breath.mp4 |
| `73f978babd0ef6555b7b…` | cov029_camera.mp4 |
| `365429f1490e2383d505…` | cov029_spring.mp4 |
| `170a727d8c143570e2e9…` | cov014_attract.mp4 |
| `0bb2f3604070bd7e527a…` | hyp004_attract.mp4 |
| (6 × params.json, all identical) | `*.params.json` |

Scope of the claim, stated plainly: byte-identity holds for **this toolchain**
(PIL 13.0.0 / numpy 2.5.4 / ffmpeg n9.0.2, `-bitexact`, x264 `-threads 1`) on this
host class. A different x264 build may encode the same frames to different bytes —
the toolchain versions are part of the recipe and belong in the manifest.
`*.results.json` files contain wall-clock measurements and are excluded from the
claim; they are logs, not artifacts.

Loop-seam measurements (mean abs pixel diff, last frame vs first frame, against
the median ordinary inter-frame diff — seam should be ≤ typical step):

| Clip | Seam | Median step | Spring state residual |
|---|---|---|---|
| cov029_attract | 1.00 | 3.42 | 0.0 px |
| cov014_attract | 1.70 | 5.24 | 0.0 px |
| hyp004_attract | 1.75 | 4.90 | 0.0 px |
| cov029_breath | 1.04 | 1.75 | — |
| cov029_camera | 0.00 | 3.48 | — |
| cov029_spring | 0.17 | 0.13 | 0.0 px |

Composites and breath close their loops *below* ordinary frame-to-frame change —
no visible seam. The spring's simulated state returns to its start value exactly
(0.0 px residual at recorded precision) after warmup; the spring-only clip's seam
(0.17 vs median step 0.13) is a single frame-step at the cycle's steepest phase on
a clip whose total motion is a few pixels — a metric artifact, at worst a
sub-perceptual pulse.

## 3. Cost

| | Code animation (this spike) | Wan 2.2 I2V (prior spike) |
|---|---|---|
| Wall time per clip | **22–29 s** (render 19–24 s + encode 2–5 s) | **771 s** (LoRA) / 760 s (base) |
| Frames | 96 (6.0 s @ 16 fps) | 81 (5.06 s @ 16 fps) |
| Hardware | CPU only, 1 pinned thread of a 16-thread host | RTX A6000 (~28 GB incl. another tenant) |
| Marginal cost of clip #100 | identical ~25 s, parallelizable across cores | identical ~13 min of the only big GPU |

≈ **30× faster**, on hardware that is otherwise idle, with 15 more cores free for
batch parallelism. The whole spike — 6 clips × 2 proof runs + GIF + strips — took
about 12 minutes of wall time end to end.

## 4. Honest quality read

Frame strips in `strips/` (frames 0/16/32/48/64/80 of each composite + spring).

- **Breath/sway** — reads as alive. A 3 px bob + 0.8% scale is below conscious
  notice and exactly at the level where a still stops looking dead. Cheapest
  primitive, highest value per line of code.
- **Camera** — reads as production value. The ping-pong push-in is the most
  visible motion in the composites and carries them; framing drift toward the
  face (hyp004) feels intentional. Flat, though: one plane, no parallax — the
  background moves exactly with the figure, which a real camera would not do.
- **Spring layer** — the weakest at spike constants. Median inter-frame diff
  0.13 vs breath's 1.75: at ±8 px drive on a smooth skin region it reads in
  motion as a gentle swell synchronized a beat behind the breath — correct
  secondary-motion *behavior* — but it is subtle to the edge of invisible in
  stills, and its one clear win is structural: on img-cov-029 her hands lie
  inside the warp region, so they move *with* the chest instead of sliding
  against it the way a rigid bob alone would make them. Where the region
  crosses hard linework (tentacles over the chest in img-cov-014) the warp
  bends the lines smoothly — no tearing or smearing at these amplitudes, but
  the bend is content-blind: it cannot know a tentacle should be rigid.
- **Composite (attract)** — the three together clear the "alive still" bar for
  menu/ambient use. Identity is perfect by construction (same pixels, remapped);
  nothing melts, nothing drifts off-register — the two failure classes that cap
  the Wan clips (finger melding, register drift) do not exist here. What it
  cannot do is *act*: the pose, expression, and hands are frozen in everything
  except position. It is a photograph breathing, not a performance.
- **Artifacts** — bilinear remapping softens linework slightly at warp peaks;
  no edge halos (reflect padding + full-frame regions); no loop seams (§2).

## 5. Viability verdicts

**(a) Game idle/ambient loops — VIABLE; make it the default.** This is the
estate's companion-idle use case (Séraphine standard: visible posture/expression
change is the bar for *character* idles; ambient character presence needs the
breath/sway/camera subset, which is proven here). Seamless by construction,
regenerable from data, runs anywhere.

**(b) Attract/menu loops — VIABLE; make it the default.** The composite is
purpose-built for this and clears it. The GIF (416 px wide, 8.8 MB — would want
tuning for web) works for store/HF pages where autoplay video is awkward.

**(c) Corpus video-lane items as a class — VIABLE for a typed subclass.**
The lane should distinguish `ambient-loop` (code) from `action` (I2V). Code
items are ~30× cheaper, deterministic (a property no other lane item has),
and — decisive for publish tier — carry **no model-license surface at all**:
our stills, our parameters, open toolchain. The lopi999 problem does not
exist for this class.

**(d) Live2D-style parameter animation — VIABLE as a format, with authoring.**
These primitives *are* Live2D's model (parameter-driven deformation) minus the
rig. What is missing is mesh/mask authoring per character. That fits the
estate's code-first direction: author region/parameter sets as data in the
lumen character record (the job JSONs here are a working schema sketch), and
the runtime evaluates the same math this spike validated. Do not build a
general rigging tool; per-character authored parameter data + this evaluator
is the proportionate version.

**(e) Explicit contact scenes — NOT VIABLE.** A warp remaps pixels that exist;
it cannot create the pixels a contact scene needs between poses — no new
occlusion, no hand repositioning, no partner geometry, no expression change.
Even the 14B generative model only amplified a pose the still already
contained (Wan spike §4); code animation cannot do even that for contact — it
moves what is drawn, whole or smoothly bent, nothing more. Contact stays with
trained I2V (the from-scratch own-LoRA route) or hand-authored sprite work.

## 6. Where each approach owns the territory

- **Code animation is the default** for: idle/ambient loops, attract/menu
  loops, corpus `ambient-loop` items, Live2D-style record playback, and any
  "make this still feel alive" request currently burning a 13-minute GPU
  render.
- **Trained I2V remains necessary** for: any clip where the action is the
  content — contact, gesture sequences, expression/register changes,
  narrative beats. That shrinks the own-LoRA reproduction program (Wan spike
  §5.3) to action clips only; the loop class never needed it.

## 7. What a production version needs

1. **Params in the corpus manifest.** Promote the job JSON into the item
   manifest as an `animation` block (primitives + constants + seed +
   toolchain versions). No block → still; block → regenerable loop. This is
   the single highest-leverage step: it makes the video lane's loop class a
   *view* of the image lane, not a separate asset pile.
2. **Region authoring.** Hand ellipses worked for 3 stills; production needs
   per-character region sets (chest, hair, hips, hem) as authored data, with
   coarse segmentation/matting assist — and **layer splits** (figure cutout
   over background) where camera parallax is wanted, since a single plane
   cannot parallax.
3. **Amplitude pass.** The spring wants ~2–3× spike amplitude with
   per-region gain, and **coupled springs** (breath → chest → hair) so
   secondary motion cascades instead of moving in lockstep.
4. **Expression/blink overlays are scheduling, not warps.** Drawn variants
   (the estate's face-set work) cross-faded on the same deterministic clock;
   code anim can time them, it cannot synthesize them.
5. **Toolchain pinning.** ffmpeg/x264/PIL/numpy versions recorded per item
   (byte-identity is per-toolchain, §2).
6. **Not needed:** a rigging GUI, a physics engine, any GPU. The evaluator is
   ~200 lines and should stay that way (Tiger Style: the difficulty belongs
   in the authored data, not the code).

## 8. Files

Primo `~/ntr-corpus/video/_incoming/codeanim-spike1/`: `SPIKE.md` (this file),
`animate.py`, `run_spike.sh`, `jobs/` (the 6 job JSONs), `clips/` (6 mp4 +
GIF + params + results), `clips-run1/`, `clips-run2/` (proof runs),
`hashes_run1.txt`, `hashes_run2.txt`, `hashdiff.txt` (empty),
`determinism.txt`, `strips/` (4 frame strips), `run.log`.
Sandbox copies: `~/workspace/ntr-corpus-skeleton/codeanim-SPIKE.md`,
`codeanim/` (animate.py, jobs, strips, headline mp4 + gif).
