# Specs-H House Template

Codified 2026-10-23 from the keeper registry (`KEEPERS.md` / `keepers.json`).
A unique request = this invariant core + slot fills. The core never changes
between requests; consistency comes from that, not from the new words.

## Invariant core (verbatim, every generation)

STYLE prefix (prepended to the positive prompt):

```
masterpiece, best quality, absurdres, anime coloring, cel shading, flat color, sharp lineart, vibrant colors, detailed eyes, shiny hair,
```

Standard negative (verbatim; the protective tail is never edited out):

```
worst quality, low quality, lowres, blurry, jpeg_artifacts, watermark, signature, text, logo, realistic, photorealistic, 3d, cgi, sketch, chibi, super_deformed, bad_anatomy, bad_hands, bad_feet, extra_fingers, missing_fingers, extra_limbs, fused_fingers, deformed, cropped, out_of_frame, young, loli, child, teen, shota, multiple_girls, twins, multiple_persona
```

Negative variants (the only sanctioned edits):

- `NEG_NOTEXT` — for rounds where lettering is wanted in-frame: drop
  `watermark, signature, text, logo, ` → `watermark, signature, `.
  (In practice lettering is composited deterministically in post; see the
  S8 mug lineage. In-frame text remains the exception.)
- `NEG_NOGUY` — standard negative + `, 1boy, man, male, camera, cameraman`
  for solo frames where a partner or camera artifact keeps intruding.
- `multiple_girls` may be relaxed ONLY for yuri/harem items (corpus rule).

## Standard settings

| Field | Standard | Close-up bump |
|---|---|---|
| Checkpoint | Iris (Illustrious XL v1.1) | same |
| Sampler / scheduler | dpmpp_2m / karras | same |
| Steps | 28 | 36 |
| CFG | 5.5 | 5.5 |
| Size | 832×1216 | 1024×1536 |
| LoRA | none by default | per-slot only |

Inpaint fixes: masked, denoise 0.85–1.0 by purpose (0.85 blend, 1.0 redraw),
cfg 6.0, steps 32–36. Tight masks beat large ones on this checkpoint —
a large undefined area under the mouth inpaints as fabric (v25 lesson).

## Slots

```
{STYLE} 1girl, solo, adult woman, {HER: hair, build, signature features},
{ACT: what she is doing, cause visible in frame},
{STATE: expression + arousal state vocabulary, face AND body expressing it},
{SETTING: place, framing (cowboy shot / close-up / upper body)}
```

Slot rules:

- HER: age is always explicit (`adult woman`, `mature female` where apt).
  Hair color/arrangement and signature features (cow ears, gyaru tan,
  glasses) live here.
- ACT: the legibility rule applies — cause visible in contact, in frame.
  If a hand performs the act, the hand and its connection to her arm must
  be specified (`fingers gripping`, `hands squeezing`), never implied.
- STATE: use the adopted vocabularies — Specs-H types (H-E8 edge/cumming/
  just-came, H-E9–E12) and EXPRESSIONS.md recipes (e.g. #13 asymmetric
  eyes: `one eye half closed, one eye wide open, rolling eyes, uneven
  eyes`). Face and body both carry the state or the frame fails the gate.
- SETTING: one place, indoors/outdoors explicit, framing tag last.

## Worked example (the E10 winner, decomposed)

- HER: `long brown hair, low ponytail, cow ears, bell collar, micro bikini, cow print micro bikini, huge breasts`
- ACT: `lactation, leaking milk, female ejaculation, excessive pussy juice, squirting`
- STATE: `ahegao, trembling body, drooling, tongue out, open mouth, one eye half closed, one eye wide open, rolling eyes, dazed, stupefied, unfocused eyes, orgasm`
- SETTING: `cowboy shot, barn, indoors`
- Seed 19809 → `img-h-e10-b.png`, SHA-256 `3c8131d4…`

## LoRA doctrine (granularity)

- ONE house **style** LoRA for everything (the look), trained from this
  registry at the 20-diverse pilot gate; content never goes into it.
- **Concept** LoRAs only where seed-hunting is proven expensive (the
  latch is the standing candidate); one act per LoRA, trigger-worded.
- **Character** LoRAs are the separate Strobe B2 lane (per girl), never
  mixed into the corpus style set.
- Milking, breast size, rope, squirting etc. are prompt tags the base
  model already knows — no LoRA for anything a tag can say.
- Stack limit ~3 (style + character + concept), each A/B'd.
