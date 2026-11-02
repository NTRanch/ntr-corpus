# Audio Factory v1 — the audio lane under the Corpus Factory contract

Owner directive 2026-10-23 23:08 PDT: standardize audio the same way as
LoRA training and animation. This document is the audio twin of
CORPUS-FACTORY.md; where they overlap, the Factory contract governs.

## 1. Voice identity (locked before production)

- Each heroine has ONE synthetic voice identity: an engine, a voice/seed
  configuration, and a reference render set. The identity record lives in
  the catalog; changing it is a new identity version, never a silent swap.
- No real-person likeness, ever (Tier X rule). Synthetic voices only.
- Her identity stays constant across all states and arc stages; what
  changes is performance, never the voice itself.

## 2. State matrix (per girl)

Cells (Owner, 2026-10-23 23:07 PDT): orgasm; edging; masturbating gently;
masturbating feverishly; kink-specific (matched to her END themes);
sex-toy play; corruption-arc enjoyment (staged: hesitant -> warming ->
eager -> surrendered, same voice throughout).
Minimum 2 variants per cell where engine quality holds; a cell with no
acceptable render is recorded as FAILED with the engine note, never
filled with a substandard take.

## 3. Asset contract (audio manifest)

Per asset: `asset_id` (girl + cell + variant), `sha256`, engine name +
version + checkpoint hash, voice identity id + version, generation seed
and full parameter record, text/prompt where the engine takes one,
duration, sample rate, channels, loudness (integrated LUFS + true peak),
provenance (source_type, adult_basis — fictional adult character),
license_status (production-cleared only for publish-clear engines),
lifecycle state (candidate | accepted | keeper | superseded | rejected),
owner ear verdict + timestamp when ruled.

## 4. Determinism

- Engines and versions are pinned per production run; a run records its
  full environment in the batch manifest.
- Fixed seed per (girl, cell, variant). Where the engine is seedable, a
  double-render of a pilot cell must hash-match before volume proceeds —
  the same proof discipline as the image runner and codeanim.
- Where an engine proves non-deterministic, that is recorded as its
  class; assets from it are `seed-recorded, output-unique` and are never
  described as reproducible.

## 5. Technical standard

- Masters: WAV, 48 kHz, mono for voice/reaction (stereo only for designed
  SFX), trimmed of leading/trailing silence beyond 50 ms.
- Loudness: masters normalized to -16 LUFS integrated, true peak <= -1 dBTP;
  the normalization tool + version is recorded per batch.
- Game derivatives (generated at admission, versioned like image packs):
  OGG Vorbis q6, loop-trimmed variant where the cell is a loop candidate,
  and a contact audition strip per girl for the owner's ear gate.
- No clipping, no DC offset, no engine watermark tones; QC flags are
  taxonomy codes in the catalog, same as image QC.

## 6. Admission

Automation sorts; the owner's ear promotes. Nothing enters the corpus as
accepted on a model's say-so. Failed cells and rejected takes stay in the
catalog with their flags — the failure record is part of the standard.
