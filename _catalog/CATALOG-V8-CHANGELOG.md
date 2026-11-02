# Catalog v8 — A3 category fields populated via catq

Built 2026-10-25. Base: `catalog-v7.jsonl` (md5 `a57d48567d04a95683307b262313bc01`, unchanged).
Output: `catalog-v8.jsonl` (md5 `31b4204017acaa0a336acad6fc0509af`). Tool: catq
(`~/workspace/catalog-tool-20261025/target/release/catq`) — every write went through
catq script mode against a working copy; v7 was never written.

v8 adds exactly four fields — `heroine`, `family`, `rating`, `pool` (the A3 fields
from the Danbooru adaptation study) — and changes nothing else. All values are
**derived from recorded evidence** (the row itself, its generation record, its
spec/batch/decision records); where no recorded evidence exists the field stays
absent. Unknown is a value; nothing was guessed.

Per-row derivation evidence for every populated value is in
`v8-scripts/derivation-table.json` (stem, value, evidence tier, evidence pointer),
produced by `v8-scripts/derive_v8.py`.

## Derivation rules (written before application, applied as written)

### family — from the row's id family / lane as recorded (601/601 populated)

- lane `portraits` → `portraits`
- `img-cov-*` → `cov`; `img-hx-*` → `hx`; `img-hyp-*` → `hyp`; `img-exh-*` → `exh`;
  `img-ntr-*` → `ntr`; `img-sol-*` → `sol`
- `img-h-e*` → `e-series`; `img-h-s*` → `s-series`; `img-h-x*` → `x-series`
  (the Specs-H batch families; "e-series" is the brief's own term, extended
  symmetrically to the scene and x batches)

Counts: cov 85, hx 46, hyp 24, exh 8, ntr 8, sol 8, e-series 101, s-series 133,
x-series 74, portraits 114. Unset: 0 — every row's id family is recorded.

### heroine — only where a record names one of the ten heroines (112/601 populated)

- Portraits lane only: the heroine whose name token appears in the asset
  filename (`<name>_begin/_end…`, `nsfw-end-<name>`, `nsfw2/3-end-<name>`,
  `img-maren-*` → maren, `test-viv-*` → vivienne — see judgment call 3).
- Corpus lane: absent for all rows. CORPUS-SPECS-H's cast rule records the
  corpus figures as original unnamed women (the named cast belongs to the
  portrait lane). Verified mechanically: zero heroine-name hits across all
  corpus recipe positives and lifecycle_basis strings.

Counts: cordelia 6, kaisa 7, katya 7, manon 40, maren 13, sadie 7, valentina 7,
vivienne 10, yuna 6, zuzana 9.
Unset: 489 — reason classes: corpus-lane cast rule (487), full-cast contact
sheet naming no single heroine (2: contact-BEGIN.png, contact-END.png).

### rating — g/s/q/e per the Danbooru scale (601/601 populated, 0 unset)

Word map: the estate's generation records carry a declared rating word —
`explicit`→e, `questionable`→q, `sensitive`→s, `safe`→g. Precedence (first hit wins):

1. **job-record** (35 rows): the exact generation job in `jobs-*.jsonl` for the item.
2. **batch-record** (219 rows): the rating word in the item's batch tuple
   (seed_batch1/2, hypno_batches, specs_h_v*, maren_expr*, nsfw_end_tests, …).
3. **batch-record-seedjoin** (10 rows): batch tuple joined on the row's own
   recipe (seed, width, height).
4. **keepers-seed-join** (1 row): seed recorded for the file in
   keepers.json/KEEPERS.md, joined to that seed's batch record.
5. **retry-base-record** (20 rows): a plain `-rN` retry inherits its base
   item's recorded word (same scene re-rendered; directed later rounds carry
   their own job records and are caught at tier 1).
6. **markers** (114 rows): marker analysis over recorded prompt text
   (catalog recipe, batch tags, keeper_harvest batch.json, keepers card
   recipe, or v7-recipes-full, in that order) using the published marker
   lists in `derive_v8.py` — explicit-act markers → e; nudity/exposure
   markers → q; sexualized-clothing / trance-arousal markers on a clothed
   figure → s; none → g. Sub-rules: an orgasmic-expression marker
   (orgasm/ahegao) with exposure markers → e, alone → q; the lactation act
   (milking / milk spray / milk stream) → e; visible leaking milk counts as
   exposure evidence (q tier); lactation tag alone, clothed → s.
7. **portrait-set** (105 rows): recorded set membership for portrait rows
   with no generation record in the skeleton — BEGIN set (incl. contact-BEGIN)
   → g; NSFW END sets (`*_end*`, `nsfw-end/nsfw2-end/nsfw3-end`, contact-END) → e.
8. **edit-inheritance** (97 rows): a pixel-edit derivative (inpaint / cleanup /
   colorize / lettering / fix lineage, per cleanup_s8*.py, inpaint_*.py,
   colorize_s12b_*.py, the v44–v48 edit batches) inherits its base render's
   rating; longest rated prefix stem wins; the s12b colorize rows are tied by
   the recorded `SRC` line in colorize_s12b_v36.py to img-h-s12-b.

Counts: e 463, q 53, s 41, g 44. Unset: 0.
Recorded words (tiers 1–5: 285 rows) always govern over marker inference
(tier 6); marker inference was never used to override a declared rating.

### pool — recorded presentation rows/sets only (194/601 populated)

- `eye-pass-sheet-{1..5}-row-{1..4}` (117 rows): the 117 corpus originals,
  positionally over the sorted `corpus117/` filename list (24 per sheet,
  rows of 6) — the mapping the owner's positional verdicts were recorded
  against (CATALOG-V4 amendment), cross-validated at hx-003/004/005
  (positions 57–59), hx-009 (63), ntr-008 (109), sol-003 (112).
- `retry-row-a1/a2/a2b/a2c/a2d/a2e/a2f/a2g/a3/a3b/a3c/a3d/b1/b1b/b2/b2b/b2c`
  (54 rows): the decision strips in decisions-20261024/, compositions as
  recorded in the 2026-10-24/25 daily logs.
- `decision-1` (6 rows): the six decision1-*.jpg cells in decisions-20261023/.
- `gate-pail-s12b` (7 rows): gate-pail-s12b-20261024.jpg — pail a–d
  (img-h-s8-pail-v48-a…d) + s12b variations a–c (img-h-s12b-e2r-a/b/c, per the
  v6 changelog's derivation record).
- `v37-s11-picks` (10 rows): the ten s11 items of specs_h_v37_batch.py
  (daily log: "v37 S11 ×10" sheet pass).

Unset: 407 — reason class: no recorded presentation row/set for the row.

## Execution (catq script mode, dogfooded)

Scripts (generated from the derivation table by `v8-scripts/gen_scripts.py`):
`v8-scripts/family.sh` (10 commands, id-glob/lane selections),
`v8-scripts/heroine.sh` (10 commands, id-glob selections),
`v8-scripts/rating.sh` (14 commands, sha256-list `--where` selections in
chunks of 50 — row-exact because 15 stems cover 50 rows),
`v8-scripts/pool.sh` (40 commands, `--ids` selections).
74 commands total. Each was run dry-run FIRST against the working copy
(logs in `v8-scripts/dry-runs/`), and every command's `rows changed` matched
its expected count exactly before any apply ran. Sample dry-run diff:

```
DRY RUN (no changes written; pass --apply to write)
rows selected: 85
rows changed: 85
field changes:
  family: (absent) → cov ×85
```

Apply pass (same scripts with `--apply`): family 601, heroine 112,
rating 601, pool 194 — 1,508 field assignments; applied totals identical to
dry-run totals per field. catq's own audit trail (timestamp, script,
rows changed, md5 before/after per command, chaining from v7's md5 to
31b42040…) is preserved in `v8-scripts/apply-changelog.txt` (74 lines).

## Validation (v8-scripts/validate_v8.py — independent file-side ground truth)

- Row count: v7 = v8 = **601**. Id (asset_file) multiset identical:
  **566 unique stems** both sides (the 35 extra rows are the 15 known
  duplicate stems' batch-version variants).
- Field-level diff over all 601 rows (matched by asset_file+path):
  **every v7 field value unchanged**; added keys are only the four new
  fields (family 601 rows, rating 601, pool 194, heroine 112).
- State tallies from the v8 file: keeper **74**, accepted **82**,
  candidate **350**, rejected **86**, superseded **9** — unchanged.
- catq vs ground truth: **69 value-count queries** (5 states, 10 heroines,
  10 families, 4 ratings, 40 pools) — all equal.
- parent/child chain: `parent:img-cov-037-r1` = 2 (fix1, fix2);
  `parent:img-h-s12b-e2` = 3 (e2r-a/b/c); `child:img-h-s12b-e2r-a` = 1;
  `child:img-cov-037-r1-fix1` = 1 — all match file ground truth.
- Combined query `state:keeper rating:e family:*` summed over all ten
  families: catq **59** = ground truth **59**.
- Untouched: `catalog-v7.jsonl` md5 `a57d48567d04a95683307b262313bc01`;
  `keepers.json` md5 `f87c59527414c0c9592fd43afb41efd6`.

Note: rows keep their `catalog_version: "v7"` field value — the validation
contract (only the four fields added) and catq's settable-field list both
require it; the v8 identity lives at the file level.

## Judgment calls (each with its evidence)

1. **Family names for the Specs-H batches** are `e-series` / `s-series` /
   `x-series`: the task brief's own example term for the first, extended
   symmetrically; Specs-H groups its types as H-E/H-S/H-X and the batches
   share one pipeline.
2. **Portrait-lane family is `portraits`** (the recorded lane); the
   individual subject is carried by `heroine`, so family is not redundant.
3. **test-viv-* → heroine vivienne**: nsfw_end_tests.py records the subject
   as 28 years old with black-cherry hair and violet eyes — Vivienne's
   recorded portrait description — under the `viv` prefix; all three test
   rows also take their recorded word `explicit` → e.
4. **Contact sheets carry no heroine**: contact-BEGIN/END.png are full-cast
   sheets; no single heroine is named. Their ratings follow their sets (g/e).
5. **Recorded rating words govern over marker inference** wherever both
   exist (285 rows). The declared word is the estate's own record of the
   item's content class; markers only fill gaps. Example consequence:
   hx-005's clothed trance frames rate e because hypno_batches records the
   item as `explicit`; its retries inherit that word (tier 5).
6. **`nipple play` is an e-marker**: seed_batch2 records the identical
   scene (img-cov-030, same tags) as `explicit`.
7. **Trance markers on clothed figures → s** (hypnosis, empty eyes, spiral
   eyes, @_@, entranced): matches the recorded `sensitive` words for
   identical clothed trance items (seed_batch1 hyp-001/hyp-002).
8. **Lactation split**: milking act → e (the batch records' own practice,
   e.g. gen_s8_fresh rates its milking items `explicit`); visible leaking
   milk = exposure evidence → q (img-h-s12-c), and e when paired with an
   orgasmic marker (img-h-s12-b: ahegao + leaking milk). The rule also
   carries a bare-`lactation`-mention → s branch for clothed figures, but
   no row landed on it — every lactation-mentioning row resolved at q or e
   or carried a recorded word.
9. **img-h-s8t-final rates e** via keepers-seed-join: KEEPERS.md records it
   as the tankard-retry final at seed 21424, which is the v35 batch's
   img-h-s8t-r4 seed; that tuple's recorded word is `explicit`.
10. **Decision-1's tankard cell is img-h-s8t-final**: strip filename
    `decision1-s8-tankard-final.jpg` ↔ the s8t (S8 tankard) family's
    `-final` row; KEEPERS.md calls that file "S8 TANKARD RETRY FINAL".
11. **cov-037-r1-fix1/fix2 are NOT in retry-row-a2**: the strip presented
    r1 itself; fix1/fix2 are post-verdict edits of r1 (fix2 was later
    presented singly — a single image is not a row/set).
12. **hx-009-x1/x2 carry no pool**: x1 was never presented; x2 was
    presented as a single image (2026-10-25 log), not as a row/set.
13. **Pools NOT assigned despite presentation artifacts existing**:
    the v39 sheet and the BDSM v40–v42 panels — their batch item ids
    (img-h-e1-a, img-b01-a, …) match zero catalog stems; those renders were
    never admitted to the catalog, so there are no rows to pool. The E12
    v43 panel has no composition record in the skeleton. Retry rows B2d
    (hx-009-z1/z2) and B3 (ntr-008/sol-003 retries) contain no catalog rows.
14. **Rating applied by sha256-list selection, not by id**: 15 stems cover
    50 rows (batch-version variants of e1/e2/e3/e6/s2/s4/e10/e11/…) whose
    ratings can differ per version; selections had to be row-exact.
    Family/heroine selections are stem-safe (batch-version variants share
    a family; portrait duplicate stems are the same filename for the same
    heroine, e.g. kaisa_begin.png in two directories) and were verified
    per-command by dry-run counts.
