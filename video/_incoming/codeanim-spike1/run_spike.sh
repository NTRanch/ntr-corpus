#!/bin/bash
# codeanim spike runner — runs the full pipeline TWICE with identical
# inputs and diffs SHA-256 of every media/params output.
# Determinism hygiene: fixed env, ffmpeg -bitexact, x264 -threads 1.
set -u
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
BASE=~/ntr-corpus/video/_incoming/codeanim-spike1
SRC=~/codeanim-src
cd "$SRC" || exit 1

run_pipeline () {
  local OUT="$1"
  mkdir -p "$OUT"
  : > "$OUT/timings.txt"
  for job in "$SRC"/jobs/*.json; do
    local name; name=$(basename "$job" .json)
    local t0=$SECONDS
    python3 "$SRC/animate.py" "$job" "$OUT/frames-$name" "$OUT/$name.results.json" > "$OUT/$name.render.log" 2>&1 || { echo "RENDER FAIL $name"; return 1; }
    local t1=$SECONDS
    ffmpeg -y -bitexact -framerate 16 -i "$OUT/frames-$name/f%03d.png" \
      -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium -threads 1 \
      -movflags +faststart "$OUT/$name.mp4" > "$OUT/$name.encode.log" 2>&1 || { echo "ENCODE FAIL $name"; return 1; }
    local t2=$SECONDS
    echo "$name render_s=$((t1-t0)) encode_s=$((t2-t1))" >> "$OUT/timings.txt"
    cp "$job" "$OUT/$name.params.json"
    rm -rf "$OUT/frames-$name"
  done
  # gif for the headline composite only — palette built from THIS run's
  # own frames so run 2 never reads run 1's artifacts
  python3 "$SRC/animate.py" "$SRC/jobs/cov029_attract.json" "$OUT/frames-gif" "$OUT/gif.results.json" >/dev/null 2>&1
  ffmpeg -y -bitexact -framerate 16 -i "$OUT/frames-gif/f%03d.png" \
    -vf "fps=12,scale=416:-1:flags=lanczos,palettegen" "$OUT/pal.png" >/dev/null 2>&1
  ffmpeg -y -bitexact -framerate 16 -i "$OUT/frames-gif/f%03d.png" -i "$OUT/pal.png" \
    -lavfi "fps=12,scale=416:-1:flags=lanczos [x]; [x][1:v] paletteuse" \
    "$OUT/cov029_attract.gif" >/dev/null 2>&1
  rm -rf "$OUT/frames-gif" "$OUT/pal.png" "$OUT/gif.results.json"
}

echo "=== RUN 1 ==="
run_pipeline "$BASE/clips-run1" || exit 1
echo "=== RUN 2 ==="
run_pipeline "$BASE/clips-run2" || exit 1

( cd "$BASE/clips-run1" && sha256sum *.mp4 *.gif *.params.json | sort -k2 ) > "$BASE/hashes_run1.txt"
( cd "$BASE/clips-run2" && sha256sum *.mp4 *.gif *.params.json | sort -k2 ) > "$BASE/hashes_run2.txt"
if diff -u "$BASE/hashes_run1.txt" "$BASE/hashes_run2.txt" > "$BASE/hashdiff.txt"; then
  echo "DETERMINISM: PASS — all outputs byte-identical across runs" | tee "$BASE/determinism.txt"
else
  echo "DETERMINISM: FAIL — see hashdiff.txt" | tee "$BASE/determinism.txt"
fi

mkdir -p "$BASE/clips" "$BASE/strips"
cp "$BASE/clips-run1"/*.mp4 "$BASE/clips-run1"/*.gif "$BASE/clips-run1"/*.params.json "$BASE/clips-run1"/*.results.json "$BASE/clips/"
for c in cov029_attract cov014_attract hyp004_attract cov029_spring; do
  ffmpeg -y -bitexact -i "$BASE/clips/$c.mp4" \
    -vf "select='not(mod(n\,16))',scale=277:-1,tile=6x1" -frames:v 1 "$BASE/strips/$c-strip.png" >/dev/null 2>&1
done
cp "$SRC/animate.py" "$BASE/animate.py"
sha256sum "$BASE/animate.py"
echo "=== DONE ==="
ls -la "$BASE/clips"
