# ntr-corpus — registry

The provenance registry for the Nice Thoughts Ranch generated-media
corpus: a multi-lane library of studio-original images, animation,
video, Live2D, 3D, game assets, and manga produced to support the
studio's games and apps.

**This repository contains no media.** It holds the corpus's catalog,
standards, keeper registry, and per-item hashes — the records that
make every admitted item verifiable. Media is distributed separately
through gated Hugging Face datasets under the
[NiceThoughtsRanch](https://huggingface.co/NiceThoughtsRanch)
organization, behind an 18+ agreement gate and a
not-for-all-audiences tag.

> Adult content notice: the corpus itself is 18+ material featuring
> fictional adult characters only. No real person is depicted in any
> item. This registry is metadata about that corpus.

## Layout

- `_catalog/` — the normalized catalog (JSONL, versioned v1–v8)
  with per-version changelogs, dedupe dispositions, verdict
  overlays, and the keepers registry. Catalog v8: 601 rows —
  74 keeper, 82 accepted, 350 candidate, 86 rejected, 9 superseded.
  Every row carries its item's SHA-256, lifecycle state, rating,
  and provenance basis.
- `_standards/` — the rules the corpus is built under: the
  admission checklist (manifest complete, hash recorded, fictional
  adults only, license basis present), the corpus-factory contract,
  and the house standards for expressions, dialogue, and audio.

## Admission in one paragraph

An item enters a lane only as Tier P: studio-original production,
or third-party material whose rights holder granted redistribution,
verified per item and recorded in its manifest. Internal-only
reference material never enters a lane and is never uploaded
anywhere. Rejected material is excluded on sight. No manifest, no
admission.

## Access to the media

Media lanes are published as gated datasets (one per lane) under
the NiceThoughtsRanch Hugging Face organization as each lane's
first verified batch lands. Access requires accepting the gate
agreement: 18+ / age of majority, fictional adults only, no real
person depicted, no redistribution to minors, no use depicting
real persons.

## Rights

Registry contents © Nice Thoughts Ranch. The catalog's hashes and
metadata are published so any holder of a corpus item can verify
it against the record. Corpus media remains all rights reserved
and is available only through the gated datasets above.
