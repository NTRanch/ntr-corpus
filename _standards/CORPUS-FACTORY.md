# Corpus Factory v1 — contract for deterministic, scalable asset production

Owner-approved 2026-10-23 22:53 PDT. Purpose: replace one-off batch scripts
with a single deterministic pipeline that produces, catalogs, quality-gates,
and derives game-ready assets for Strobe and the planned NTRanch titles.

## 1. Asset contract (manifest schema v1)

Every asset carries a sidecar manifest record (JSONL catalog is the index of
record; per-file sidecars are generated FROM the catalog, never edited by hand).

Required fields:
- `asset_id` — stable slug, unique forever (never reused).
- `sha256` — of the original PNG. Originals are immutable; any change is a
  new asset with `derived_from` pointing back.
- `path` — current location on primo.
- `recipe` — object: `template_version`, `checkpoint` (name + sha256),
  `loras` (name, sha256, weight), `seed`, `sampler`, `scheduler`, `steps`,
  `cfg`, `width`, `height`, `positive` (full string), `negative` (full string).
- `content` — object: `type_code` (Specs-H/C), `cluster`, `character_id`
  (or `archetype`), `state`, `expression`, `framing`, `costume`, `setting`,
  `canon_invariants` checked (hair/eye colors where applicable).
- `provenance` — `source_type` (original-generation | abstracted-type |
  study-derived), `adult_basis` (how adulthood is established for the item),
  `license_status` (production-cleared | internal-only | quarantined),
  `license_alert` (bool).
- `lifecycle` — `state`: candidate | accepted | keeper | golden |
  superseded | rejected; `owner_verdict` + `owner_verdict_at` when ruled;
  `pax_gate` notes.
- `derivatives` — map of derivative kind -> {path, sha256, tool_version}.

## 2. Queue runner

- Jobs are data (JSONL), never code edits. One job = one asset_id + recipe.
- Runner groups jobs by (checkpoint, width, height, steps) to avoid model
  churn; executes in order; writes output + manifest atomically.
- Idempotent: a job whose asset_id already has a catalog record with a
  matching recipe hash is skipped. Resumable after interruption.
- Determinism proof: a fixed pilot set is run twice; SHA-256 of outputs
  must match 100% before the runner is trusted for volume.
- ComfyUI lifecycle rule stands: start only if down; stop only if the
  runner started it.

## 3. QC first gate (automated, before owner eye)

Flags, never silent drops: tagger vocabulary check; text/watermark present;
grey or drifted skin cast; canon color mismatch (portrait lane); face
cropped or missing; cause/state/face-body legibility legs (Specs-H rule);
obvious limb/hand defect heuristics where detectable. Every flag is a
taxonomy code in the catalog (`qc_flags: []`). Owner eye promotes;
automation only sorts the queue.

## 4. Derivative pack (at admission)

Generated once, deterministically, versioned tools:
- `thumb` (contact-sheet JPEG), `webp` (game-ready), `palette` (JSON),
  `mask` (subject segmentation PNG), `cutout` (transparent PNG),
  `landmarks` (face/pose keypoints JSON) when tooling is present.
Each derivative is recorded with its tool version; re-derivation on tool
upgrade creates a new version, never overwrites silently.

## 5. Demand matrix

Production is planned as matrix rows: title x character/archetype x
expression x state x pose x framing x costume x setting x asset type.
Batches fill matrix gaps by quota; near-duplicate cells need explicit
justification. Canon packs (turnarounds, expression grids, part
inventories for Live2D, neutral poses for 3D) are matrix rows like any
other, scheduled deliberately.

## 6. License and provenance gate

No asset is `production-cleared` while any input (checkpoint, LoRA, voice,
reference) has unresolved commercial status. Unclear inputs stay
`internal-only` or `quarantined` in the manifest. This gate precedes
scale, not follows it.

## 7. LoRA policy (standing)

House style LoRA: pilot at 20 diverse keepers, production candidate at 40;
diversity rules in HOUSE-TEMPLATE.md. Character LoRAs are a separate lane
per character. Concept LoRAs only for measured failure modes. Style is
trained; content is prompted; characters are anchored.

## 8. Metrics reported per run

Jobs attempted/completed, wall time, images/hour, keeper rate, QC flag
distribution by taxonomy code, duplicate-hash count, determinism result.
Progress is reported from these numbers, not impressions.
