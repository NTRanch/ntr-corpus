# SPIKE — Wan2.2 I2V NSFW LoRA (lopi999) as NTR corpus video-lane opener

Date: 2026-10-22 (America/Los_Angeles). Internal evidence only. Nothing was uploaded anywhere.
Spike dir: `~/ntr-corpus/video/_incoming/spike1/`

## 1. LICENSE VERDICT — publish tier is BLOCKED BY LICENSE

### The LoRA (lopi999/Wan2.2-I2V_General-NSFW-LoRA)

- The Hugging Face repo declares **no license at all**: the API `cardData` has no `license` field, and the README contains no license text. The card in full is a stub. Verbatim, the license-relevant card content is:

  Front matter:
  > base_model: Wan-AI/Wan2.2-I2V-A14B
  > instance_prompt: nsfwsks

  Body:
  > HuggingFace mirror of https://civitai.com/models/1307155
  >
  > You should use `nsfwsks` to trigger the image generation.

  With no grant, the file as we hold it is all-rights-reserved by default: no redistribution right, no derivative right, no commercial-use right is conveyed by this artifact.

- The canonical source (Civitai model 1307155, "(wan 2.2 experimental) WAN General NSFW model"; lopi999 is only the mirror uploader) carries Civitai permission flags, read from the Civitai API on 2026-10-22:
  - `allowCommercialUse: ["RentCivit"]` — commercial use is permitted **only** as generation rented through Civitai's own service. Commercial use of outputs anywhere else (our games, our HF datasets, any storefront) is **not** granted.
  - `allowDerivatives: true`, `allowDifferentLicense: true`, `allowNoCredit: true`.

- **Which constraint binds:** the operative block for publish tier is **commercial use of outputs** (RentCivit-only at the source, and no grant whatsoever on the HF copy), with **weights redistribution** also ungranted. Derivative *training* is the one thing the Civitai flags allow — but a derivative of these weights would still inherit the output-commercial-use cap in any sane reading, so it does not open a publish path either.

### The base model (Wan-AI/Wan2.2-I2V-A14B)

- Declared license: **Apache 2.0** (`license: apache-2.0` in the card and `license:apache-2.0` tag). Verbatim from its README's License Agreement section:

  > The models in this repository are licensed under the Apache 2.0 License. We claim no rights over the your generated contents, granting you the freedom to use them while ensuring that your usage complies with the provisions of this license.

  The base model is publish-clean: Apache 2.0, and the licensor expressly claims no rights over generated contents. Everything built from the base model alone is ours to publish.

## 2. What was downloaded

Placement follows the existing strobe-gen pattern: weights under `~/models/wan-video/`, resolved through a new `wan:` section appended to `~/strobe-gen-test/extra_model_paths-aur.yaml` (backup at `extra_model_paths-aur.yaml.bak-20261022-wan`). The fp8-scaled stack was chosen over fp16 because rose's llama-server already holds ~19 GB of the A6000's 46 GB; fp16 (2 × 28.6 GB) does not fit that reality, fp8 (2 × 14.3 GB) does.

| File | Source | Bytes | SHA-256 |
|---|---|---|---|
| loras/NSFW-22-H-e8.safetensors | lopi999/Wan2.2-I2V_General-NSFW-LoRA | 613,516,752 | 34e2144d3cd65360f97d09ccbe03e1c39a096df6c9234af5fe3899d1b63cda39 |
| loras/NSFW-22-L-e8.safetensors | lopi999/Wan2.2-I2V_General-NSFW-LoRA | 613,516,752 | d6b783742f4d5fd63a0223ae1d5bf64fc995a6b408480ac2a00528ae0d4146db |
| diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors | Comfy-Org/Wan-2.2 (split_files) | 14,294,742,832 | 6122e79d55e0f235698d11d657f3b196c5273c830da00b2b013c5a048d5e6a42 |
| diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors | Comfy-Org/Wan-2.2 (split_files) | 14,294,742,832 | 5471a457b6ac404202a5fbe6c11595a3d5641fc766b00f38763f72303fffc21e |
| text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors | Comfy-Org/Wan-2.2 (split_files) | 6,735,906,897 | c3355d30191f1f066b26d93fba017ae9809dce6c627dda5f6a66eaa651204f68 |
| vae/wan_2.1_vae.safetensors | Comfy-Org/Wan-2.2 (split_files) | 253,815,318 | 2fc39d31359a4b0a64f55876d8ff7fa8d780956ae2cb13463b0223e15148976b |

Total downloaded: 36,806,248,383 bytes (~36.8 GB). Free disk on /home: 145 GB before, 110 GB after.
Already on disk before the spike: no usable Wan weights (only a 536 KB metadata stub of Wan2.2-TI2V-5B in the HF cache). ComfyUI itself (AUR, v0.39.0 at /opt/comfyui) already ships the Wan nodes and core video nodes (CreateVideo/SaveVideo); no VideoHelperSuite needed. Note for future runs: in ComfyUI 0.39.0 the conditioning node is registered as `WanImageToVideo` (the old `Wan22ImageToVideo` name is rejected).

## 3. Render facts

- Source still: **img-cov-029** (seed2 coverage batch, admitted + manifested). Solo adult woman, completely nude, upper body, touching her own breasts; generated with Iris and **no LoRA** in its own generation record, so no SDXL gimmick for I2V to destroy. Native 832×1216; rendered at 544×800 (comparable pixel count to the 832×480 template default, native aspect kept).
- Workflow (saved as `workflow_lora.json` and `workflow_base.json` in the spike dir): LoadImage → WanImageToVideo conditioning (umt5 fp8 text encoder, wan_2.1 VAE) → high-noise fp8 model (+ NSFW-22-H LoRA @ 1.0) → ModelSamplingSD3 shift 5.0 → KSamplerAdvanced steps 0–10 → low-noise fp8 model (+ NSFW-22-L LoRA @ 1.0) → steps 10–20 → VAE decode → CreateVideo 16 fps → SaveVideo mp4/h264. 20 steps total, cfg 3.5, euler/simple — the ComfyUI Wan2.2 I2V template defaults, because the LoRA card states no settings beyond the trigger word. LoRA strength 1.0 both stages. Seed 42042 for both renders.
- Motion prompt (verbatim, both renders): "nsfwsks, a nude anime woman with long black hair and large breasts sits facing the camera, she slowly rubs and squeezes her own breasts with both hands in a steady rhythm, fingers kneading, she breathes deeply, chest heaving, blushing, mouth slightly open, hair swaying gently, smooth continuous motion, high quality"
- LoRA render: **771 s** wall on the RTX A6000 (GPU1). Output `img-cov-029_wan22_lora_00001_.mp4`: 544×800, 81 frames, 16 fps, 5.06 s, 1,766,258 bytes.
- Control render (identical everything, LoRA nodes removed): **760 s**. Output `img-cov-029_wan22_base_00001_.mp4`: same format facts, 1,503,433 bytes.
- GPU note: ComfyUI's RAM-pressure offloading was active; observed GPU1 total during sampling was ~28.4 GB including rose's ~19.3 GB residency. Rose (127.0.0.1:11434) was never touched and verified responding before and after; ComfyUI was started for this spike and stopped afterward.

## 4. Quality notes (paired comparison, frame-checked at 1.2 s / 2.5 s / 4.9 s; frames in `frames-lora/`, `frames-base/`)

- **Identity and style preservation: strong in both clips.** Face, eyes, hair, cel shading and the purple palette hold for the full 5 s; the character never melts or swaps.
- **Motion coherence:** the LoRA clip performs the prompted action — both hands kneading/squeezing with visible breast deformation — continuously through roughly the first 60% of the clip. The base clip starts similarly (the still is already posed for it and the prompt is explicit) but decays earlier into near-static posing.
- **Register:** the LoRA clip holds the aroused register (blush, parted lips) to the end. The base clip drifts off-prompt into a pleasant closed smile and camera engagement by 5 s.
- **Shared failure modes (LoRA does not fix these):** finger melding is visible in both clips by ~1 s; in both, the hands eventually ball into fists and drift off-target (LoRA clip at ~4.9 s, base earlier). No camera motion in either. End-of-clip action dissolution is the main quality ceiling at 81 frames.
- **Is the LoRA's effect visible?** Yes, but as an amplifier/register-keeper, not a capability unlock — on frontal solo self-touch content the base model already follows an explicit motion prompt. n=1 still, one motion class; a partner/interaction still would likely separate them further, and is the obvious next probe if this lane proceeds.

## 5. If the license blocks publish use, what would a from-scratch reproduction of the EFFECT take?

### 5.1 LoRA internals (observable facts, header-only reads)

- Files: `NSFW-22-H-e8.safetensors` (high-noise stage) and `NSFW-22-L-e8.safetensors` (low-noise stage) — a matched pair, one per Wan2.2 MoE stage; on Civitai these are versions "2.2 HIGH v0.08a" / "2.2 LOW v0.08a", and the `e8` suffix is an epoch-8 export.
- Structure (identical in both files): 800 tensors = 400 LoRA pairs, BF16. **Rank 64 uniformly**, and **no alpha keys** (scale carried by training convention). All **40 transformer blocks** are targeted, and the targeting is full-network, not attention-only: per block, self_attn {q,k,v,o}, cross_attn {q,k,v,o}, and ffn {0,2} — 10 modules × 40 blocks.
- Key naming (`diffusion_model.blocks.N.cross_attn.k.lora_A.weight`, …) is the musubi-tuner / ai-toolkit export convention for Wan.
- Metadata: the safetensors `__metadata__` contains **only** `{"format": "pt"}`. There are no kohya/musubi `ss_*` fields — no dataset name, resolution, learning rate, or epoch count recorded in the file. Training class is inferable (full-network rank-64 video LoRA, two stage-specific exports, ≥8 epochs from the filename), exact hyperparameters are not recoverable from the artifact.

### 5.2 Behavioral spec of the effect (from the paired renders in §4)

A trainer reproducing this effect is targeting these observable behaviors, relative to base Wan2.2 I2V given the same still, prompt, and seed:

1. **Sustained contact motion:** prompted self-touch/interaction motion persists at working amplitude for the majority of an 81-frame clip instead of decaying into idle sway after ~2 s.
2. **Soft-tissue response:** breasts deform visibly under hand pressure during contact motion (squeeze/knead reads as pressure, not sliding).
3. **Arousal register retention:** facial affect stays in the prompted aroused register (blush, parted lips, unfocused gaze) for the full clip; no drift to neutral smiling or camera posing.
4. **Motion amplitude:** overall body/hand travel is larger than base at identical settings, without identity loss.
5. Explicitly **not** part of the effect: hand/finger fidelity, new anatomy, camera moves, partner introduction. The reference LoRA provides none of these.

Application contract: trigger token `nsfwsks` in the prompt; paired LoRAs, H on the high-noise model and L on the low-noise model, each at strength 1.0, 20-step 10/10 split, cfg ~3.5.

### 5.3 Reproduction route — train our own

- **Tooling:** musubi-tuner (native Wan2.2 support, fp8 + block-swap training fits a rank-64 full-network LoRA into the A6000's 46 GB alongside nothing else running heavy) is the primary candidate; ai-toolkit is the alternative. Train two exports — high-noise and low-noise stage — exactly as the reference is structured, with timestep-window sampling per stage.
- **Data:** the effect class (§5.2) is a *motion prior*, trained from video clips, not stills. General video LoRAs of this class are typically trained on a few hundred to ~2,000 short captioned clips. Our clean supply: animate admitted corpus stills with the **base** Wan2.2 (Apache 2.0; licensor claims no rights over generated contents) using explicit motion prompts, then curate ruthlessly for the §5.2 behaviors — a few hundred keeper clips (81 frames, ~544×800) is a realistic first corpus, and our stills library makes source frames effectively unlimited. Caption with the motion description plus a trigger token of our own.
- **Compute:** rank-64 full-network on 14B fp8 at 81 frames is the heavy end of LoRA training; planning figure is several hours per stage per epoch-set on one A6000 — an overnight window per stage, not a lunch break. The reference artifact represents ≥8 epochs × 2 stages of somebody else's compute; expect the same order for ours.
- **The discipline that makes it clean:** train toward the §5.2 behavioral spec from our own data only. **Never** train on clips generated with lopi999's LoRA in the loop — that would distill the restricted artifact's behavior into a derivative of it. Base-model outputs and self-generated/licensed footage only; the restricted file's role ends at evidence (this report).
- **Why not just fine-tune their file:** Civitai's flags allow derivatives, but (a) the HF artifact we hold carries no license grant at all, and (b) the RentCivit-only commercial cap would still hang over anything derived from it. From-scratch on the Apache-2.0 base is the only route whose outputs are unambiguously ours.

## 6. Publish-tier recommendation

**BLOCKED-BY-LICENSE.** The pipeline works end-to-end on our hardware today and quality is usable-with-caveats (hand fidelity, end-of-clip drift), but the LoRA cannot lawfully feed publish-tier output: no license on the HF artifact, and RentCivit-only commercial use at the canonical source. Internal/experimental use stands. The publish path for this lane is §5.3: our own rank-64 H/L pair trained on base-model-generated clips from our own corpus stills — the base model, the stills, the prompts, and the resulting weights would all be ours.
