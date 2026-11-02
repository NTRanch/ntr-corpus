#!/bin/bash
# NSFW END v3 codeanim double-run — mirrors the specs-H production run exactly:
# animate.py (SHA 6093ed87...), 96 frames @16fps, ffmpeg -bitexact libx264
# -threads 1, fixed thread env. Outputs staged ONLY; nothing admitted.
set -u
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
BASE=~/ntr-corpus/video/_incoming/nsfw-end-v3-codeanim
SRC=~/codeanim-src
LOG="$BASE/run.log"
: > "$LOG"

run_pipeline () {
  local OUT="$1"
  mkdir -p "$OUT"
  : > "$OUT/timings.txt"
  for job in "$BASE"/jobs/*.json; do
    local name; name=$(basename "$job" .json)
    local t0=$SECONDS
    python3 "$SRC/animate.py" "$job" "$OUT/frames-$name" "$OUT/$name.results.json" > "$OUT/$name.render.log" 2>&1 || { echo "RENDER FAIL $name" | tee -a "$LOG"; return 1; }
    local t1=$SECONDS
    ffmpeg -y -bitexact -framerate 16 -i "$OUT/frames-$name/f%03d.png" \
      -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium -threads 1 \
      -movflags +faststart "$OUT/$name.mp4" > "$OUT/$name.encode.log" 2>&1 || { echo "ENCODE FAIL $name" | tee -a "$LOG"; return 1; }
    local t2=$SECONDS
    echo "$name render_s=$((t1-t0)) encode_s=$((t2-t1))" >> "$OUT/timings.txt"
    cp "$job" "$OUT/$name.params.json"
    rm -rf "$OUT/frames-$name"
    local sha; sha=$(sha256sum "$OUT/$name.mp4" | cut -c1-12)
    echo "$2 $name OK sha=$sha" | tee -a "$LOG"
  done
}

T_START=$SECONDS
echo "=== RUN 1 ===" | tee -a "$LOG"
run_pipeline "$BASE/clips-run1" "run1" || exit 1
T_MID=$SECONDS
echo "=== RUN 2 ===" | tee -a "$LOG"
run_pipeline "$BASE/clips-run2" "run2" || exit 1
T_END=$SECONDS

( cd "$BASE/clips-run1" && sha256sum *.mp4 *.params.json | sort -k2 ) > "$BASE/hashes_run1.txt"
( cd "$BASE/clips-run2" && sha256sum *.mp4 *.params.json | sort -k2 ) > "$BASE/hashes_run2.txt"
if diff -u "$BASE/hashes_run1.txt" "$BASE/hashes_run2.txt" > "$BASE/hashdiff.txt"; then
  echo "DETERMINISM: PASS" | tee -a "$LOG"
else
  echo "DETERMINISM: FAIL — see hashdiff.txt" | tee -a "$LOG"
fi
echo "WALL run1_s=$((T_MID-T_START)) run2_s=$((T_END-T_MID)) total_s=$((T_END-T_START))" | tee -a "$LOG"
echo "DONE" > "$BASE/DONE"
echo "=== DONE ===" | tee -a "$LOG"
