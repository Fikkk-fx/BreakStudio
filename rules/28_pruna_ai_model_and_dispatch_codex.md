# ⚡ DIRECTOR O.S. V20.5 — MODULE 28: PRUNA AI MODEL & DISPATCH CODEX
========================================================================================================
MASTER DIRECTORIAL SPECIFICATION FOR PRUNA AI IMAGE & VIDEO GENERATION ENGINES (SSOT)
========================================================================================================

Welcome to **Module 28 (Pruna AI Model & Dispatch Codex)**.
This module serves as the **Single Source of Truth (SSOT)** for orchestrating, parameterizing, and dispatching generations to the **Pruna AI** ecosystem within Director O.S. V20.5 (Raw UGC & Social Mobile Studio Edition).

---

## 🌐 SECTION I: PRUNA AI ARCHITECTURAL OVERVIEW

Pruna AI provides ultra-low latency, cost-effective inference endpoints for next-generation image and video foundation models.

### 🔑 Authentication & Base Configuration:
- **Base URL:** `https://api.pruna.ai/v1`
- **Authentication:** `apikey: <PRUNA_AI_API_KEY>` header.
- **Local Key Storage:** Managed in `.env` (`PRUNA_AI_API_KEY=pru_...`) or environment variable.
- **Workflow Modes:**
  1. **Synchronous Mode:** Header `Try-Sync: true` (waits up to 60s for immediate payload return).
  2. **Asynchronous Mode:** Default. Returns prediction ID and `get_url`. Status polled via `GET https://api.pruna.ai/v1/predictions/status/<id>`.
  3. **File Management:** `POST https://api.pruna.ai/v1/files` (multipart form `content=@<file>`) returns canonical cloud URI for conditioning.

---

## 🤖 SECTION II: THE 6 SUPPORTED PRUNA AI ENGINES

Director O.S. V20.5 natively binds to 6 specialized Pruna AI models across pre-production and final rendering:

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                PRUNA AI MODEL MATRIX FOR UGC PRODUCTION                                │
├────────────────────┬───────────┬───────────────────────────────┬───────────────────────────────────────┤
│ MODEL IDENTIFIER   │ DOMAIN    │ RESOLUTION & ASPECT RATIO     │ CORE CAPABILITY & UGC USE CASE        │
├────────────────────┼───────────┼───────────────────────────────┼───────────────────────────────────────┤
│ p-image-ideogram   │ Image     │ 1K / 2K | 9:16, 1:1, custom   │ Typography, CharSheets & Clean Text   │
│ flux-dev           │ Image     │ Up to 1024px+ | 9:16, 1:1     │ Photorealistic Street & Props         │
│ flux-dev-lora      │ Image     │ 1MP / 0.25MP | 9:16, 1:1      │ LoRA Styles, Face & Brand Consistency │
│ p-video-2-pro      │ Video     │ 480p / 768p (24fps) | 9:16    │ Omni-Conditioned Video + Auto Audio   │
│ p-video-2          │ Video     │ 720p / 1080p (24/48fps)| 9:16 │ Audio-Driven Sync, Extended Duration  │
│ p-video-edit       │ Video Edit│ Source Resolution | Up to 15s │ UGC Re-skinning & Video Modifications │
└────────────────────┴───────────┴───────────────────────────────┴───────────────────────────────────────┘
```

---

## 📸 SECTION III: IMAGE GENERATION ENGINES (TURN 4a GATEWAY)

In **Turn 4a**, the AI Director generates visual reference assets:
- **CharSheet (4-Panel Raw Character Sheet):** Panel 1 Front Torso/Outfit, Panel 2 Back, Panel 3 Face Normal, Panel 4 Open Mouth Teeth.
- **EnvSheet (Empty Architectural Lived-In Set):** 0% human silhouettes.
- **PropSheet (Tactile Handheld Props):** Micro-textures, real-world patina.

### 1. `p-image-ideogram` (Typography & Structural Asset Engine)
Ideal for character sheets requiring exact label rendering, posters, smartphone screens, and graphic overlays.
- **Endpoint:** `POST https://api.pruna.ai/v1/predictions`
- **Header:** `Model: p-image-ideogram`
- **Key Parameters:**
  - `prompt` (*string, required*): Detailed asset prompt.
  - `thinking` (*string, default: "high"*): Reasoning effort — `"very low"`, `"low"`, `"medium"`, `"high"`, `"very high"`.
  - `image_size` (*string, default: "1K"*): `"1K"` or `"2K"`.
  - `aspect_ratio` (*string, default: "1:1"* for CharSheets, `"9:16"` for Mobile UGC).
  - `prompt_upsampling` (*boolean, default: true*).
  - `output_format` (*string, default: "jpg"*): `"jpg"`, `"png"`, or `"webp"`.

### 2. `flux-dev` (Photorealistic Biological & Texture Engine)
Ideal for hyper-realistic skin pores, greasy smartphone CMOS halation, and natural ambient lighting.
- **Header:** `Model: flux-dev`
- **Key Parameters:**
  - `prompt` (*string, required*): Photorealistic prose with optical and environmental specifications.
  - `speed_mode` (*string*): `"Juiced 🔥 (default)"`, `"Extra Juiced 🔥 (more speed)"`, `"Lightly Juiced 🍊"`, `"Blink of an eye 👁️"`.
  - `num_inference_steps` (*integer, default: 28*).
  - `guidance` (*number, default: 3.5*).
  - `aspect_ratio` (*string, default: "9:16"* or `"1:1"`).

### 3. `flux-dev-lora` (Character & Stylistic Lock Engine)
Enables persistent identity and bespoke creator aesthetics using HuggingFace LoRAs.
- **Header:** `Model: flux-dev-lora`
- **Key Parameters:**
  - `lora` (*string*): HuggingFace LoRA repository identifier (e.g., `"owner/lora-name"`).
  - `lora_scale` (*number, default: 1.0*): Strength multiplier (-1 to 3).
  - `extra_lora` (*string, optional*): Secondary LoRA repository.
  - `image` (*string URI, optional*): Reference image URI for image-to-image workflows.
  - `prompt_strength` (*number, default: 0.8*): Transformation strength (0.0 to 1.0).

---

## 🎥 SECTION IV: VIDEO GENERATION ENGINES (TURN 6 DIRECT DISPATCH)

In **Turn 6**, the AI Director dispatches final Master UGC Video Prompts.

### 1. `p-video-2-pro` (Flagship Directorial Video Engine)
Provides cinematic and raw mobile motion coherence with first/last frame locking and synchronized AI-generated audio.
- **Header:** `Model: p-video-2-pro`
- **Key Parameters:**
  - `prompt` (*string, required*): Master UGC Video Prompt (Layer 1 to Layer 6 or 4-Block format).
  - `image` (*string URI, optional*): First-frame anchor (typically generated from Turn 4a).
  - `last_frame_image` (*string URI, optional*): Tail-frame anchor for seamless cut-to-cut transitions.
  - `duration` (*integer, 5–15s, default: 5*): Exact temporal length.
  - `resolution` (*string, default: "768p"*): `"480p"` or `"768p"`.
  - `mode` (*string, default: "speed"*):
    - `"speed"`: Fast generation turnaround.
    - `"quality"`: Maximum optical and temporal coherence.
    - `"cost"`: Budget-optimized rendering.
  - `prompt_upsampler` (*string, default: "turbo"*): `"off"`, `"turbo"`, or `"max"`.
  - `aspect_ratio` (*string, default: "9:16"* for TikTok/Reels/Shorts).

### 2. `p-video-2` (Audio-Conditioned & Extended Duration Engine)
Supports external audio conditioning (e.g. voiceover, podcasts, street interview clips) and resolutions up to 1080p.
- **Header:** `Model: p-video-2`
- **Key Parameters:**
  - `prompt` (*string, required*).
  - `duration` (*integer, 1–20s*): Leave empty when audio is provided to match audio length.
  - `image` (*string URI, optional*): Input image for image-to-video.
  - `audio` (*string URI, optional*): Input audio file (WAV, MP3, FLAC) to condition timing and lipsync.
  - `resolution` (*string, default: "720p"*): `"720p"` or `"1080p"`.
  - `fps` (*integer, default: 24*): `24` or `48`.
  - `aspect_ratio` (*string, default: "9:16"*).
  - `draft` (*boolean, default: false*): Half-price preview mode.
  - `disable_safety_filter` (*boolean, default: true*): Prevents false positive filters on raw street footage.

### 3. `p-video-edit` (UGC Video Retexturing & Modification Engine)
Edits an existing video (up to 15s) guided by prompts and optional reference images.
- **Header:** `Model: p-video-edit`
- **Key Parameters:**
  - `video` (*string URI, required*): Source video URI.
  - `prompt` (*string, required*): Editing instructions (e.g. background replacement, wardrobe switch).
  - `images` (*array of URIs, up to 4*): Reference image guidance.
  - `draft` (*boolean, default: false*).
  - `save_audio` (*boolean, default: true*).

---

## 🛠️ SECTION V: CLI DISPATCH WORKFLOW (`pruna_client.py`)

The local tool `pruna_client.py` automates asset upload, prediction dispatch, polling, and local file saving.

### 1. Uploading Assets:
```bash
python pruna_client.py upload --file assets/character_sheet.jpg
# Output: [SUCCESS] Uploaded: https://api.pruna.ai/v1/files/abc123...
```

### 2. Turn 4a Image Generation:
```bash
# Generate 9:16 CharSheet / Poster via Ideogram:
python pruna_client.py image \
  --model p-image-ideogram \
  --prompt "4-Panel Raw Character Sheet of Indonesian male street food barista, plain white background, 9:16" \
  --thinking high \
  --aspect-ratio 9:16 \
  --output assets/charsheet_ideogram.jpg

# Generate Photorealistic Environmental Plate via Flux Dev:
python pruna_client.py image \
  --model flux-dev \
  --prompt "Empty warung kopi interior in Jakarta, morning sunlight streaming through window, smartphone CMOS 24mm f/1.7, 9:16" \
  --speed-mode "Juiced 🔥 (default)" \
  --aspect-ratio 9:16 \
  --output assets/env_warung.jpg
```

### 3. Turn 6 Video Generation:
```bash
# High-Motion UGC Clip via p-video-2-pro:
python pruna_client.py video \
  --model p-video-2-pro \
  --prompt "Raw handheld smartphone footage. A charismatic Indonesian street vendor laughs while pouring iced tea into a plastic cup. Natural camera micro-shake, warm morning sunlight." \
  --image assets/charsheet_ideogram.jpg \
  --duration 5 \
  --resolution 768p \
  --mode speed \
  --aspect-ratio 9:16 \
  --output outputs/clip_01.mp4

# Audio-Conditioned Video via p-video-2:
python pruna_client.py video \
  --model p-video-2 \
  --prompt "Young woman talking excitedly to the camera in her bedroom, natural 80/20 screen-look drift." \
  --audio voiceovers/audio_clip.mp3 \
  --resolution 1080p \
  --aspect-ratio 9:16 \
  --output outputs/clip_02.mp4
```

### 4. Video Editing:
```bash
python pruna_client.py edit-video \
  --video outputs/raw_interview.mp4 \
  --prompt "Change the lighting to golden hour sunset with soft lens flare" \
  --output outputs/interview_golden_hour.mp4
```

---

## 🛡️ SECTION VI: HARDWARE LOCKS & ZERO-DEFECT PRUNA INTEGRATION

1. **Aspect Ratio Hardware Lock:** Mobile native UGC MUST strictly request `--aspect-ratio 9:16`. Do NOT default to 16:9 for TikTok/Reels/Shorts.
2. **Local-to-Cloud Auto Handoff:** `pruna_client.py` automatically detects if `--image`, `--audio`, or `--video` is a local file path, uploads it via `/v1/files`, and transparently passes the resulting cloud URI.
3. **Draft Mode Policy:** Always use `--draft` or mode `cost`/`speed` during rapid storyboarding and prototyping; reserve `resolution 1080p` and mode `quality` for final locked cuts.
