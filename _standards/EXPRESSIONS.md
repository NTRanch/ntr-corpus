# EXPRESSIONS.md — orgasm-expression / position concept catalog

Corpus standard. Source: the 2026-10-22 Civitai expressions review
(`~/workspace/civitai-expressions-20261022/REPORT.md`, Pax-gated) —
23 user-supplied models screened firsthand via the Civitai API:
8 ADOPTED (6 downloaded + 2 adopt-ready), 11 EMULATE-CLEAN
(native Danbooru recipes, no third-party weights), 3 REJECTED
(1 on sight — gallery minor flag; 2 as styles — franchise / living artist).

## Standing rules for everything below

- The corpus protective negative applies verbatim to every generation.
- Cast eye rule: heart pupils only with iris + rest of eye in natural color.
- **Ringed eyes — ADOPTED as a named eye-dialect variant (Owner ruling
  2026-10-25).** Token `ringed_eyes` (concentric-ring pupils), evidence:
  94 posts / 2.8% in the hypnosis census
  (`~/workspace/danbooru-hypnosis-mining-20261025/VOCAB-MAP.md`) — the one
  shaped-pupil dialect with real frequency that neither house lane named.
  It joins the variant set beside heart-shaped and spiral pupils in both
  eye lanes (Iris recipe and the Pony eye lane), under the same cast eye
  rule: rings render in the natural iris color, never as a color fill.
  A test render is owed before production trust, per the standing rule
  below.
- **Test renders are owed for every adopted LoRA before production trust.**
  Nothing below is production-cleared until a test render passes Pax's gate.
- 2311348 (Comic Last Page) is INTERNAL composition reference only
  (trained on third-party manga pages; provenance ruling 2026-10-22).
  Its outputs are not publish-tier.
- 1179881 (Climax Pony) carries the Pony caution: test render owed before
  any production use on Illustrious-family checkpoints.

## Adopted LoRA presets (primo `~/models/strobe-gen/`)

| File | Model (Civitai id) | Trigger | Strength | SHA-256 | Status |
|---|---|---|---|---|---|
| `orgasmic_heartblast.safetensors` | Orgasmic Heartblast (2045091) | `orgasmic heartblast` | ~1.0 | `A57F52FA…1509` | downloaded, test render owed |
| `eye_covering_orgasm_ill_v11.safetensors` | Eye covering orgasm (1857286) | `eye covering orgasm` | ~1.0 | `206329D0…421D` | downloaded, test render owed |
| `SexMachine_OrgasmFactory_IL.safetensors` | Sex machine / Orgasm factory (2593801) | per creator card | ~0.8–1.0 | `392645D7…EC3B` | downloaded, test render owed |
| `FComic_HardCore_LastPage_Creampie_Anime_IL_V01.safetensors` | Hentai Comic Random Generator (2311348) | per creator card | — | `570845BE…8805` | **internal reference only** |
| `MindBreak_ixl.safetensors` | Mind break [CONCEPT] (2131691) | `M1NDBR34K1NG` | ~0.8–1.0 | `9E97A85A…33E8` | downloaded, test render owed |
| `IntenseDoggyStyle_IL.safetensors` | Intense Doggy Style Sex (1973628) | per creator card | ~0.8–1.0 | `5E67E2D3…F3AF` | downloaded, test render owed |
| `Covering_Own_Mouth_IL.safetensors` (name TBD on download) | Covering own mouth (2332768) | per creator card | ~1.0 | — | adopt-ready, not downloaded |
| `Climax_Pony.safetensors` (name TBD on download) | Climax, cum, orgasm (1179881) | per creator card | ~1.0 | — | adopt-ready, Pony caution |

(Full hashes in the review REPORT.md downloads table.)

## Native recipes (no third-party weights — Illustrious vocabulary)

Prompt cores; scene dressing comes from the corpus spec.

1. **Explosive orgasm**: `ahegao, torogao, rolling eyes, open mouth, drooling,
   saliva, trembling, orgasm, female orgasm, blush, @_@` — wide-eyed variant:
   swap `rolling eyes` → `wide-eyed, constricted pupils`.
2. **Orgasm FX/SFX layer**: in-prompt `spoken heart, heart, trembling, motion
   lines, heart-shaped pupils`. Typographic SFX / speech bubbles are composited
   in post (manga lane) — diffusion text rendering is unreliable, standing finding.
3. **POV hands climax**: `pov, pov hands, fingering, spread legs, on back,
   legs up, female orgasm, female ejaculation, tears, tearing up, wavy mouth,
   furrowed brow, raised eyebrows, blush, open mouth, sweat, motion blur`.
4. **Impact orgasm face**: `half-closed eyes, rolling eyes, one eye closed,
   torogao, open mouth, drooling, saliva` — the asymmetry is the whole trick;
   expect to seed-hunt.
5. **Excessive orgasm**: `head back, arched back, trembling, motion lines,
   motion blur, female ejaculation, squirting, spread legs, steaming body`.
   Afterimage is the weakest native trait — `motion blur` approximates it.
6. **Head-back sitting**: `sitting, sex, sitting on person, face-to-face,
   arched back, head back, orgasm` + `front view` / `side view` for camera.
7. **Cowgirl**: `cowgirl position, girl on top, straddling, assertive female,
   bouncing breasts, trembling, orgasm, closed eyes, open mouth`.
8. **Laptop solo**: `solo, masturbation, fingering, female masturbation, laptop,
   computer, sitting, chair, spread legs, torogao, half-closed eyes, trembling,
   motion lines, pussy juice, looking down`.
9. **Fucked-silly expression cut**: `torogao, ahegao, rolling eyes, drooling,
   saliva, clenched teeth, trembling, steaming body, pillow grab, female orgasm`.
10. **Ahegao control**: `ahegao, rolling eyes, tongue out, open mouth, drooling`
    + explicit eye color.
11. **Suppression** (fallback for adopt-ready 2332768): `covering own mouth,
    hand over own mouth, trembling, orgasm, blush`.
12. **Pony climax fallback** (for 1179881): `climax, cum, trembling, overflow,
    spoken heart, impact lines` (Illustrious renders `impact lines` weakly).
13. **Squirting ahegao** (adapted 2026-10-23 from Civitai 2074718
    "DigitalDelights" — its LoRA is RentCivit/Rent-only and the Owner ruled
    it DO NOT USE the same day; vocabulary only, no weights): `ahegao,
    trembling body, drooling, tongue out, open mouth, one eye half closed,
    one eye wide open, orgasm, female ejaculation, excessive pussy juice,
    pussy juice trail, squirting`. The asymmetric-eyes pairing (one half
    closed, one wide) is the distinctive face — vary it per heroine. The
    weights file sits quarantined at primo `~/models/quarantine-nopublish/`
    and must never enter a workflow or ComfyUI's LoRA list.

Cleared native vocabulary from rejected packs (no style emulated):
`cross-section, uterus, cervix, internal cumshot, x-ray, deep penetration`
(internal cutaway — manga lane).

## Coverage-matrix mapping

New cells this catalog opens: **orgasm expressions** (its own axis),
**positions** (cowgirl/doggy/sitting), **sex machine**. Hypnosis crosses follow
the standing rule (hypnosis is the primary category). See CORPUS-SPECS-C.md
for the 17 generation specs (C-1…C-17) built from this catalog.

## Tooling verdict (from the review, recorded)

No MCP tool warranted (no state, no enforcement beyond the tagger+admission
pipeline, no daemon, no multi-client need). Catalog-first is the end state.
If the catalog outgrows this page, fold it into `local-strobe-asset-intake`.
