---
name: speech-dialogue-spec-and-line-split-codex
description: "Prose dialogue inlining SSOT, acoustic delivery specifications, Indonesian e-taling diacritics, TTS line-split dynamic tempo control, and persona voice locks."
---

# 🎙️ 20. SPEECH DIALOGUE SPEC & LINE-SPLIT CODEX

## §PROSE-DIALOGUE — PROSE INLINING AS SINGLE SOURCE OF TRUTH (SSOT)
In video prompt generation, spoken dialogue must NEVER be isolated into a detached script block. Spoken dialogue is **FUSED DIRECTLY INTO PROSE ACTIONS** in Block 1 / Block 3 using natural speaking verbs and strict double-quote fencing:

```text
At [X.Xs] [physical action prose], [Character] [speaking verb] "[exact spoken words with direct diacritics]"
```

### 🔒 THE 4 LAWS OF PROSE INLINING:
1. **QUOTES FENCE VOICED WORDS:** Only text enclosed in double quotes (`"..."`) is voiced by the multi-modal audio DiT model (such as MiniMax Hailuo H3 or Sora). Everything outside quotes is physical acting.
2. **VERBS CARRY SUBTEXT & TONE:** Descriptive speaking verbs (*whispers, gasps, snarls, stammers, mutters*) convey performance tone naturally without injecting artificial bracketed labels that TTS engines might accidentally read aloud (#123).
3. **NO DETACHED "DIALOG:" LABELS:** Forbid prefixes like `Dialogue: "..."` inside prose, as legacy models frequently read the word *"Dialogue"* aloud.
4. **DIRECT DIACRITIC ANCHORING (Mandate 13):** Indonesian *e-taling* words are written directly with acute accents (`é`) inside quotes (e.g. `"Adél... bésok kuncinya harus berés!"`). 0% phonetic bracket clutter in prose.

---

## §O — ACOUSTIC DELIVERY SPECIFICATION (BLOCK 7 / SOUND SPEC)
Block 7 serves as the **Acoustic Mastering & Voice Delivery Specification**, NOT a redundant duplicate script:
- **0% DOUBLE-SPEAK (#123):** Block 7 references spoken lines by their **EXACT TIMESTAMPS**, never re-quoting full sentences.
- **DELIVERY SPEC SYNTAX (§O-DIA):**
  ```text
  At [X.Xs] [LANGUAGE-REGION DIALECT, NATIVE-FLUENT, CADENCE/SUBTEXT, PITCH Hz, SPEECH RATE wps]
  ```

**Examples:**
- *Indonesian:* `At 04.2s [Bahasa Indonesia, Logat Jakarta, Native Fluent, Bisikan Panik Menekan, 140Hz, 1.8 wps]`
- *English:* `At 02.1s [English, London RP, Native Fluent, Cold Restrained Command, 110Hz, 1.4 wps]`

---

## §O-FLOW — LINE-SPLIT DYNAMIC TEMPO CONTROL (ANTI-MONOTONE LAW)
Modern Text-to-Speech (TTS) and DiT audio models cannot smoothly modulate tempo *within* a single continuous sentence (asking for *"start slow... then suddenly speak fast... then slow down"* causes the engine to flatten the entire line into a robotic monotone average).

### ⚡ THE LINE-SPLIT TEMPO PROTOCOL:
To create realistic emotional tempo shifts, **SPLIT THE UTTERANCE INTO 2–3 SEPARATELY TAGGED LINES**:
```text
At 03.0s [Cepat, Menekan, Napas Pendek, 1.9 wps] "Kita harus keluar sekarang—"
At 05.2s [Melambat Berat, Hampir Berbisik, 1.1 wps] "...sebelum gerbangnya terkunci."
```
- Trailing em-dashes (`—`) and leading ellipses (`...`) act as natural acoustic seams, allowing the audio engine to pause and reset vocal pitch realistically.

---

## §O-PHON — PHONETIC GLOSSING (INLINE ACOUSTIC CLARITY)
For difficult proper nouns, acronyms, or loan words:
- **Indonesian Pepet vs Taling:** `"sêdan"`, `"bêda"`, `"kéréta"`.
- **English Stress & Homographs:** `"record[REK-ord]"` (noun) vs `"record[re-KORD]"` (verb); `"tear[TEER]"` (drop) vs `"tear[TARE]"` (rip).
- **Spoken Numbers:** Numbers are written in full words (`"dua ribu dua puluh empat"`, `"twenty twenty-four"`) to prevent TTS digit-by-digit reading.

---

## PERSONA VOICE LOCK — NUMERIC ACOUSTIC PASSPORT
Every speaking character possesses a persistent voice passport in their character specification that is copied identically across all clips:
```text
PERSONA VOICE LOCK:
- Silas: Low-frequency resonant baritone (105Hz–115Hz), British Received Pronunciation (RP), measured cadence (1.3 wps), sharp dry glottal stops.
- Maya: Mid-tone athletic alto (160Hz–175Hz), Bahasa Indonesia Logat Baku Jakarta, dynamic breath-driven cadence (1.7 wps), subtle vocal fry on sentence endings.
```
- **NUMBERS OR IT DRIFTS:** Vague adjectives (*"deep voice"*, *"raspy"*) drift between clips. Specifying fundamental frequency ($\Delta F_0 \ge 50\text{Hz}$) and words-per-second locks vocal identity permanently across multi-clip productions (#24).

---

## §VO-WPS — VOICEOVER (VO) WPS MATHEMATICAL CALCULATION & SYNCHRONIZATION PROTOCOL

Whenever a scene or shot incorporates **Voiceover (VO)**, **Narration**, or **Internal Monologue**:

### 1. 🧮 THE MATHEMATICAL WPS FORMULA:
$$\text{WPS} = \frac{\text{Word Count}}{\Delta t} = \frac{\text{Jumlah Kata Eksak Di Dalam Kutip}}{\text{Waktu Selesai (s)} - \text{Waktu Mulai (s)}}$$

- **Word Count ($N$):** Count every single spoken word inside quotes.
- **Duration Window ($\Delta t$):** The exact allocated seconds for the voiceover burst (`End.s - Start.s`).
- **WPS Declaration Tag:** The resulting WPS must be stated directly in the VO prompt tag:
  ```text
  [VO: [Speaker] — Off-Screen / Non-Diegetic | Start.s–End.s (Duration: X.Xs) | Word Count: N words | Speech Rate: X.X WPS (Target Sync: 1.7–2.0 WPS, Synchronized)]:
  "[Verbatim voiceover line with 'é' diacritics]"
  ```

### 2. ⚖️ CALIBRATED SPEED REGIMES (NEITHER TOO FAST NOR TOO SLOW):
| Regime | Target WPS Envelope | Emotional / Narrative Context | Pacing Risk if Violated |
| :--- | :--- | :--- | :--- |
| 🧘‍♂️ **Contemplative / Somatic** | **1.3 – 1.6 WPS** | Philosophical reflections, grief/trauma, elegiac sorrow, atmospheric dread | $< 1.3$ WPS: Unnaturally dragging, lethargic dead air, clip overrun |
| 🚶‍♂️ **Cinematic Baseline (SSOT)** | **1.7 – 2.0 WPS** | Standard storytelling, documentary narration, brand manifestos | **Optimal Sweet Spot:** Pristine organic human cadence & clear syllables |
| 🏃‍♂️ **Urgent Hook / Trailer** | **2.1 – 2.4 WPS** | High-energy trailers, viral hook lines, fast tactical exposition | $> 2.4$ WPS: Rushed gibberish, clipped phonemes, chipmunk artifact, desync |

### 3. 🔒 THE 4 ANTI-DESYNC LAWS FOR VO:
1. **LIP-SYNC ISOLATION LAW (0% False Mouth Flapping):** When VO is heard while a character is on screen, the prompt MUST declare: `[Lips remaining closed in neutral repose, 0% mouth moving for VO, natural breathing and focused gaze]`. Multi-modal diffusion models will hallucinate erroneous mouth flapping unless explicitly commanded to keep lips shut during VO.
2. **SHOT-BOUNDARY ENCLOSURE (Mandate 1 & 23):** Like on-screen dialogue, VO speech windows must conclude at least **0.2s before a hard cut** (`VO End Time <= Cut Timestamp - 0.2s`) to prevent audio bleeding across shot transitions.
3. **0.8s TAIL-BUFFER INTEGRITY:** All voiceover narration in the final shot must conclude at `Total Duration - 0.8s`, leaving the final 0.8s clean for natural vocal decay and room tone.
4. **ACOUSTIC DUCKING SYNCHRONIZATION:** In the Audio Block, the soundscape/foley must explicitly duck by **-4dB to -6dB at 2.5kHz** synchronized precisely to the VO speech window `[Start.s–End.s]`.
