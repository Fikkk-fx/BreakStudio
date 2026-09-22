# 🚀 DIRECTOR O.S. V20.5 — MODULE 01K: MINIMAX H3 (HAILUO 3.0) OMNI-MODAL ARCHITECTURE & EXECUTION CODEX
========================================================================================================
MINIMAX H3 (HAILUO 3.0 / HAILUO-03) OMNI-MODAL FOUNDATION & DUAL-BRANCH DIRECTORIAL SPECIFICATION (SSOT)
========================================================================================================

Welcome to **Module 01K (MiniMax H3 Omni-Modal Architecture & Execution Codex)**. This module establishes the exact byte-level prompt formatting, multi-modal reference binding, canonical dialogue tagging syntax, and hardware parameter mapping for the **MiniMax H3** (Hailuo 3.0) foundation model.

---

## 🏛️ 1. ARCHITECTURE & OMNI-MODAL FOUNDATION OVERVIEW

MiniMax H3 is a next-generation open-weight multimodal generative AI model built on a **Joint Audio-Video Diffusion Transformer (DiT)**. Unlike disjointed multi-pipeline architectures (which generate video first and bolt on separate TTS or Foley vocoders), MiniMax H3 synthesizes spatial pixels, temporal kinematics, and native 32 kHz stereo acoustics inside a **single unified context window**.

### Key Technical Benchmarks:
* **Video Output:** 768P & 2K resolution at 24 FPS (cinematic motion smoothness).
* **Clip Duration:** 4s to 15s per generation pass.
* **Native Stereo Audio:** 32 kHz high-fidelity stereo audio natively generated with zero-latency lip-sync, room acoustic reverb (RT60), and synchronized tactile Foley.
* **Multilingual Speech:** Native phoneme articulation across 11 major languages (English, Mandarin, Japanese, Korean, Indonesian, Spanish, French, German, Arabic, etc.).
* **Multi-Modal Context Limit:** Accepts up to 12 reference files simultaneously (up to 9 images, 3 videos, and 3 audio clips).

---

## 🔀 2. THE DUAL-BRANCH GENERATION MATRIX: FL2VA VS REF2VA

MiniMax H3 operates strictly through two dedicated checkpoint branches. Prompts MUST be tailored to the active branch:

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   MINIMAX H3 DUAL BRANCHES                                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. FL2VA (Frame-Led-to-Video-Audio):                                                                 │
│    ├── 0 Images : Standard Text-to-Video (T2V)                                                       │
│    ├── 1 Image  : Image-to-Video (I2V) anchoring Start Frame or End Frame                                │
│    └── 2 Images : First-and-Last-Frame Interpolation (Deterministic State A ──► State B transition)    │
│                                                                                                      │
│ 2. Ref2VA (Reference-to-Video-Audio):                                                                │
│    └── Multi-Asset Reference Conditioning:                                                           │
│        ├── Character Consistency (Face, Hairstyle, Skin Tone, Physique)                              │
│        ├── Wardrobe & Prop Parity (Costumes, Weapons, Apparatuses)                                   │
│        ├── Environmental Architecture & Lighting Style                                               │
│        └── Motion Transfer & Voice Character Audio Conditioning                                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### ⛔ Strict Branch Anti-Contamination Rules:
1. **Ref2VA Clean Start Law:** In Ref2VA mode, **NEVER** include frame-alignment lines or start-frame anchor statements at the beginning of the prompt. Start directly with `[Scene]` architecture and semantic character descriptions.
2. **Audio Reference Requirement:** Audio cannot be provided as the sole reference input. An audio reference clip MUST always be paired with at least 1 image or video asset.

---

## 📝 3. CANONICAL PROMPT STRUCTURE (MINIMAX H3 STANDARD)

MiniMax H3 adheres to a structured, 4-block modular format:

```text
[Scene]: [Subject / Characters] inside [Environment / Architecture] under [Lighting Vector & Atmospheric Depth].
[Timeline]: [0s-X s: Initial Action & Somatic Setup] -> [Xs-Y s: Escalation, Kinetic Interaction & Cuts] -> [Ys-Duration: Climax / Momentum Handover].
[Camera]: [Focal Length in mm] [Shot Framing] with [Camera Rig Motion, Speed, and Angle].
[Audio]: [Synchronized Diegetic Foley & Mechanical Sounds]; [Room Acoustics, Reverb & Acoustic Decay].
```

---

## 🎙️ 4. CHARACTER ID & DIALOGUE SYNTAX CODEX (`<d>` TAGGING)

To achieve 100% stable speaker assignment and authentic lip-sync in MiniMax H3:

### A. Syntax Rule:
* Every active speaker MUST be assigned a unique numeric identifier: `(S1)`, `(S2)`, `(S3)`.
* Dialogue MUST be enclosed inside the canonical `<d>[Language] "..."</d>` markup with emotional and delivery cues:

```text
(S1) [Emotional Delivery / Vocal Cadence] says: <d>[Language] "Spoken text (1-7 words max)"</d>
```

### B. Standard Multi-Speaker Tactical Relay Example:
```text
(S1) [Urgent, authoritative command] says: <d>[Indonesian] "Tutup pintu darurat sekarang!"</d>
(S2) [Trembling voice, heavy breathing] says: <d>[Indonesian] "Kuncinya patah di dalam!"</d>
```

### C. Director O.S. Dynamic Word Budget Integration:
* Spoken dialogue strictly respects **Mandate 5** (1 to 7 words maximum per burst).
* Spoken dialogue concludes $\ge 0.2\text{s}$ before any motivated inline cut (`[HARD CUT]`).

---

## 📦 5. ATLAS CLOUD & API PARAMETER MAPPING SPECIFICATIONS

When dispatching generation requests to Atlas Cloud API (`/api/v1/model/generateVideo`) or local ComfyUI wrappers:

```json
{
  "model": "minimax/h3/reference-to-video",
  "prompt": "[Scene]: ... [Timeline]: ... [Camera]: ... [Audio]: ...",
  "ratio": "16:9",
  "resolution": "2K",
  "duration": 15,
  "refers": [
    {
      "url": "https://cdn.atlascloud.ai/char1_base_ugc.png",
      "type": "image"
    },
    {
      "url": "https://cdn.atlascloud.ai/char1_stateB_damage.png",
      "type": "image"
    },
    {
      "url": "https://cdn.atlascloud.ai/env_auditorium.png",
      "type": "image"
    }
  ]
}
```

### Parameter Mapping Standards:
* **Model Keys:**
  * `minimax/h3/reference-to-video` (Ref2VA mode)
  * `minimax/h3/image-to-video` (FL2VA 1-frame or 2-frame mode)
  * `minimax/h3/text-to-video` (FL2VA 0-frame mode)
* **Aspect Ratio:** Stored in key `"ratio"` (Values: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`).
* **Resolution:** `"768P"` or `"2K"` (Auto-mapped from `720p` $\to$ `768P`, `1080p`/`2k` $\to$ `2K`).
* **Duration:** Integer value between `4` and `15` seconds (e.g. `5`, `10`, `15`).
* **References (`refers`):** Array of objects containing `"url"` and `"type"` (`"image"`, `"video"`, or `"audio"`).

---

## ⚡ 6. CROSS-MODEL COMPATIBILITY MATRIX

| Feature / Task | ByteDance Seedance 2.5 Pro | MiniMax H3 (Hailuo 3.0) | Kling V3.0 Pro | Wan 2.7 Pro |
| :--- | :--- | :--- | :--- | :--- |
| **Max Multi-References** | Up to 50 assets | Up to 12 assets (9 img, 3 vid, 3 aud) | 2 assets (Start + End) | Up to 10 images |
| **Native Audio DiT** | ✅ Yes (Volcano Engine) | ✅ Yes (Joint DiT 32kHz) | ✅ Yes (`sound: true`) | ❌ No (Video only) |
| **Dialogue Tag Format** | `[Name speaking in Language: "..."]` | `(S1) [Delivery] says: <d>[Lang] "..."</d>` | Inline natural text | N/A |
| **First/Last Frame Transition**| Supported | Supported (FL2VA 2-frame) | Supported | Supported |
| **Max Duration Single Pass** | 15s | 15s | 10s | 10s |
| **Open Weights Available** | ❌ Proprietary API | ✅ Open-Weight & GGUF | ❌ Proprietary API | ✅ Open-Weight |
