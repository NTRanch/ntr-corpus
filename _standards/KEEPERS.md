# Specs-H Keeper Registry

Machine records: `keepers.json` beside this file (full recipe cards).
Primo copy: `~/ntr-corpus/_standards/KEEPERS.md` + `keepers.json`.

Status key: KEEPER = owner named it a keeper. ACCEPTED = owner words on record.
ACCEPTED-BY-CONTINUATION = owner-directed round, carried forward unrejected.
PAX-SELECTED = owner-directed round, Pax picked the winner, no separate verdict.
SUPERSEDED = replaced or owner-rejected; record only, do not ship.

Confirmed cards: 52 (incl. 1 superseded). Candidates awaiting verdict: 12.

## House-LoRA gate

Pilot at **20 diverse keepers**, production candidate at **40**. Diversity rules:
- >=6 distinct women/hair
- >=5 act/expression families
- no family >25% of the training subset
- mixed framings (close-up / upper body / wider)
- every item tagger-passed and owner-accepted

## Keepers

### img-h-e6 — ACCEPTED
- H-E6 pumps, courtesy-beg face
- File: `~/ntr-corpus/images/_candidates/specs-h-v4/img-h-e6.png`
- SHA-256: `53efeefd116b5db98fc71031c01cac91d677a2fac5160c28080c3f3e54146c09`
- Basis: Owner accepted the v4 directed regen; later served as the combo3 parent.
- Recipe: checkpoint=Iris.safetensors, seed=9766, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-e6-combo3 — ACCEPTED
- H-E6 face+torso combo inpaint
- File: `~/ntr-corpus/images/_candidates/specs-h-v10/img-h-e6-combo3.png`
- SHA-256: `433d691181d5443b923d5f328ffb9a2cf895a4a3753831ec4936015f1ae9c505`
- Basis: Owner 2026-10-23 13:23 PDT: "this version is good".
- Method: combined face+torso masked inpaint from the v4 original, one sampling pass, denoise 0.85, seed 3503; unified prompt (ecstasy face + grip squeeze + clear dome pumps leaking) (parent: img-h-e6, sha 53efeefd)

### img-h-e10-b — ACCEPTED-BY-CONTINUATION
- H-E10 earnest host, squirting ahegao
- File: `~/ntr-corpus/images/_candidates/specs-h-v14/img-h-e10-b.png`
- SHA-256: `3c8131d495e09d6c0d2ca5e712232ff48690e5d6b2fbbf17c56f0fd3b792a6e5`
- Basis: Owner-directed recipe-#13 asymmetric-eyes hunt (v14); carried into later rounds unrejected.

### img-h-e11-r3 — KEEPER
- H-E11 smirk-collapse, heavy rope + ball gag
- File: `~/ntr-corpus/images/_candidates/specs-h-v18/img-h-e11-r3.png`
- SHA-256: `724a4f281a5584dd44dcf49187779344ac7558ce4162ee5c1ebc0f86ae93193c`
- Basis: Owner 2026-10-23 19:01 PDT: v19 sheet top right = keeper.

### img-h-e12-b — ACCEPTED-BY-CONTINUATION
- H-E12 trait-surfacing, milk-spray orgasm
- File: `~/ntr-corpus/images/_candidates/specs-h-v16/img-h-e12-b.png`
- SHA-256: `7000fad5aa141475d9d89d7355529621ccf9de83f83a03d4395c5c56405f070e`
- Basis: Owner directive 2026-10-23 15:55 PDT; only seed with legible squirt AND uneven eyes.
- Recipe: checkpoint=Iris.safetensors, seed=19811, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s2-a — ACCEPTED
- H-S2 x-ray service A
- File: `~/ntr-corpus/images/_candidates/specs-h-v7/img-h-s2-a.png`
- SHA-256: `a5b87518335fadccf0d3aeaeadfc94f4e7e2a2ef4c62bff6e1ef0e20f6d7032d`
- Basis: Owner 2026-10-23 12:36 PDT: "all 3 of those are good".
- Recipe: checkpoint=Iris.safetensors, seed=9118, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s2-b — ACCEPTED
- H-S2 x-ray service B
- File: `~/ntr-corpus/images/_candidates/specs-h-v7/img-h-s2-b.png`
- SHA-256: `7bf2f6497b70fe46fb3dbb7ab1d123e111894528500d91a7871b64cd7b74be2f`
- Basis: Owner 2026-10-23 12:36 PDT: "all 3 of those are good".
- Recipe: checkpoint=Iris.safetensors, seed=9119, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s2-c-fixed — ACCEPTED
- H-S2 x-ray C, inpaint-fixed
- File: `~/ntr-corpus/images/_candidates/specs-h-v8/img-h-s2-c-fixed.png`
- SHA-256: `4140d91f7dcb985f711c2246f910cfd28abbf8f99cc5a9205d1ec11330d7b5ad`
- Basis: Owner 2026-10-23 12:53 PDT: "that one is great nice job".
- Method: masked inpaint from the v7 C image; feathered pelvis/buttock mask; denoise 0.88; seed 9120 (parent: img-h-s2-c, sha 39ccc5c7)

### img-h-s8-final-v15 — ACCEPTED-BY-CONTINUATION
- H-S8 engorgement relief, mug final (royal script)
- File: `~/ntr-corpus/images/_candidates/specs-h-v14/img-h-s8-final-v15.png`
- SHA-256: `7bfa1cdc5364509a62f44e1175884d0bb2e9ca6590084e98ad26e2c06409df78`
- Basis: Owner-directed lettering rounds v12-v15; royal-script printed look is his spec.

### img-h-s8-m1 — PAX-SELECTED
- H-S8 milking close-up, parent of v20 final
- File: `~/ntr-corpus/images/_candidates/specs-h-v20/img-h-s8-m1.png`
- SHA-256: `3fbd44f09ef59d2f051a8b82cfd350425452a0922957aa18ca697b2ed36ad764`
- Basis: Owner-directed close-up round (v20 quality bump); Pax winner of 4 seeds.

### img-h-s8-final-v20 — PAX-SELECTED
- H-S8 milking close-up final, big royal script
- File: `~/ntr-corpus/images/_candidates/specs-h-v20/img-h-s8-final-v20.png`
- SHA-256: `b4badbca5b0097724f1afddc5e8f9408dab506afcb52743c44ef149217e292fc`
- Basis: Lettering pass 2 on m1 recorded as the keeper of that pass; no separate owner verdict.

### img-h-x9-keeper — KEEPER
- Self-suckle latch, breast-to-lips (from seed 19409 via v28 inpaint 20703)
- File: `~/ntr-corpus/images/_candidates/specs-h-v28-x9/img-h-x9-keeper.png`
- SHA-256: `a7dbdd69293ab6f747792fddd2d520c907128740001aae3da5e4182d6a724ed3`
- Basis: Owner 2026-10-23 18:13 PDT: "this one is a keeper".

### img-h-x7-hand20103-recolor — SUPERSEDED
- x7 hand fix v24+v26 recolor (superseded by v29 round)
- File: `~/ntr-corpus/images/_candidates/specs-h-v26/img-h-x7-hand20103-recolor.png`
- SHA-256: `bc60b91e4f8d2f24ae1ef4e685c1dbb60cd29e93496251978b19df33b9d584b6`
- Basis: Owner 2026-10-23 18:12 PDT rejected the delivery: "the hands don't match her actions". Kept as record; do not ship.
- Method: deterministic recolor: teal-slate hand pixels (G>R) in x>=540,y>=760 remapped to breast skin tone (232,181,178) scaled by per-pixel luminance; lineart, areola, milk spray untouched

### img-h-x6 — KEEPER
- Self-suckle mood keeper (hearts, latch implied)
- File: `~/ntr-corpus/images/_candidates/specs-h-v22/img-h-x6.png`
- SHA-256: `89745e5949ee3898ea0b46302653f6a387b769378ae9729b0afdbbe9157a15ed`
- Basis: Owner 2026-10-23 18:57 PDT: "keeper" (on the reposted single).
- Recipe: checkpoint=Iris.safetensors, seed=19406, steps=36, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-x5-polish — KEEPER
- Self-suckle x5 polished (uneven eyes, hearts, spray, warm skin)
- File: `~/ntr-corpus/images/_candidates/specs-h-v23/img-h-x5-polish.png`
- SHA-256: `3d9deff569e4e77bbab15f5d2df8c234e16389fbc5ada1f4b0323e4a24fcba8a`
- Basis: Owner 2026-10-23 18:58 PDT: "keeper" (on the reposted polished single). Supersedes his queued fix directive on the unpolished parent frame.
- Method: img2img polish of specs-h-v22 img-h-x5.png (seed 19405)

### img-h-s7 — KEEPER
- H-S7 soaking solo (v13 redo)
- File: `~/ntr-corpus/images/_candidates/specs-h-v13/img-h-s7.png`
- SHA-256: `d3e0cc315abe49a3f0adff62dfac8efe1dc64fbf481fb57682681d8475af5504`
- Basis: Owner 2026-10-23 19:01 PDT: v19 sheet bottom left = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=9781, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s8-c — KEEPER
- H-S8 topless silver (v13)
- File: `~/ntr-corpus/images/_candidates/specs-h-v13/img-h-s8-c.png`
- SHA-256: `91207e85388efce616a7cb2a853790885030fdf92e2468a862d33e40407f2e98`
- Basis: Owner 2026-10-23 19:01 PDT: v19 sheet bottom center = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=9782, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s7-v12 — KEEPER
- H-S7 unseen performance, guy removed (v12)
- File: `~/ntr-corpus/images/_candidates/specs-h-v12/img-h-s7.png`
- SHA-256: `33c710cc1ac37e7383e607baa1fb99e5b2866230c67baaf86a4d22ecac16c8ee`
- Basis: Owner 2026-10-23 19:08 PDT: v12 fixes sheet bottom left = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=9781, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s8-v12 — KEEPER
- H-S8 mug 'for master' pseudo-text original (v12, seed 9782)
- File: `~/ntr-corpus/images/_candidates/specs-h-v12/img-h-s8.png`
- SHA-256: `901fc013bb32834e207b16d23f3f5bac911698ed016737a77e8f45ffaf7818df`
- Basis: Owner 2026-10-23 19:08 PDT: v12 fixes sheet bottom center = keeper. Note: frame carries model-generated pseudo-text along the bottom edge, keepered as-is.
- Recipe: checkpoint=Iris.safetensors, seed=9782, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s9-r2 — KEEPER
- H-S9 hostess, both breasts out over apron (v36 expose round)
- File: `~/ntr-corpus/images/_candidates/specs-h-v36/img-h-s9-r2.png`
- SHA-256: `6889d1411d713094ea37973fba29d3cabb67517fa78353cd6ef95c885e98b5db`
- Basis: Owner 2026-10-23 22:26 PDT: "2nd ... keeper" on the combined v36 sheets presentation (counted in display order: cell 2 = S9-r2). Pax had picked r1; owner pick governs.
- Recipe: checkpoint=Iris.safetensors, seed=21502, steps=36, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-s11-r1 — KEEPER
- H-S11 squirt-climax, standing profile (v36 expose round)
- File: `~/ntr-corpus/images/_candidates/specs-h-v36/img-h-s11-r1.png`
- SHA-256: `3baaa9ca2010336cfe6e5b3dd94ac19769d8a372c0b48bed8b2b7027936bb14a`
- Basis: Owner 2026-10-23 22:26 PDT: "the 4th one ... keeper" on the combined v36 sheets presentation (counted in display order: cell 4 = S11-r1). Pax had picked r3; owner pick governs.
- Recipe: checkpoint=Iris.safetensors, seed=21511, steps=36, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-s9-r1 — KEEPER
- H-S9 hostess, apron aside, one breast fully exposed (v36)
- File: `~/ntr-corpus/images/_candidates/specs-h-v36/img-h-s9-r1.png`
- SHA-256: `8168d20cc1a6ce706dc152e93ccc475989520e2a55930b8815d7be3b7c2daf77`
- Basis: Owner 2026-10-23 22:28 PDT: "1st one with her tit out is a keeper" (first exposed-breast cell of the S9/S11 sheet = S9-r1).
- Recipe: checkpoint=Iris.safetensors, seed=21501, steps=36, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-e10-r2 — KEEPER
- H-E10 stupefied squirt retry r2 (grey-mauve cast, owner keepered as-is)
- File: `~/ntr-corpus/images/_candidates/specs-h-v35/img-h-e10-r2.png`
- SHA-256: `8cc667a36ccc0735e3aa3645b083f8e0b1e621227c57e5aa5c16289a00de94cb`
- Basis: Owner 2026-10-23 22:39 PDT, by labeled screenshot: img-h-e10-r2 = keeper. Note: the grey-mauve skin cast Pax flagged as a defect stands per owner verdict.
- Recipe: checkpoint=Iris.safetensors, seed=21402, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-e10-r3 — KEEPER
- H-E10 stupefied squirt retry r3 (clean warm skin)
- File: `~/ntr-corpus/images/_candidates/specs-h-v35/img-h-e10-r3.png`
- SHA-256: `3dd568b11fba54be667ca447e9c6a9b393df2b1021a2a15291c1e4eb1e402474`
- Basis: Owner 2026-10-23 22:39 PDT, by labeled screenshot: img-h-e10-r3 = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=21403, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s8t-r2 — KEEPER
- H-S8 tankard retry r2 (squeezing over the table)
- File: `~/ntr-corpus/images/_candidates/specs-h-v35/img-h-s8t-r2.png`
- SHA-256: `f02b0c63d2f67cc3ab0bb14cf0ee3112b2a9b74cfc0e162edd8e90a282d6a9dd`
- Basis: Owner 2026-10-23 22:38 PDT, by labeled screenshot: img-h-s8t-r2 = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=21422, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-s8t-r3 — KEEPER
- H-S8 tankard retry r3 (milking pumps into barrel)
- File: `~/ntr-corpus/images/_candidates/specs-h-v35/img-h-s8t-r3.png`
- SHA-256: `e3b32c66b43e6915bea9b1315c85a85377ba9a2b4a24448265a81b191c4c2505`
- Basis: Owner 2026-10-23 22:38 PDT, by labeled screenshot: img-h-s8t-r3 = keeper.
- Recipe: checkpoint=Iris.safetensors, seed=21423, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=1024, height=1536

### img-h-s8-pail-v48-a — KEEPER
- H-S8 pail v48 a — under-table milking cups, glasses of milk
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-pail/img-h-s8-pail-v48-a.png`
- SHA-256: `448b5aa5c7d19aa9ceb309712d0e80b86bf2835c694381ba4d4c23e93ebe24e0`
- Basis: Owner keep 2026-10-24 (gate sheet 1, top row a-c).
- Recipe: checkpoint=Iris.safetensors, seed=17221, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s8-pail-v48-b — KEEPER
- H-S8 pail v48 b — hugging the milking canister, top-down
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-pail/img-h-s8-pail-v48-b.png`
- SHA-256: `dc166443eb6cd03438057822c75efedd5712faa5b75ff379157d94cd7c2dcd46`
- Basis: Owner keep 2026-10-24 (gate sheet 1, top row a-c).
- Recipe: checkpoint=Iris.safetensors, seed=17222, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s8-pail-v48-c — KEEPER
- H-S8 pail v48 c — top-down, spraying into floor pans
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-pail/img-h-s8-pail-v48-c.png`
- SHA-256: `4be1114a2bfe2686ef309c72897354db2b714d7f487bce8a41e746fab24c9f18`
- Basis: Owner keep 2026-10-24 (gate sheet 1, top row a-c).
- Recipe: checkpoint=Iris.safetensors, seed=17223, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s12b-e2r-a — KEEPER
- H-S12b redhead cow-print variation a — full cow-print dress, barn
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-s12b/img-h-s12b-e2r-a.png`
- SHA-256: `c34135ab4af300be638e307ed3eeab76634b18c9eded8848409567479a91a785`
- Basis: Owner keep 2026-10-24 (all three cow girls). Directed edit of keeper e2: red hair + cow print.
- Recipe: checkpoint=Iris.safetensors, seed=21562, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s12b-e2r-b — KEEPER
- H-S12b redhead cow-print variation b — cow print, warm yellow cast
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-s12b/img-h-s12b-e2r-b.png`
- SHA-256: `e193f1aeb9f9cf1b4244b4bf22a8828cbc6e567128a3c0e8869cc51f73f6602f`
- Basis: Owner keep 2026-10-24 (all three cow girls, kept despite the yellow cast Pax flagged).
- Recipe: checkpoint=Iris.safetensors, seed=21571, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-h-s12b-e2r-c — KEEPER
- H-S12b redhead cow-print variation c — cow-print bodysuit and stockings
- File: `~/ntr-corpus/images/_candidates/specs-h-v48-s12b/img-h-s12b-e2r-c.png`
- SHA-256: `dc4928d65f07c41f32ebfa98cce534e5c2252d57fee814bd1321fea44a06c88c`
- Basis: Owner keep 2026-10-24 (all three cow girls).
- Recipe: checkpoint=Iris.safetensors, seed=21572, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-030-r1 — KEEPER
- cov-030 retry r1 — solo couch version (kept over the couple version)
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-030-r1.png`
- SHA-256: `cf7e6ea62b19064735ac2dc3288dc5d96c4a176a95485b484bd0ffe9c1158bc4`
- Basis: Owner keep 2026-10-24, retry row A1 (kept 1, 3, 4).
- Recipe: checkpoint=Iris.safetensors, seed=33115, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-032-r1 — KEEPER
- cov-032 retry r1 — early-20s recast
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-032-r1.png`
- SHA-256: `d4a6e173571230d6369672b127f1d1cdab76f95f4b62e4f9398ae3f602a57012`
- Basis: Owner keep 2026-10-24, retry row A1.
- Recipe: checkpoint=Iris.safetensors, seed=33101, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-032-r2 — KEEPER
- cov-032 retry r2 — late-30s cougar recast
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-032-r2.png`
- SHA-256: `1bc7af41b029aa67ab87b25c486670bd114d925c23a3f95d126db786bf459994`
- Basis: Owner keep 2026-10-24, retry row A1.
- Recipe: checkpoint=Iris.safetensors, seed=33102, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-009-c3d — KEEPER
- hx-009 covert v3 d — x-ray frame reveal, office girl
- File: `~/ntr-corpus/images/_candidates/covert-v3-20261024/img-hx-009-c3d.png`
- SHA-256: `5d7a808760c31c51552312fe2a0254b6b7b91417ea9d627e4f613d7b145dba41`
- Basis: Owner keep 2026-10-24 (the 4th of the covert v3 row; the only true reveal-window device of the round).
- Recipe: checkpoint=Iris.safetensors, seed=35104, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-036-r1 — KEEPER
- cov-036 retry r1 — cougar-recast, early-20s version (lingerie, morning stretch)
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-036-r1.png`
- SHA-256: `8f6c36329dd4aa76eccb75849d9a2c0c00d7861f2fbe24edeb569694c9afd19b`
- Basis: Owner keep 2026-10-25, retry row A2 (kept 1, 2).
- Recipe: checkpoint=Iris.safetensors, seed=33103, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-036-r2 — KEEPER
- cov-036 retry r2 — cougar-recast, late-30s cougar version (lingerie, morning stretch)
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-036-r2.png`
- SHA-256: `4d8e95ded6b2f9bf2835c937989e070843713a5a79368d39ac4856cd4e422a88`
- Basis: Owner keep 2026-10-25, retry row A2 (kept 1, 2).
- Recipe: checkpoint=Iris.safetensors, seed=33104, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-037-r1-fix2 — KEEPER
- cov-037 retry r1, flesh-recolor fix2 — paizuri tip corrected green to flesh
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-037-r1-fix2.png`
- SHA-256: `901be41aed8ca6b7bf744282e16671c91d1afa545087f635aed72379d10540c2`
- Basis: Owner keep-with-edit 2026-10-25, row A2 cell 3; fix2 accepted by owner ("this works"). Deterministic PIL recolor, disclosed.
- Method: deterministic PIL hue-remap of the rendered tip region (saturation/value preserved, outline + slit detail kept) on the parent render; no regeneration (parent: img-cov-037-r1, sha bd367444)

### img-cov-037-r5d — KEEPER
- cov-037 directed r5d — eager paizuri, clarified owner definition (aroused, devoted to please)
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-cov-037-r5d.png`
- SHA-256: `057f683d9032294dd865a4337d5eaa67984cceb9925126d693942581ae1d9e8c`
- Basis: Owner keep 2026-10-25, row A2d cell 4.
- Recipe: checkpoint=Iris.safetensors, seed=33154, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-037-r6a — KEEPER
- cov-037 directed r6a — inverted under-him sucking composition, spiral eyes
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-cov-037-r6a.png`
- SHA-256: `a8b98b5a18c9bba66c0916751f0560503343b851bd65172e05dc365c858b1aaf`
- Basis: Owner keep 2026-10-25, row A2e cell 1 — over Pax FAIL gate; owner governs.
- Recipe: checkpoint=Iris.safetensors, seed=33161, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-037-r7a — KEEPER
- cov-037 directed r7a — her orgasm face as her paizuri makes him cum
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-cov-037-r7a.png`
- SHA-256: `1d9d05e7741667e2b5d6410b913304db549b95edb16f144bee6f297740ead3ed`
- Basis: Owner keep 2026-10-25, row A2f cell 1.
- Recipe: checkpoint=Iris.safetensors, seed=33171, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-037-r8a — KEEPER
- cov-037 directed r8a — deepthroat side profile, elongated sucking face, tears, hatched blush
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-cov-037-r8a.png`
- SHA-256: `343e66c7c7acd8ac7bea4ecf9aaf6bf5f1e9fd3add838941b08a7cbb20ee33cf`
- Basis: Owner keep 2026-10-25, row A2g cell 1.
- Recipe: checkpoint=Iris.safetensors, seed=33181, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-042-r1 — KEEPER
- cov-042 retry r1 — mating press, nakadashi, legs up, overwhelmed
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-042-r1.png`
- SHA-256: `e68ddc233fcfea57d1fddd171f698c762655b9d3b0d204dcceb4b47d73a43cbd`
- Basis: Owner keep 2026-10-25, retry row A3 cell 1.
- Recipe: checkpoint=Iris.safetensors, seed=33119, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-046-r1 — KEEPER
- cov-046 retry r1 — adult college sophomore recast, anal tail-plug presenting
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-046-r1.png`
- SHA-256: `d8990c98c8cd739a6644bdecaefeb814276ef7387e7bc9bff5a711e2a7b0b520`
- Basis: Owner keep 2026-10-25, retry row A3 cell 3.
- Recipe: checkpoint=Iris.safetensors, seed=33105, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-cov-046-r2 — KEEPER
- cov-046 retry r2 — adult college sophomore recast, anal tail-plug presenting
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-cov-046-r2.png`
- SHA-256: `11b7ece65fb539f92300e627fa589205a1a50f4c89a432fc7393a0929b860d7d`
- Basis: Owner keep 2026-10-25, retry row A3 cell 4.
- Recipe: checkpoint=Iris.safetensors, seed=33106, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-003-r1 — KEEPER
- hx-003 retry r1 — hypnosis lactation, kitchen trance, uneven pupils
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-hx-003-r1.png`
- SHA-256: `754557ca05109134bdd472389d75e12de21cb8d542a0534e1f71a0e659c473bb`
- Basis: Owner keep 2026-10-25, retry row B1 cell 1.
- Recipe: checkpoint=Iris.safetensors, seed=33107, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-003-r3a — KEEPER
- hx-003 redo r3a — leaking nipples, aroused blush, openly delighted at being seen
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-hx-003-r3a.png`
- SHA-256: `ac53326e130e591308c7462982a655cd2fb834bbf72a16faeb6ccd2cb14e25d2`
- Basis: Owner keep 2026-10-25, row B1b cell 1 (all three r3 kept).
- Recipe: checkpoint=Iris.safetensors, seed=33211, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-003-r3b — KEEPER
- hx-003 redo r3b — leaking nipples, brazen delight
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-hx-003-r3b.png`
- SHA-256: `4d22939a0bd056a81d66c2f674f7499467c406c5edd95bade84765b126ccddf2`
- Basis: Owner keep 2026-10-25, row B1b cell 2 — over Pax PARTIAL gate; owner governs.
- Recipe: checkpoint=Iris.safetensors, seed=33212, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-003-r3c — KEEPER
- hx-003 redo r3c — leaking through maid blouse, sly sideways glance, secret pleasure
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261025/img-hx-003-r3c.png`
- SHA-256: `792f8d2bf36de5d731fdc04dc1f27d9b2d81e9f87fb929dabc94bef68065cd1c`
- Basis: Owner keep 2026-10-25, row B1b cell 3 (Pax PASS-on-directive).
- Recipe: checkpoint=Iris.safetensors, seed=33213, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-004-r2 — KEEPER
- hx-004 retry r2 — deep trance ahegao, heart pupils
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-hx-004-r2.png`
- SHA-256: `e565c40828ca13e5b14fa31315b149ad87a50e29b2574c0a0fd8c9245bdd7bff`
- Basis: Owner keep 2026-10-25, retry row B1 cell 4 — over Pax FAIL-on-directive (symmetric pupils); owner governs.
- Recipe: checkpoint=Iris.safetensors, seed=33110, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

### img-hx-005-r1 — KEEPER
- hx-005 retry r1 — hypnosis netorare, hotel room, spiral eyes, wedding ring
- File: `~/ntr-corpus/images/_candidates/eye-pass-retries-20261024/img-hx-005-r1.png`
- SHA-256: `a43d7d849b05e533058649f1e1d221fd755f6191e347745ebb8513195a2c84f9`
- Basis: Owner keep 2026-10-25, retry row B2 cell 1 — over Pax FAIL-on-directive (symmetric spirals); owner governs.
- Recipe: checkpoint=Iris.safetensors, seed=33111, steps=28, cfg=5.5, sampler=dpmpp_2m, scheduler=karras, width=832, height=1216

## Candidates awaiting owner verdict
- `specs-h-v11/img-h-e9.png` (seed 9769) — H-E9 predator grin, Pax gate full land; owner verdict pending
- `specs-h-v11/img-h-s10.png` (seed 9823) — H-S10 self-proposed arrangement (fenced), Pax gate land; verdict pending
- `specs-h-v11/img-h-s12-a/b/c.png` (seed 9770) — H-S12 arousal-swelling 3-state set, Pax gate land; verdict pending
- `specs-h-v22/img-h-x4.png` (seed 19404) — Self-suckle act winner (tongue on lifted nipple); verdict pending
- `specs-h-v29/img-h-x7-hand20805.png` (seed 20805) — x7 round 2 PARTIAL: one coherent gripping hand with spray at the left breast; pinching hand absent; no furniture (20802 has the hand but a table edge intrudes)
- `specs-h-v35/img-h-e12-r1.png` (seed 21411) — E12 RETRY WINNER (Pax pick): strongest eye split yet (one rolled white, one open) + dual milk spray + squirt starburst. Delivered 19:1x for verdict.
- `specs-h-v35/img-h-s8t-final.png` (seed 21424) — S8 TANKARD RETRY FINAL: r4 act winner + deterministic royal-script lettering, sha bd365496. Pax-selected, awaiting verdict.
- `eye-pass-retries-20261025/img-cov-042-r3a.png` (seed 33191) — cov-042 redo r3a: face visible, uneven corrupted orgasm (magenta swirl heart eye vs white heart-pupil eye). Pax STRONG PASS. Banked unruled; cov-042 slot parked for owner circle-back.
- `eye-pass-retries-20261025/img-cov-042-r3b.png` (seed 33192) — cov-042 redo r3b: uneven eyes land (blue heart vs magenta), composition tangles. Pax PARTIAL. Banked unruled; slot parked.
- `eye-pass-retries-20261025/img-cov-042-r4a.png` (seed 33120) — cov-042 r4a: same-seed face-reveal attempt on r2; base scene did not hold (recomposed inverted face close-up). Banked unruled; slot parked.
- `eye-pass-retries-20261025/img-cov-042-r4b.png` (seed 33193) — cov-042 r4b: same-prompt face-reveal attempt; base scene did not hold. Banked unruled; slot parked.
- `eye-pass-retries-20261025/img-hx-009-x2.png` — hx-009 x-ray composite x2: rimmed x-ray window over her CLOSED coat; gold rope harness + nipple clamp over the dark dress beneath; outside fully clothed. First render implementing the device. Verdict pending owner.

## Failed rounds (lessons kept)
- **specs-h-v30-x8** — Right-hand distinguishability inpaint on x8 20604 FAILED all 4 seeds: 20901 fingers scrambled into the milk splash (crop-verified), 20902 green-yellow block artifact at the mouth, 20903/20904 splash masses. The v27 fist remains the best x8 hand state. Lesson: mask sat inside the milk-splash zone and the model filled it with splash; a tighter fist-only mask excluding the splash is the next lever.
- **specs-h-v29 (partial)** — Full bottom-band mask invited furniture (table edges) in 20802/20804 and palette shift in 20801; white glove hand in 20806. Best = 20805 partial.
