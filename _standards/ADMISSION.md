# Corpus admission checklist (IDEA-0079 criteria, content form)

An item enters a lane only when ALL of these hold:

1. Tier P: studio-original, or third-party with redistribution
   granted by the rights holder (not a scraper-written license).
2. Manifest complete (manifest-template.json), SHA-256 recorded
   and matching the file on disk.
3. Fictional adults only; no real person depicted; consent legible
   in the work where the scene implies a dynamic.
4. Tags from the Danbooru vocabulary (pixai-tagger set); rating
   assigned from the Danbooru rating taxonomy.
5. Structured caption present (state-of-dress inventory, visible
   body parts, camera, mood palette).

Before any Hugging Face push of a batch, additionally:

6. Name sweep: no personal names anywhere (studio attribution
   only).
7. License basis present for every item in the batch.
8. Target repo NFAA-tagged and gated (G1 agreement; G3 manual
   approval for training-ready bundles).
9. Post-push logged-out verification: NFAA interstitial shows;
   gated files are not directly fetchable.
10. Batch reported with repo URL + verification results.

Tier I (internal-only) material is indexed under _internal-index/
and NEVER copied into a lane. Tier X is rejected on sight.
