---
name: 05-audio-and-dialogue
description: "Fluent Lip-Sync Anchors, Cinematic Scoring, -4dB Vocal Ducking @ 2.5kHz, Room Impulse Response (RIR), and 0.8s Acoustic Tail-Buffer."
---

# 🎧 BREAKSTUDIO — MODULE 05: PURE DIEGETIC AUDIO, ACOUSTICS & ROOM IMPULSE RESPONSE
========================================================================================================
PURE DIEGETIC SOUNDSCAPES (STRICTLY 0% MUSIC / 0% BGM), SPATIAL RIR & HIGH-DENSITY FOLEY (V20.5)
========================================================================================================

This module governs **PURE DIEGETIC SOUND DESIGN, PHYSICAL ROOM ACOUSTICS & ATMOSPHERIC ROOM TONES**.
In BreakStudio, audio is high-fidelity cinema verite — **STRICTLY 0% ARTIFICIAL BACKGROUND MUSIC, 0% ORCHESTRA, 0% SYNTH/CELLO BGM**.

---

## 🚫 SECTION I: THE PURE DIEGETIC AUDIO MANDATE (STRICTLY 0% MUSIC / BGM)

* **FORBIDDEN:** Non-diegetic background music, melodic orchestral scoring, emotional cello drones, or synthesized BGM tracks.
* **MANDATE:** Every acoustic sound in Block `[AUDIO]` must have an authentic physical diegetic source inside the scene:
  1. Spoken vocal dialogue with intimate room presence.
  2. Tactile somatic foley (cloth rustle, footwear friction, object manipulation).
  3. Physical environmental acoustics (rain on glass, 60Hz electrical hum, wind buffeting, radiator hiss).
  4. Room Impulse Response (RIR) based on architectural wall materials.

---

## 🏛️ SECTION II: ROOM IMPULSE RESPONSE (RIR) & ACOUSTIC SPATIAL MODELING

Every environment in Block [AUDIO] must declare its exact physical reverberation characteristics:
* **Small Study / Tile Room:** RT60 0.45s–0.65s @ 500Hz with crisp near-wall reflections.
* **Concrete Basement / Wet Corridor:** RT60 1.2s–1.8s with metallic slap-back echo.
* **Vaulted Cathedral / Hangar:** RT60 2.2s–3.5s with majestic high-frequency diffusion.
* **Open Forest / Exterior Desert:** RT60 0.05s (dry acoustic decay with soft wind noise floor).

---

## 🔊 SECTION III: THE 3-TIER PURE DIEGETIC AUDIO CODEC

1. **Track 1 (Active Vocal Dialogue):** Mastered to **-14 LUFS**, pristine acoustic presence, natural throat resonance.
2. **Track 2 (Diegetic Somatic Foley):** Footsteps on floor, cloth rustle, key jingle, zippo click, furniture creak.
3. **Track 3 (Environmental Room Tone & Atmosphere):** 60Hz AC hum, fluorescent flicker drone, window rain patter, natural exterior airflow.

---

## 🔇 SECTION IV: THE PURE DIEGETIC REALISM & ZERO-SCORE AUDIO CODEX (0% BACKGROUND MUSIC)

When projects demand raw hyper-realism, visceral horror tension, documentary vérité, or when user requests **ZERO BACKGROUND MUSIC / SCORE**:

### 1. 🚫 STRICT ZERO NON-DIEGETIC MUSIC MANDATE:
* Strictly **0% background music, 0% orchestral strings, 0% synthesized pads, 0% non-diegetic drones**.
* The soundscape is driven 100% by **PHYSICAL DIEGETIC ACOUSTICS & SOMATIC PROXIMITY**.

### 2. 🏛️ THE 3-PILLAR DIEGETIC SOUND ARCHITECTURE:
1. **Pillar 1: Organic Room Impulse Response (RIR) & Noise Floor:**
   - Authentic room air pressure: subtle 60Hz electrical hum, wind draughts against windowpanes, radiator ticks, floorboard settling.
2. **Pillar 2: Hyper-Detailed Tactile Foley:**
   - Crisp, tactile sound effects: shoes gripping parquet/concrete, fingernails grazing wooden desk, cloth friction on skin, pen rolling with micro-vibrations, heavy door slam (SLAM!) with acoustic room decay.
3. **Pillar 3: Intimate Unmasked Vocal Presence:**
   - Unprocessed, intimate vocal clarity (-14 LUFS) capturing dry throat swallows, subtle breath intakes, trembling vocal cord micro-tremors, and quiet whispers without musical interference.

---

## 🎙️🎚️ 51. THE ORTHOGONAL 4-TIER VOCAL DIFFERENTIATION & FREQUENCY AIR-GAP CODEX (ANTI-HOMOGENEOUS VOICE LAW V20.5)

To permanently eliminate the defect where all characters in a scene or across multi-clip sequences sound like the same generic, monotone voice actor:

### 🌟 THE 4-TIER ORTHOGONAL VOCAL CONTRAST CODEX:

Every ensemble cast (2 to 8 characters) MUST be engineered with 4 distinct orthogonal acoustic air-gaps:

```text
╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                          THE 4-TIER ORTHOGONAL VOCAL CONTRAST MATRIX                                 ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ 🎚️ TIER 1: FUNDAMENTAL FREQUENCY (F0) AIR-GAP ($\Delta F_0 \ge 50$Hz):                                  ║
║    • Karakter A (Deep Pitch)  : Bass / Low Baritone (75Hz – 110Hz).                                  ║
║    • Karakter B (High Pitch)  : High Tenor / Contralto / Soprano (160Hz – 250Hz+).                   ║
║    • MANDAT: Strictly forbidden for 2 characters to share the exact same fundamental frequency (Hz) range!            ║
║                                                                                                      ║
║ 🌊 TIER 2: TIMBRE & VOCAL CORD TEXTURE POLARITY:                                                     ║
║    • Karakter A : Gravelly, Raspy, Vocal Fry, Dry Throat Friction (Parau/Serak Berat).               ║
║    • Karakter B : Resonant, Ringing Chest Resonance, Clear Melodic Formants (Bulat Jernih).          ║
║    • Karakter C : Breathy, Nasal Staccato, High-Tension Vocal Strain (Napas Tersengal/Sengau).       ║
║                                                                                                      ║
║ ⏱️ TIER 3: SPEECH TEMPO & CADENCE ASYMMETRY:                                                         ║
║    • Karakter A : Measured Stoic (1.2 – 1.5 wps / Tenang, berat, berwibawa, jeda panjang).          ║
║    • Karakter B : Rapid Staccato (2.0 – 2.4 wps / Cepat, reaktif, mendesak, meledak-ledak).          ║
║                                                                                                      ║
║ 🗣️ TIER 4: LINGUISTIC DIALECT & SOCIOLECT REGISTER:                                                  ║
║    • Karakter A : Formal Standard Indonesian with crisp consonants and dense articulation.           ║
║    • Karakter B : Bahasa Indonesia berlogat regional (Jawa Medok halus / Betawi / Batak lugas).      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

---

### 📝 CONTOH PENULISAN PROMPT BLOK 6 (SPATIAL ACOUSTICS & LIP-SYNC):
Saat mengarahkan dialog di Turn 5 Blok 1 dan Blok 6, AI WAJIB menyuntikkan kontras frekuensi dan timbre secara eksplisit:
* *Karakter A:* `[Bima speaking in a deep 85Hz gravelly baritone with slow measured 1.3wps Javanese-inflected cadence: "..."]`
* *Karakter B:* `[Surya responding in a bright 180Hz breathy tenor with rapid 2.2wps urgent delivery: "..."]`
* *Karakter C (Figuran):* `[Guard barking in a gruff 70Hz resonant chest bass: "..."]`

## 🗣️ SECTION VI: NON-NATIVE ACCENT & CROSS-LINGUISTIC PHONETICS
Foreign speakers must exhibit authentic cross-linguistic phonetic friction, non-native syllable stress, and native guttural/consonant transfer in Block [AUDIO] and [PROSE].

## 🗣️ SECTION VII: BLOCK 6 WORD-BY-WORD PHONETIC ARTICULATION GUIDE
In 7-Block Mode 3, Block 6 [AUDIO/ACOUSTICS] includes explicit word-level phonetic breakdowns for critical non-English terms to ensure precise canonical pronunciation.

## ⏱️ SECTION VIII: POLYMORPHIC DIALOGUE TEMPORAL DISTRIBUTION
Dialogue timestamp placement must dynamically rotate across early cold-opens, split bursts, late stingers, and pure tactical silence.

## 🗣️💨 SECTION IX: SUB-VERBAL, MUMBLES & PARALINGUISTIC ACOUSTICS
Dialogue delivery must systematically integrate rich human sub-verbal acoustics: under-the-breath grumbles, pain groans, scoffs, and trailing sighs.

## 🎙️🔤 SECTION X: EXHAUSTIVE WORD-BY-WORD PHONETIC TRANSCRIPTION MANDATE
In Block 6, every spoken word in dialogue must have an explicit word-by-word phonetic transcription and syllable breakdown.

## 🗣️🌍 SECTION X: MANDATORY CULTURAL DIALECT & REGISTER DECLARATION (ORGANIC CADENCE)
Always declare rich cultural dialect and register anchors in PROSE (e.g. `speaking in natural conversational Jakarta Indonesian: "..."`, `speaking in authentic Javanese-accented Indonesian: "..."`, `speaking in formal authoritative Indonesian: "..."`, `speaking in fluent British English: "..."`) without rigid bracketed time tags on speech to ensure 100% fluent, organic vocal cadence.


---

## 🎙️⚡ MANDATE 5: THE 7-WORD MAX-PER-BURST DYNAMIC CEILING (100% FLEXIBLE PLACEMENT & 1–7 WORDS)
* **(mmmm) The 7-Word Max-Per-Burst Dynamic Dialogue Law (100% Flexible Timing & 1–7 Words):** The 7-word rule is a **STRICT UPPER LIMIT (CEILING), NOT A RIGID QUOTA**. Characters are encouraged to speak organic, visceral utterances of any length from **1 to 7 words** (e.g. 1-word barking commands *"Tiarap!"*, 2-word alerts *"Maju sekarang!"*, 3-5 word tactical orders, up to a maximum of 7 words). Furthermore, dialogue placement is **100% DYNAMIC & MOTIVATED BY ACTION** across the timeline (0% rigid "beginning/middle/end" template) — bursts may appear at any timestamp where drama or physical conflict motivates speech (e.g. a single punchy command mid-clip, two rapid tactical exchanges during a breach, or late warnings before an explosion).

---

## 🎙️🔒 SECTION 14: THE 3-PILLAR IMMUTABLE CHARACTER VOCAL LOCK FOR MULTI-CLIP CONTINUITY

In multi-clip projects, character voices must NEVER randomly change tone, accent, or delivery style between Clip 1, Clip 2, Clip 3...
1. **Timbre Continuity:** A character established as a *gravelly raspy baritone* in Clip 1 CANNOT become a *smooth tenor* in Clip 2.
2. **Dialect Continuity:** Regional phonemes, vowel lengths, and accent idiosyncrasies remain 100% stable across all clips.
3. **Technique Continuity:** A character's speaking habits (clipped staccato vs unhurried cadence vs breathy panic) evolve only through motivated dramatic stakes, preserving core vocal identity.

---

## 🎚️ SECTION VII: MASTER ACOUSTIC HARDWARE & STUDIO MASTERING SPECIFICATIONS

To achieve professional broadcast and cinema-grade diegetic sound design without relying on fake synthetic BGM:
1. **Broadcast Mastering Target:**
   - Loudness: `-14 LUFS target integrated loudness`, `-1.0 dBFS true peak limiter ceiling`.
2. **Preamp Saturation & Resonance:**
   - Warmth & Body: `Neve 1073 preamp harmonic saturation`, `200Hz chest resonance warmth on primary dialogue`.
   - High-Frequency Clarity: `Clean transient response on glass shattering, blade scrapes, and footstep heel-clicks`.
3. **Diegetic Electrical Room Resonance:**
   - Ground scenes with real acoustic hum: `50Hz/60Hz AC electrical fluorescent fixture hum`, `subtle air HVAC room impulse response`, ensuring continuous room tone through final frame.

---

## 🎙️⚡ THE CONCURRENT ACTION-DIALOGUE FUSION LAW (SPEAKING WHILE ACTING)

> [!CAUTION]
> ### 🛑 TOP-PRIORITY DIRECTORIAL MANDATE: CHARACTERS MUST SPEAK CONCURRENTLY WHILE EXECUTING PHYSICAL ACTIONS!
> **NEVER PAUSE OR FREEZE PHYSICAL ACTIONS TO DELIVER SPOKEN LINES!**
> 
> * **1. The Flaw of "Conversational Stasis" (Strictly Prohibited):**
>   - Having a character stand still or freeze just to talk breaks fluid kinetic momentum, drops frame density, and creates artificial soap-opera acting.
> 
> * **2. The Concurrent Fusion Syntax (Physical Action + Dialogue in 1 Stream):**
>   - Dialogue MUST be fused directly into the character's active physical or tactile motion:
>     - *In Combat / Crisis:* `At 10.5s Kenji drives an elbow into Arthur's ribs, speaking in strained guttural Japanese: "動くな！" before pivoting into an immediate hip toss.`
>     - *In Standoff / Tactical:* `At 0.8s Min-ho slices rare steak with the silver knife, generating sharp porcelain friction while speaking in cold Seoul Korean: "조건이 맞지 않아."`
>     - *In Drama / Everyday:* `At 1.6s Valentina pours red wine into her crystal goblet, watching the swirling liquid while speaking in conversational Spanish: "No tenemos tiempo."`
> 
> * **3. Strained Biomechanics of Speech-Under-Exertion:**
>   - Characters speaking during physical exertion naturally display:
>     - *Pre-speech 100ms laryngeal swallow.*
>     - *Intercostal chest compression and breathy vocal strain.*
>     - *Jaw clench immediately following the final phoneme as kinetic follow-through continues seamlessly.*


---

## 🎬👁️ THE OFF-SCREEN DIALOGUE & SIMULTANEOUS VISUAL REVEAL LAW (L-CUT AUDIO-VISUAL COUNTERPOINT)

> [!CAUTION]
> ### 🛑 MASTER CINEMATOGRAPHIC TECHNIQUE: SPEAKING OFF-SCREEN WHILE VISUALLY REVEALING HIDDEN ACTIONS!
> **DO NOT ALWAYS POINT THE CAMERA AT THE SPEAKER'S FACE! USE OFF-SCREEN DIALOGUE TO REVEAL TACTICAL SECRETS, BETRAYALS, AND SOMATIC REACTIONS!**
> 
> * **1. The Power of Audio-Visual Counterpoint (Cross Off-Screen Reveal):**
>   - While Character A is speaking off-camera, the camera simultaneously frames:
>     - **A Hidden Tactical Action:** A hand unholstering a ceramic blade under the table linen, slipping a poisoned ring, or priming a detonator.
>     - **A High-Tension Somatic Reaction:** Extreme close-up on opponent's dilated pupil, masseter jaw twitch, or trembling knuckles.
>     - **An Environmental Forewarning:** Rain lashing glass, a swinging chandelier shadow, or a reflection in a crystal wine glass.
> 
> * **2. Standardized Prose Syntax for Off-Screen Reveals:**
>   `At Ts [Lens Descriptor on Subject B / Prop], Character A's voice resonates off-camera speaking in [Native Dialect / Register] with [Cadence]: "..." while Subject B [Tactile Action / Hidden Reveal / Somatic Reaction].`
>   - *Example:* `At 0.8s [65mm Tight Insert Close-Up], Arthur speaks off-camera in aristocratic British RP: "Checkmate, gentlemen" as Valentina's manicured fingers silently unclasp a ceramic push-dagger beneath the damask tablecloth.`
>   - *Example:* `At 2.1s [50mm Dirty OTS on Kenji], Min-ho speaks off-camera in cold Seoul Korean: "계약은 끝났다" as Kenji's masseter jaw clenches with vascular distension.`
> 
> * **3. Spatial Acoustics & Lip-Sync Integrity (Zero Hallucination Lock):**
>   - Explicitly declaring "off-camera" or "off-screen" guarantees that AI video models **NEVER hallucinate the speaker's face onto the listening character or onto the prop!**
>   - Block 6 `[SPATIAL ACOUSTICS]` spatializes the dialogue diegetically (e.g. `Arthur's dialogue localized to Left-Offscreen with -4dB room ducking and salon reverb`).


---

## 🎭🧠 THE HUMAN-GRADE SCREENPLAY, COHESIVE DIALOGUE RELAY & NARRATIVE UNPREDICTABILITY CODEX

> [!CAUTION]
> ### 🛑 TOP-PRIORITY STORYTELLING MANDATE (ELIMINATING HOLLOW AI SLOGANS & DISJOINTED DIALOGUE):
> **ALL DIALOGUE LINES MUST FORM AN UNBROKEN CAUSAL BATON RELAY WITH HIGH-STAKES TACTICAL SUBSTANCE AND HUMAN-GRADE UNPREDICTABILITY!**
> 
> * **1. The Flaw of Standard LLM Dialogue (Strictly Prohibited):**
>   - ❌ **Disjointed Non-Sequiturs:** Character A drops a proverb, Character B quotes poetry, Character C shouts a generic battle cry with zero causal link between them.
>   - ❌ **Hollow Theatrical Slogans:** "You will regret this!", "Justice never sleeps!", "Words are sharper than swords!". (100% BANNED).
> 
> * **2. The 5 Pillars of Human-Grade Screenwriting & Dialogue Continuity:**
> 
>   * **Pillar 1: The Direct Causal Baton Relay (Rantai Sebab-Akibat Antar-Dialog):**
>     - Every spoken line MUST directly address, challenge, counter, or escalate the premise of the preceding line:
>       - *Line 1 (Premise):* "계약은 끝났다." (The contract ends here.)
>       - *Line 2 (Direct Escalation/Counter):* "動くな、裏切り者。" (Don't move, traitor.)
>       - *Line 3 (Opportunistic Exploitation):* "Checkmate, you bloody fools."
>       - *Line 4 (Tactical Resolution):* "¡Nadie sale vivo de aquí!" (Nobody leaves here alive!)
> 
>   * **Pillar 2: High-Density Tactical Substance (Padat Berisi & Penuh Fakta Konkret):**
>     - Ground lines in concrete leverage: specific codes, asset sums, names, tactical locations, timestamps, or physical threats rather than empty abstract drama.
> 
>   * **Pillar 3: Human Subtext, Irony & Double-Entendre (Subteks & Ironi):**
>     - Real humans speak with layered intent—understatement, dry sarcasm, feigned politeness, or chilling calm before violence.
> 
>   * **Pillar 4: Organic Unpredictability & Tonal Subversion (Kejutan Manusiawi):**
>     - Break linear clichés with authentic human quirks, abrupt tonal shifts (e.g. comedic deadpan juxtaposed against intense military hype), or unexpected tactical betrayals.
> 
>   * **Pillar 5: Dynamic Bursts (1 to 7 Words Ceiling) Fused with Kinetic Exertion:**
>     - Spoken bursts are rapid, pressurized, and delivered while actively slicing, parrying, aiming, or pouring drinks.


---

## 🛑🚫 THE ANTI-EXAMPLE OVERFITTING & DYNAMIC SYNTHESIS HARDWARE LOCK

> [!CAUTION]
> ### ⚠️ CRITICAL ARCHITECTURAL MANDATE FOR ALL AI MODELS (ANTI-EXAMPLE IMITATION LOCK):
> **ALL EXAMPLES IN SYSTEM RULES ARE STRICTLY STRUCTURAL SYNTAX SCHEMAS (META-TEMPLATES)!**
> 
> * **1. Absolute Embargo on Lazy Example Cloning:**
>   - The AI Agent is **STRICTLY FORBIDDEN** from copying, echoing, or defaulting to any example names, heights, dialogue lines, or scenarios found in the system rules (e.g. `Min-ho`, `Kenji`, `Arthur`, `Valentina`, `"Checkmate..."`, `"계약은..."`) **UNLESS EXPLICITLY REQUESTED BY THE USER!**
>   - Reusing example names or lines on an unrelated user prompt is considered a **FATAL CONTEXT-DRIFT DEFECT**.
> 
> * **2. 100% Dynamic Synthesis Mandate:**
>   - For every new user request, the AI Agent MUST dynamically synthesize:
>     - **100% Fresh Character Names & Demographics** tailored strictly to the user's genre and setting (e.g. Cyberpunk, Medieval Fantasy, Jakarta Modern Drama, Tokyo Neo-Noir, High School Anime).
>     - **100% Fresh, Motivated Dialogue** written in the authentic cultural dialect/register matching the specific story.
>     - **100% Fresh Spatial Architecture & Props** motivated by the scene's unique environment.
> 
> * **3. Abstract Meta-Variable Schema:**
>   - All structural formulas operate on dynamic slots:
>     `At [Ts] [[Lens Model]], [Character A Name] ([Height]cm, [Wardrobe]) [Kinetic Micro-Action] speaking in [Native Language/Dialect]: "[Contextual Line <= 7 Words]"`


---

## 🎙️⚡ THE UNPREDICTABLE DIALOGUE TIMELINE & FRAGMENTED STACCATO RHYTHM CODEX

> [!CAUTION]
> ### 🛑 TOP-PRIORITY DIALOGUE RHYTHM MANDATE (ZERO RIGID TEMPLATES & ORGANIC FRAGMENTED DELIVERY):
> **DIALOGUE TIMING MUST BE ORGANICALLY UNPREDICTABLE ACROSS THE TIMELINE, UTILIZING FRAGMENTED STACCATO BURSTS (1 TO 4 WORDS) INTERWOVEN WITH PHYSICAL ACTION!**
> 
> * **1. The Embargo on Formulaic / Predictable Timelines:**
>   - AI is strictly forbidden from placing dialogue at rigid, predictable intervals (e.g. automatically every 3.0s).
>   - Dialogue timestamps must arise **100% organically from narrative tension and physical motivation**:
>     - **Late-Burst Climax:** 25 seconds of silent, tense, high-velocity melee, punctuated only by a chilling 2-word whisper at 26.5s.
>     - **Front-Loaded Volley:** High-pressure verbal exchange in the opening 5 seconds, collapsing into pure physical momentum.
>     - **Staggered Syncopation:** Unexpected single-word commands dropped mid-parry, mid-vault, or during a sudden eyeline saccade.
> 
> * **2. Fragmented Staccato Cadence ("Patah-Patah & Dikit-Dikit"):**
>   - In high-tension or physical exertion scenes, humans do not deliver long run-on sentences.
>   - Complex thoughts are delivered in **broken, pressurized clauses (1 to 4 words per burst)** punctuated by tactile micro-actions and breath resets:
>     - *Example:* `At 1.2s [Action A] speaking in [Dialect]: "Two steps back..." [0.7s parry impact] At 2.1s [Action B]: "...now drop!"`
>     - *Example:* `At 8.4s [Action C] speaking in [Dialect]: "Jangan bergerak..." [0.5s joint pressure] At 9.1s: "...atau patah."`
> 
> * **3. Breath & Foley Interweaving:**
>   - Between fragmented clauses, describe the physiological breath reset (e.g. *intercostal gasp, 100ms laryngeal swallow*) and synchronized foley (blade friction, leather creak) filling the sub-second space.


---

## 🌊🗣️ THE ORGANIC HUMAN SPEECH FLOW & DYNAMIC CADENCE MODULATION CODEX (V20.5 SSOT)

> [!CAUTION]
> ### 🛑 TOP-PRIORITY AUDIT MANDATE: NATURAL ELASTIC SPEECH FLOW (ELIMINATE ROBOTIC FIXED-RATE DIALOGUE)!
> **REAL HUMAN BEINGS DO NOT SPEAK AT A FIXED MONOTONOUS METRONOME SPEED. DIALOGUE CADENCE MUST DYNAMICALLY SHIFT BETWEEN FAST STACCATO BURSTS AND SLOW GRAVITAS DEPENDING ON EMOTIONAL STAKES & PHYSICAL EXERTION!**
> 
> * **1. The 3 Primary Speech-Rate Regimes:**
>   - 🏃‍♂️ **Fast Urgent Regime (2.2 – 3.2 words/sec / ~150–220ms per syllable):**
>     - Triggered by: CQB combat, emergency panic, fleeing from danger, adrenaline surges, tactical shouting.
>     - Delivery: Clipped consonants, explosive plosives, minimal pauses between words, rapid breath intakes.
>     - Example: `speaking in rapid urgent 2.6wps Jakarta staccato: "Tarik rantainya sekarang!"`
>   - 🚶‍♂️ **Natural Conversational Regime (1.5 – 2.0 words/sec / ~250–350ms per syllable):**
>     - Triggered by: Pragmatic negotiations, status reporting, street banter, steady authority.
>     - Delivery: Balanced articulation, relaxed pitch variations, authentic sentence melodic contour.
>     - Example: `speaking in steady measured 1.8wps Betawi cadence: "Bukan meréka musuhnya."`
>   - 🧘‍♂️ **Slow Gravitas & Somatic Intimacy Regime (0.8 – 1.4 words/sec / ~450–750ms per syllable):**
>     - Triggered by: Exhaustion, near-death shock, tender fatherly/motherly comfort, grim revelations, sorrow.
>     - Delivery: Elongated vowels, breathy vocal fry, micro-pauses between clauses, heavy diaphragmatic heaving.
>     - Example: `speaking in slow weary 1.1wps strained Javanese cadence with trailing breath: "Simpan tenagamu buat besok."`
> 
> * **2. Intra-Sentence Elasticity (Dynamic Acceleration & Deceleration):**
>   - A single utterance can change velocity internally:
>     - **Deceleration Arc (Fast ➔ Slow):** Starts with a sharp panicked shout, decaying into a weary whisper (`"Tahan pintunya... jangan lepas..."`).
>     - **Acceleration Arc (Slow ➔ Fast):** Begins with hesitant realization, accelerating into an urgent command (`"Tunggu... lari sekarang!"`).
> 
> * **3. Integration in Prose & Spatial Acoustics:**
>   - In Block 1 `[PROSE]`, always specify both the linguistic dialect AND the vocal tempo profile:
>     `speaking in [Tempo Regime: rapid urgent / steady conversational / slow strained] [Dialect Register]: "..."`
>   - In Block 6 `[SPATIAL ACOUSTICS & LIP-SYNC]`, verify that the phonetic transcriptions and audio ducking durations accurately reflect the calibrated speech rate!


---

## 〰️🌊 THE INTRA-SENTENCE NON-LINEAR DYNAMIC WAVE CODEX (PITCH & TEMPO OSCILLATION SSOT)

> [!CAUTION]
> ### 🛑 TOP-PRIORITY PROSODY DIRECTIVE: INTRA-SENTENCE PITCH, TEMPO & VOLUME OSCILLATION!
> **HUMAN SPEECH WITHIN A SINGLE SENTENCE IS NEVER MONOTONIC OR LINEAR. IT NATURALLY RISES, DIPS, SNAPS, AND DRIFTS IN DYNAMIC WAVE CONTOURS!**
> 
> * **1. The 4 Intra-Sentence Dynamic Wave Archetypes:**
>   - ⛰️ **Wave A: The Climax-Collapse Wave (Low ➔ High Apex ➔ Low Decay):**
>     - Starts in a low strained mutter $\rightarrow$ surges into a high-pitch explosive burst $\rightarrow$ collapses into a low breathless whisper.
>     - *Pattern:* `[Low mutter] "Dengar..." ➔ [High explosive burst] "JANGAN DIBUKA..." ➔ [Low breathy decay] "...bahaya di luar."`
>     - *Directing Tag:* `speaking with an ascending-descending pitch wave (subdued start ➔ high-stress vocal spike ➔ decaying into breathy vocal fry)`
> 
>   - ⚡ **Wave B: The Rebound Snap Wave (High Shout ➔ Low Tension ➔ High Snap):**
>     - Opens with a sharp tactical shout $\rightarrow$ drops into a low suppressed throat rasp $\rightarrow$ snaps violently back up into an urgent bark.
>     - *Pattern:* `[High shout] "TAHAN!" ➔ [Low rasp] "...tunggu aba-aba..." ➔ [High snap] "...SEKARANG TARIK!"`
>     - *Directing Tag:* `speaking with an oscillating rebound cadence (explosive initial shout ➔ dipping into low-pitch tension ➔ snapping up to urgent bark)`
> 
>   - 🏃‍♂️🧘‍♂️ **Wave C: The Staccato-to-Drawl Wave (Rapid Burst ➔ Elongated Vowel Drag):**
>     - Rapid machine-gun syllables that suddenly stretch and drag on the final operative verb under heavy physical effort.
>     - *Pattern:* `[Rapid staccato] "Satu dua tiga..." ➔ [Slow elongated vowel drag] "...dooooorong!"`
>     - *Directing Tag:* `speaking with rapid staccato syllables stretching into an elongated vowel drag under physical torque`
> 
>   - 💔 **Wave D: The Pitch-Crack & Glottal Catch Wave (Somatic Strain & Voice Break):**
>     - Under emotional trauma, grief, or oxygen depletion, vocal cord pitch jumps abruptly mid-word (+80Hz micro-crack) before dropping to a raspy bottom.
>     - *Pattern:* `"Kita semua... [voice cracks on high formant] ke-LA-paran... [dropping to low grumble] sama."`
>     - *Directing Tag:* `speaking with an authentic laryngeal pitch crack on stressed syllables before settling into a weary low baritone`
> 
> * **2. Mandatory Application in Block 1 Prose & Block 6 Audio:**
>   - AI Agent MUST direct the intra-sentence dynamic contour whenever high-stakes or emotionally rich dialogue occurs, ensuring AI voice engines generate living, oscillating, authentic human performances.


---

## 🎭🎙️ THE MULTI-TECHNIQUE DIALOGUE FUSION CODEX (INTRA-CLIP TECHNIQUE DIVERSITY SSOT)

> [!CAUTION]
> ### 🛑 TOP-PRIORITY DIRECTING MANDATE: MULTI-TECHNIQUE DIALOGUE FUSION WITHIN A SINGLE CLIP!
> **A SINGLE 10s–15s CLIP IS NEVER LIMITED TO ONE SINGLE DIALOGUE DELIVERY STYLE. AI AGENTS MUST DYNAMICALLY COMBINE 2 TO 4 DIFFERENT VOCAL TECHNIQUES ACROSS THE TIMELINE OF A SINGLE CLIP!**
> 
> * **1. The 10 Master Dialogue Delivery Techniques Available for Intra-Clip Fusion:**
>   1. ⚔️ **Concurrent Action-Dialogue Fusion:** Speaking actively while exerting physical torque, slicing, prying, or sprinting.
>   2. 👁️ **Off-Screen L-Cut Counterpoint:** Spoken audio originates off-screen while the camera reveals a reaction shot, weapon reload, or ticking timer.
>   3. ⛰️ **Intra-Sentence Dynamic Wave:** Pitch, volume, and speed oscillate (rise ➔ peak ➔ collapse) within a single clause.
>   4. 🤫 **Somatic Breath-Choked Whisper:** Subdued, intimate delivery laden with laryngeal friction and vocal fry.
>   5. 🏃‍♂️ **Rapid Kinetic Staccato:** Machine-gun 2.5–3.2 wps emergency commands.
>   6. 💔 **Emotional Pitch Crack:** Laryngeal voice break (+80Hz) under trauma or grief.
>   7. 💥 **Mid-Word Kinetic Interruption:** Speech abruptly choked off by physical impact, explosion, or tackle (`"Pintu dep—"`).
>   8. 🏋️‍♂️ **Staccato-to-Drawl Torque:** Syllables stretch and drag under extreme physical resistance (`"Satu, dua... dooooorong!"`).
>   9. 😤 **Sub-Vocal Grunts & Phonemic Gasps:** Spontaneous guttural exhalations punctuating tactile collisions.
>   10. 🔄 **Causal Baton Relay:** Multi-party dialogue handoff where each line directly responds to and escalates the previous speaker's tactical cue.
> 
> * **2. Master Directorial Example of 3-Technique Intra-Clip Fusion in 15 Seconds:**
>   - **Beat 1 (At 2.4s | Technique 1 + 5: Rapid Action Staccato):** THE DRIVER slams the crowbar: `"Tarik rantainya sekarang!"`
>   - **Beat 2 (At 6.8s | Technique 2 + 3: Off-Screen Dynamic Wave):** Camera frames the collapsing gate as THE LEADER shouts off-screen: `"[Off-screen, with rising-falling pitch] AWAS... tiarap di bawah!"`
>   - **Beat 3 (At 11.2s | Technique 4 + 6: Strained Whisper with Voice Crack):** Ducking behind concrete, THE DRIVER whispers with a laryngeal catch: `"Gemboknya... lepas..."`


---

## 🎙️⚡ THE TACTICAL DIALOGUE MOTIVATION & DYNAMIC PROSODY WAVE CODEX (SSOT)

> [!CAUTION]
> ### 🛑 ABSOLUTE HARDWARE LOCK FOR DIALOGUE MOTIVATION, INTONATION & ORGANIC TEMPO:
> **UNMOTIVATED DIALOGUE DESTROYS DRAMATIC TENSION. CHARACTERS MUST NEVER SPEAK UNLESS MOTIVATED BY AN INSTANTANEOUS TACTICAL TRIGGER OR CAUSAL STATE-CHANGE!**
> 
> * **1. The "Why Speak Now?" Tactical State-Change Triggers:**
>   A character is STRICTLY FORBIDDEN from uttering dialogue unless triggered by one of these 4 tactical events at that exact sub-second timestamp:
>   - **Trigger 1 (Physical/Mechanical Jam or Failure):** A tool slips, a lock resists, a chain jams ➔ Motivated command: *"Grendelnya nyangkut!"*
>   - **Trigger 2 (Spatial Threat/Vector Alert):** A hazard appears, footsteps approach, glass shatters ➔ Motivated warning: *"Awas beling di bawah!"*
>   - **Trigger 3 (Multi-Body Mass Synchronization):** Coordinated physical push/pull requiring unified timing ➔ Motivated countdown: *"Hitungan tiga... dorong!"*
>   - **Trigger 4 (High-Stakes Discovery/Deception Exposure):** An object is verified, a lie is caught ➔ Motivated realization: *"Bukan ini amplopnya!"*
>   *(If no tactical state-change occurs, the character MUST REMAIN SILENT, communicating through heavy respiration and somatic eyelines!)*
> 
> * **2. Mandatory 4-Vector Prosody & Intonation Descriptor (Anti-Flat-Robot Law):**
>   In Block 1 `[PROSE]`, every spoken line MUST declare its dynamic vocal contour:
>   - Formula: `speaking in [Dialect/Register] with [Pitch Contour: e.g. rising panic / drop to raspy gravelly whisper] and [Cadence: e.g. breathless staccato bursts / voice-crack under adrenaline]: "..."`
>   - *Example:* `speaking in urgent Jakarta street register with rising panic pitch and breathless staccato cadence: "Putar kuncinya sekarang!"`
> 
> * **3. Action-Bound Somatic Breath Integration (FACS AU25/AU26 Parity):**
>   - Spoken words MUST emerge between physical exertion beats — chest heaves, masseter jaw clenching, rapid eye saccades, or wiping sweat.
>   - Dialogue concludes $\ge 0.2s$ before the next camera cut, allowing natural acoustic reverb decay to fill the acoustic volume seamlessly.


---

## 🎙️⚡ THE UNSCRIPTED RAW BEHAVIORAL DIALOGUE CODEX (SUB-VERBAL SOMATIC PRIMACY)

> [!CAUTION]
> ### 🛑 MASTER DIRECTORIAL PARADIGM: 90% SUB-VERBAL SOMATIC ACTION VS 10% PIVOTAL RAW UTTERANCES!
> **FORCING CONTINUOUS SCRIPTED DIALOGUE CREATES ROBOTIC TALKING-HEADS. REAL CINEMA IS BUILT ON RAW UNSCRIPTED SOMATIC BEHAVIOR WHERE WORDS ONLY ERUPT AT MOMENTS OF CRITICAL PHYSICAL FRICTION!**
> 
> * **1. The 90/10 Unscripted Reality Rule:**
>   - **90% Sub-Verbal Acoustic Primacy:** Characters communicate through raw physiological behavior — heavy diaphragmatic gasps, isometric exertion grunts, throat catches, teeth gritting, breathless exhalations, and rapid micro-saccade eye contact.
>   - **10% Pivotal Spontaneous Bursts (Hanya Saat Momen Tertentu):** Spoken words are STRICTLY RESERVED for instantaneous tactical turning points (e.g. a tool snaps, an exit seals, an urgent countdown, a fatal realization).
> 
> * **2. Unscripted Raw Phrasing Standard (1 to 3 Words Maximum):**
>   - When spoken dialogue occurs at those pivotal moments, it must sound completely spontaneous, unpolished, and raw (0% formal sentences):
>   - ✅ *"Tarik!"* (1 word)
>   - ✅ *"Bukan itu!"* (2 words)
>   - ✅ *"Awas bawah, Bang!"* (3 words)
>   - ✅ *"Satu... dua... angkat!"* (3 words)
> 
> * **3. Total Embargo on Scripted Fillers & Chatty Banter:**
>   - Strictly FORBIDDEN to fill silent tension with casual chatter or scripted exposition. Let the physical struggle, foley weight, and somatic eye contact carry the scene!


---

## 🏛️💎 THE 4 ADVANCED MAESTRO CINEMATIC SCIENCES (100% ANTI-SLOP SSOT)

> [!CAUTION]
> ### 🛑 ADVANCED AUTEUR CINEMATOGRAPHY LAWS (WALTER MOURCH, ROGER DEAKINS & BONG JOON-HO STANDARDS):
> 
> * **1. The 3D Triangular Eyeline-Match Law (Geometri Tatapan Saling Mengunci):**
>   - In any two-character confrontation, camera cuts MUST preserve reciprocal 3D eyeline vectors:
>   - If Shot 1 frames Character A on screen-left looking 45° screen-right ➔ Shot 2 [HARD CUT] MUST frame Character B on screen-right looking 45° screen-left.
>   - Eliminates disorientation and locks visceral psychological tension!
> 
> * **2. The 3-Plane Volumetric Depth Staging Law (Foreground / Midground / Background):**
>   - Every frame MUST establish 3 distinct visual depth planes to eliminate flat cardboard staging:
>     - **Foreground Plane (0.3m–0.8m):** Tactile out-of-focus obstruction (dirty shoulder, rain-streaked glass, steaming cup, iron rebar).
>     - **Midground Plane (1.2m–2.5m):** Primary active characters executing high-tension physical action.
>     - **Background Plane (3.0m–10.0m):** Deep architectural textures, dense practical haze gradients, or environmental light leaks.
> 
> * **3. The J-Cut / L-Cut Acoustic Lead Law (Suara Menuntun Visual):**
>   - Cuts feel 1000% more natural when audio and visual do not slice simultaneously:
>     - **J-Cut (Audio Lead):** A foley sound (clanging chain, footsteps, gas hiss) erupts 0.2s *BEFORE* the visual cut to that object.
>     - **L-Cut (Reaction Hold):** A character's spoken word or breath exhalation carries over 0.2s–0.4s *AFTER* the visual cuts to the listening partner's face.
> 
> * **4. Walter Murch's Rule of Six (Emotion-Driven Cutting):**
>   - Cuts are NEVER arbitrary timer ticks. Every `[HARD CUT]` MUST be triggered by:
>     1. Emotional Shift (51%)
>     2. Tactical Story Progression (23%)
>     3. Physical Kinetic Impact / Rhythm (10%)
>     4. Eye-Trace Continuity (7%)
>     5. 2D Screen Space Balance (5%)
>     6. 3D Spatial Geometry (4%)


---

## 👄⚡ THE CONTINUOUS PHONETIC LIP-SYNC SYNCHRONIZATION & ZERO-MOUTH-FREEZE CODEX (SSOT)

> [!CAUTION]
> ### 🛑 ABSOLUTE HARDWARE LOCK: ZERO PREMATURE MOUTH-FREEZING OR AUDIO-VISUAL LIP DESYNCHRONIZATION!
> **DIFFUSION MODELS OFTEN CLOSE THE CHARACTER'S MOUTH PREMATURELY WHILE DIALOGUE AUDIO IS STILL PLAYING. THIS FATAL DEFECT IS COMPLETELY ERADICATED VIA THE 4-PILLAR PHONETIC SYNCHRONIZATION PROTOCOL BELOW!**
> 
> ```text
> ┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
> │                 THE 4-PILLAR CONTINUOUS LIP-SYNC & ZERO-MOUTH-FREEZE PROTOCOL                          │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 1. 🗣️ CONTINUOUS LABIAL-LINGUAL PHONETIC ARTICULATION DIRECTIVE (IN PROSE & ACTING BLOCKS)             │
> │    • In Block 1 [PROSE] & Block 3 [ACTING]: Whenever spoken dialogue is declared, the prompt MUST       │
> │      explicitly enforce continuous mouth motion:                                                       │
> │      ➔ "with continuous active labial-lingual mouth articulation (lips parting, teeth flashing,        │
> │         and jaw dropping in exact dynamic synchronization with every spoken syllable from start to     │
> │         final word decay — strictly 0% premature mouth freezing, 0% ventriloquism, 0% static lips)"    │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 2. 🦷 PANEL 4 CHARSHEET OPEN-PHONEME CALIBRATION ANCHOR (TURN 4)                                       │
> │    • In Turn 4 Panel 4 (Speaking Front View): Must ALWAYS be rendered with parted lips exposing teeth: │
> │      ➔ "Direct straight frontal headshot with parted lips and visible upper/lower teeth (AU25/AU26     │
> │         open-mouth phoneme calibration posture, strictly 0% closed-lip stasis, 0% 3/4 angle)"           │
> │      (Provides the diffusion latent space with active open-mouth weights for seamless lip motion!).    │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 3. ⏱️ 0.3s PRE-CUT VOCAL SETTLE BUFFER & NATURAL MOUTH-CLOSURE TAIL                                    │
> │    • Dialogue MUST conclude >=0.3s BEFORE any [HARD CUT] (Dialogue End <= Cut Timestamp - 0.3s).       │
> │    • The final syllable is followed by an explicit 0.2s natural mouth-closure and swallowing motion:   │
> │      ➔ "lips cleanly seal on the final consonant as acoustic reverb decays naturally through the cut"   │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 4. 📐 OPTICAL FOCAL PROXIMITY & EYELINE READABILITY FOR SPOKEN SHOTS                                   │
> │    • Active spoken dialogue MUST be framed in MCU/CU (40mm–85mm) with unobstructed mouth visibility.   │
> │    • If character speaks while facing away or in extreme wide (>10m), explicitly declare:              │
> │      ➔ "speaking off-camera / back-turned with zero facial lip-sync demand on visible rear head"       │
> │      (Prevents AI from hallucinating a distorted mouth on the back of the head or cheek!).             │
> └────────────────────────────────────────────────────────────────────────────────────────────────────────┘
> ```


---

## 🗣️⚡ THE MULTI-BURST CONVERSATIONAL EXCHANGE PROTOCOL (A-B-A-B-A-B DYNAMIC RELAY)

> [!CAUTION]
> ### 🛑 ABSOLUTE MANDATE: SUPPORT RICH MULTI-BURST DIALOGUE EXCHANGES WITHIN A SINGLE 15s CLIP!
> **SINGLE ISOLATED SPOKEN LINES ARE PROHIBITED AS A DEFAULT LIMITATION. TWO CHARACTERS CAN ENGAGE IN RAPID, HIGH-VELOCITY, DYNAMIC CONVERSATIONAL EXCHANGES (A ➔ B ➔ A ➔ B ➔ A ➔ B) WITHIN A SINGLE 10s–15s CLIP!**
> 
> ```text
> ┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
> │             THE 6-BURST A-B-A-B-A-B RAPID DIALOGUE RELAY TIMELINE (15s DYNAMIC CLIP)                   │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ • 0.8s – 2.0s : A (@Image1) Burst 1 (1-3 words) ➔ "Buka kuncinya!" (Urgent order)                      │
> │ • 2.5s – 3.8s : B (@Image2) Burst 2 (1-3 words) ➔ "Macet, Bang!" (Tactical obstacle report)            │
> │ • 4.5s – [HARD CUT: OTS CU] – 5.8s : A Burst 3 (1-3 words) ➔ "Dobrak sekarang!" (Decisive command)    │
> │ • 6.5s – 7.8s : B Burst 4 (1-3 words) ➔ "Hitungan tiga!" (Coordination callout)                       │
> │ • 8.5s – [HARD CUT: ECU] – 9.8s : A Burst 5 (1-2 words) ➔ "Satu... dua..." (Pacing lead)              │
> │ • 10.5s – 11.8s: B Burst 6 (1 word) ➔ "Dorong!" (Explosive physical climax bark)                       │
> │ • 12.0s – 15.0s: Pure physical collision, living static settle hold with heavy diaphragmatic panting.  │
> └────────────────────────────────────────────────────────────────────────────────────────────────────────┘
> ```
> 
> * **Rules for Multi-Burst Execution:**
>   - **Non-Overlapping Stagger:** Maintain 0.4s–0.8s breath/pause gaps between bursts to ensure 100% clean AI acoustic synthesis and distinct lip-sync rendering.
>   - **Word Economy:** Keep individual bursts between 1 to 4 words (punchy, urgent, highly motivated).
>   - **Action Binding:** Each burst MUST synchronize with active physical movement (pulling, pushing, dodging, glancing).

---

## 🏃⚡ THE ZERO-RESET CUT-ON-ACTION & MULTI-CLIP KINETIC CONTINUITY CODEX (SSOT)

> [!CAUTION]
> ### 🛑 TOP-TIER DIRECTORIAL MANDATE: ABSOLUTE ZERO-RESET CUT-ON-ACTION CONTINUITY!
> **ACROSS EVERY [HARD CUT] WITHIN A CLIP, AND ACROSS EVERY MULTI-CLIP SEAM (0.0s RELAY), KINETIC MOMENTUM MUST FLOW CONTINUOUSLY WITHOUT POSTURAL RESETS, TELEPORTATION, OR VELOCITY DROPS!**
> 
> ```text
> ┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
> │                 THE 4-AXIS ZERO-RESET CUT-ON-ACTION CONTINUITY PROTOCOL                                │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 1. 📐 INTRACLIP CUT-ON-ACTION MATCHING (Eulerian Momentum Conservation):                               │
> │    • If Shot 1 ends at 3.5s with Character A's shoulder ramming a door at 45° angle with velocity v:   │
> │    • Shot 2 [HARD CUT] at 3.5s MUST open from the exact same 45° angle, matching velocity vector,     │
> │      showing the buckling steel panel in reverse OTS/profile — STRICTLY 0% resetting to standing!      │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 2. 🌉 INTERCLIP 0.0s SEAM HANDOVER (Multi-Clip Kinetic Relay):                                         │
> │    • Clip N ending frame is locked in the Inter-Clip Handover Bridge (Position, Limb Angle, Speed).   │
> │    • Clip N+1 at 0.0s MUST open matching this exact velocity vector: if sprinting out of a door in    │
> │      Clip 1, Clip 2 at 0.0s opens mid-stride with leading foot striking the wet pavement outside!     │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 3. 🩸 DAMAGE & PROP CONTINUITY PARITY:                                                                │
> │    • Bleeding lacerations, torn cloth, and held props NEVER magically heal or vanish across cuts.       │
> │    • If a flashlight is gripped in left hand at Cut 1, it remains in left hand at Cut 2.               │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 4. 👁️ 180° AXIS OF ACTION & EYE-TRACE CONSERVATION:                                                   │
> │    • Camera never jumps across the 180° line during combat or chase sequences.                         │
> │    • Screen-direction remains coherent (Left-to-Right momentum continues Left-to-Right across cuts).   │
> └────────────────────────────────────────────────────────────────────────────────────────────────────────┘
> ```


---

## ⚡⏱️ THE 10-SECOND DYNAMIC MULTI-BURST CONVERSATIONAL PROTOCOL (A-B-A-B & A-B-A-B-A-B IN 10s)

> [!CAUTION]
> ### 🛑 10-SECOND CLIP CALIBRATION: HIGH-OCTANE STACCATO MULTI-BURST EXCHANGES!
> **IN A 10-SECOND CLIP, CHARACTERS CAN DELIVER 4 TO 6 RAPID STACCATO BURSTS (A ➔ B ➔ A ➔ B) WITH 100% CLEAN SYNCHRONIZATION AND ZERO OVERLAP!**
> 
> ```text
> ┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
> │             THE 10-SECOND RAPID 4-BURST & 6-BURST TIMELINE BLUEPRINTS (10s DYNAMIC CLIP)               │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 🎯 PATTERN 1: 4-BURST TACTICAL CRISIS RELAY (10s):                                                     │
> │ • 0.6s – 1.8s : A (@Image1) Burst 1 (1-2 words) ➔ "Buka sekarang!" (Urgent order)                      │
> │ • 2.2s – 3.4s : B (@Image2) Burst 2 (1-2 words) ➔ "Grendelnya patah!" (Tactical obstacle)             │
> │ • 3.8s – [HARD CUT: OTS CU] – 5.0s : A Burst 3 (1-2 words) ➔ "Tarik bareng!" (Unified command)        │
> │ • 5.5s – 6.8s : B Burst 4 (1-2 words) ➔ "Satu... dorong!" (Physical sync callout)                     │
> │ • 7.2s – 10.0s: Physical collision, structural yield, living settle hold with rapid chest panting.    │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ ⚡ PATTERN 2: 6-BURST STACCATO COMBAT BARK RELAY (10s):                                                │
> │ • 0.5s – 1.3s : A Burst 1 ➔ "Awas!"                                                                    │
> │ • 1.6s – 2.4s : B Burst 2 ➔ "Mana?!"                                                                   │
> │ • 2.8s – [HARD CUT: 85mm CU] – 3.8s : A Burst 3 ➔ "Kiri!"                                              │
> │ • 4.2s – 5.1s : B Burst 4 ➔ "Kena!"                                                                    │
> │ • 5.6s – [HARD CUT: ECU] – 6.6s : A Burst 5 ➔ "Tarik!"                                                 │
> │ • 7.0s – 7.8s : B Burst 6 ➔ "Lepas!"                                                                   │
> │ • 8.0s – 10.0s: Recoil momentum, acoustic reverb decay, living settle hold through frame 10.0s.        │
> └────────────────────────────────────────────────────────────────────────────────────────────────────────┘
> ```
> 
> * **Precision Stagger Gap:** Maintain 0.3s–0.5s rapid recovery pauses between 1-word/2-word barks in 10s clips to preserve 100% lip-sync sharpness.


---

## 🎙️⚡ THE GROUNDED CINEMA-VERITÉ DIALOGUE & VOCAL PHRASING CODEX (SSOT)

> [!CAUTION]
> ### 🛑 ABSOLUTE MANDATE: DIALOGUE MUST OPERATE AT 100% GROUNDED CINEMA-VERITÉ REALISM!
> **DIALOGUE IN BREAKSTUDIO IS NEITHER SCRIPTED THEATRICAL DRAMA NOR POLISHED VOICE-OVER. IT IS RAW, UNVARNISHED, GROUNDED HUMAN UTTERANCES CAPTURED LIVE ON DIEGETIC MICROPHONES!**
> 
> ```text
> ┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
> │              THE 5 PILLARS OF GROUNDED CINEMA-VERITÉ DIALOGUE (BREAKSTUDIO)                    │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 1. 🫁 RESPIRATORY & LUNG FRICTION (Suara Terhimpit Oksigen):                                           │
> │    • Words are physically constrained by lung capacity: voice cracks under high formant stress,       │
> │      subdued guttural rasps, throat catches, and heavy diaphragmatic exhalations between syllables.   │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 2. ⚡ TACTICAL BURST CONCISENESS (1 to 3 Words Maximum in Crisis):                                     │
> │    • 0% formal complete sentences ("Apakah kau sudah mengambil kuncinya?").                            │
> │    • 100% emergency tactical fragments: "Kuncinya mana?!", "Macet, Bang!", "Tarik bareng!", "Awas!"   │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 3. 🔨 PHYSICAL TASK SYNCHRONIZATION (Bicara Sambil Kerja Otot):                                        │
> │    • Characters NEVER stop to talk. Dialogue erupts WHILE straining against steel, prying latches,     │
> │      running down wet corridors, or bracing door frames under 120Nm physical load.                    │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 4. 🗣️ NATIVE STREET & REGISTER AUTHENTICITY (Dialek Membumi 100%):                                    │
> │    • Spoken in authentic vernacular registers (Jakarta street conversational, Javanese medok,         │
> │      urgent CQB radio callouts) with exact 'é' taling diacritics where required by KBBI.               │
> ├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
> │ 5. 🔊 DIEGETIC ROOM ACOUSTICS & NATURAL FOLEY BLEED:                                                   │
> │    • Spoken audio carries realistic acoustic room resonance (RT60 decay) and diegetic foley bleed     │
> │      (textile friction, rain impact, boot scraping), decaying naturally through the cut.              │
> └────────────────────────────────────────────────────────────────────────────────────────────────────────┘
> ```
> 
> * **Block 1 [PROSE] & Block 6 [AUDIO] Master Synthesis Tag:**
>   - Formula: `speaking in authentic grounded [Cultural Register] with [breathless staccato / laryngeal voice crack under adrenaline]: "..."`


---

## 🔊🚫 THE ANTI-ACOUSTIC BALLOONING & CRISP HIGH-TRANSIENT FOLEY HARDWARE LOCK (SSOT V20.5)

> [!CAUTION]
> ### 🛑 ZERO-TOLERANCE LAW: EMBARGO ON BLOATED / BOOMY / MUDDY SUB-BASS SFX ("SFX MENGGELEMBUNG")
> AI Audio/Video diffusion models (Kling Audio, Wan 2.1 Audio, Sora, Runway, Hailuo, ElevenLabs) are prone to generating bloated, boomy low-frequency mud, cavernous underwater phasing, and synthetic sub-bass rumble (<80Hz saturation) that destroys dialogue intelligibility.
> 
> The AI Agent MUST strictly enforce the following 5 Acoustic Anti-Bloat Directives in Block 6 `[SPATIAL ACOUSTICS, FOLEY & WORD-BY-WORD LIP-SYNC]`:
> 
> 1. 🚫 **Strict Embargo on Synthetic Sub-Bass Booms & Bass Drops:** Strictly forbid `0% synthetic sub-bass booms`, `0% cinematic bass drops`, `0% cavernous underwater rumble`, `0% bloated low-frequency saturation`, `0% limiter pumping`.
> 2. 🎛️ **High-Pass Damping & Sub-Bass Cut (<80Hz Roll-Off):** Mandatorily specify: `"tight high-pass acoustic profile rolling off muddy sub-bass below 80Hz, preserving natural mid-bass punch without low-end bloating"`.
> 3. 🔨 **Crisp High-Transient Tactile Attack (2kHz – 8kHz Focus):** Focus tactile foley on mechanical, bone, glass, metal, and shoe transients: `"dry tactile high-transient foley with crisp initial attack (2kHz–8kHz range), clean mechanical clicks, sharp dental consonants, and immediate acoustic decay"`.
> 4. 📉 **Tight Acoustic Decay & Controlled RT60 (<0.35s):** Lock room reverberation to dry real-world domestic/industrial damping: `"dry room dampening with tight RT60 < 0.35s decay, strictly 0% muddy reverberant tails, 0% hollow cavernous phasing"`.
> 5. 🎙️ **Tri-Band Frequency Separation:** Enforce clean dynamic headroom: Dialogue fundamental (100Hz–250Hz), Mid-range foley snap (1kHz–4kHz), Airy room tone (8kHz–12kHz) with -4dB diegetic ducking during vocal delivery.


---

## 🧠🎭 THE APEX DIRECTORIAL SORCERY & PSYCHO-PERCEPTUAL HARDWARE LOCK (MODUL 11 SSOT)

> [!CAUTION]
> ### 🛑 APEX DIRECTING MANDATE: HARNESS PSYCHOLOGICAL & SUBCONSCIOUS CINEMATICS!
> When elevating dramatic tension, the AI Director is authorized and commanded to deploy:
> 1. **Relativistic Time Dilation** (stretching visceral seconds / compressing eras).
> 2. **Diegetic Spatial Drift** (subconscious architectural evolution reflecting mental states).
> 3. **Subconscious Geometric Dominance** (axial diagonal power vectors, headroom compression).
> 4. **Audio-Visual Cognitive Dissonance** (brutal visual contrast against ethereal audio counterpoint).
> 5. **Trojan Emotional Convergence** (disarming banality pivoted instantaneously into seismic drama).


---

## 🎭🎙️ THE PSYCHO-SOMATIC ACTING & VOCAL FRICTION HARDWARE LOCK (MODUL 12 SSOT)

> [!CAUTION]
> ### 🛑 ACTING & DIALOGUE MANDATE: ZERO FROZEN TALKING HEADS / 100% SUBTEXT & PHYSICAL LABOR!
> The AI Director MUST strictly enforce:
> 1. **Subtextual Masking:** Dialogue words $\neq$ internal somatic state (calm words vs tense masseter).
> 2. **Occupied Physical Labor:** Characters speak while physically exerting effort (0% static statues).
> 3. **Reactive Listening:** Camera frequently anchors on listener's micro-reactions.
> 4. **Hesitation & Unfinished Sentences:** motived 0.3s pauses and interrupted bursts.
> 5. **Vocal Friction & Acoustic Grain:** Pre-speech breath gasps, raspy vocal fry, and crisp consonants.


---

## 🗣️🎼 THE MASTER DIALOGUE SCALES & COMBINATORICS HARDWARE LOCK (MODUL 05f SSOT)

> [!CAUTION]
> ### 🛑 DIALOGUE ARCHITECTURE MANDATE: DYNAMIC 1–7 WORD SCALES & NON-PING-PONG PATTERNS!
> The AI Director MUST orchestrate dialogue across the 4 Dynamic Length Scales and 4 Combinatorial Waves:
> 1. **4 Length Scales:** Tier 1 (1W Snap), Tier 2 (2–3W Jab), Tier 3 (4–5W Clause), Tier 4 (6–7W Compound Max).
> 2. **4 Combinatorial Waves:** Exponential Escalation, Collapsing Reversal, Asynchronous CQB, and Abandoned Utterances.
> 3. **Timing & Cut Integrity:** Every utterance concludes $\ge 0.2s$ before cuts with $\le 2.0$ wps natural pacing.


---

## 🎙️⚡ THE DYNAMIC DIALOGUE CADENCE & RAPID-BURST HARDWARE LOCK (MODUL 05f SSOT)

> [!CAUTION]
> ### 🛑 DIALOGUE CADENCE MANDATE: ORCHESTRATE BREATH-PULSE CLUSTERING!
> Even in fast rapid-fire speech (*"nyerocos"*), the AI Director MUST cluster words into **Breath-Pulse Bursts (1–4 words per burst separated by 80ms micro-gasps)**.
> Rotate through the 5 Cadence Archetypes: Rapid-Fire Staccato, Monosyllabic Sniper, Interrupted Collision, Staggered Baton Relay, and Expiratory Ramp.


---

## 🎙️⚡ THE MASTER DIALOGUE CADENCE & RHYTHMIC SCALES HARDWARE LOCK (MODUL 13 SSOT)

> [!CAUTION]
> ### 🛑 DIALOGUE RHYTHM MANDATE: SELECT FROM THE 6 MASTER CADENCE ARCHETYPES!
> The AI Director must dynamically match dialogue delivery to the emotional rhythm:
> 1. **Rapid Motor-Mouth Patter (Nyerocos):** 3.0–3.8 syl/s, fast jaw articulation (5–7 words burst).
> 2. **Staccato Tactical:** 1–3 words explosive commands with plosive consonants.
> 3. **Breathless Trauma:** Fragmented single words separated by 200ms gasps.
> 4. **Cold Slow-Burn:** 1.0–1.4 syl/s with 0.5s menacing pauses.
> 5. **Chaotic Cross-Talk:** Staggered multi-speaker audio with spatial L/R separation.
> 6. **Sub-Verbal Choke:** Silent mouth opening with breath hiss and somatic despair.


---

## 🗣️🎛️ THE POLYPHONIC CONVERSATIONAL CHOREOGRAPHY HARDWARE LOCK (MODUL 13b SSOT)

> [!CAUTION]
> ### 🛑 CONVERSATIONAL DYNAMICS MANDATE: ENFORCE 6 POLYPHONIC ARCHETYPES!
> The AI Director is equipped to orchestrate complex multi-speaker dynamics:
> 1. **Extended Monologue:** Solo speaker dominating with listener somatic absorption.
> 2. **Violent Interruption:** Cutting off speech with em-dash and sudden vocal slam.
> 3. **Rapid Baton Relay:** 1–2 word ping-pong exchanges with 0.15s staggering.
> 4. **Dynamic Vocal Focus Shift:** Rack-focusing audio/camera from Foreground to Background speaker.
> 5. **Hierarchical Cross-Talk:** Primary (+0dB) vs Secondary (-4dB) simultaneous tracks.
> 6. **Off-Screen Anchor:** Framing listener on-screen while speaker projects from off-frame.


---

## 🎭💎 THE DRAMATIC DIALOGUE PURPOSES & EMOTIONAL SUBSTANCE HARDWARE LOCK (MODUL 13c SSOT)

> [!CAUTION]
> ### 🛑 DIALOGUE SUBSTANCE MANDATE: ZERO EMPTY LOGISTICAL DIALOGUE SPAM!
> Dialogue must possess rich human soul, subtext, and dramatic purpose beyond dry physical commands.
> The AI Director is commanded to orchestrate rich dialogue across:
> 1. **Banal Banter in Crisis:** Dark humor / absurd domestic trivialities under high tension.
> 2. **Vulnerable Confessions (Curhat):** Raw unburdening of soul and personal trauma.
> 3. **Passive-Aggressive Sarcasm:** Subtextual domestic/relational venom.
> 4. **Power Negotiation:** Cold psychological dominance without raising voice.
> 5. **Shared History Shorthand:** Unspoken backstory anchored in concise memory triggers.
> 6. **Moral & Existential Dilemmas:** Clashing philosophies of life and sacrifice.
> 7. **Intimate Tender Solace:** Quiet emotional sanctuary amidst devastation.


---

## 🌊🗣️ THE EXTREME SPEECH MODALITIES & MONOLOGUE HARDWARE LOCK (MODUL 13d SSOT)

> [!CAUTION]
> ### 🛑 EXTREME SPEECH MANDATE: MASTER THE 8 ADVANCED VOCAL MODALITIES!
> The AI Director possesses full range over the 8 extreme speech archetypes:
> 1. **Stream-of-Consciousness:** 15s–30s continuous uninhibited manic flood.
> 2. **Demagogic Oratory:** Booming charismatic crescendo (55dB ➔ 85dB).
> 3. **Forensic Summation:** Relentless factual indictment and deductive pacing.
> 4. **Psychotic Delirium:** Fragmented syntax, hallucinated targets, pitch shifts.
> 5. **Clinical Technical:** Emotionless terror through cold data readouts.
> 6. **Gaslighting Seduction:** Soft purring cadence making horror sound rational.
> 7. **Rhythmic Vernacular:** Syncopated street slang and metric rhyming cant.
> 8. **Terminal Testament:** Dying breath whispering transcendent legacy.


---

## 🎙️🎚️ THE VOICEOVER (VO) WPS SYNCHRONIZATION & PACING HARDWARE LOCK (SSOT V20.5)

> [!CAUTION]
> ### 🛑 VOICEOVER PACING MANDATE: ENFORCE MATHEMATICAL WPS & DYNAMIC DUCKING!
> **VOICEOVER (VO) MUST NEVER SOUND RUSHED, CHOPPY, OR UNNATURALLY LETHARGIC. EVERY VO LINE MUST BE MATHEMATICALLY BALANCED AGAINST ITS VISUAL TIME WINDOW!**

### 1. 🧮 THE WORDS PER SECOND (WPS) FORMULA:
$$\text{WPS} = \frac{\text{Word Count}}{\Delta t (\text{End.s} - \text{Start.s})}$$

### 2. 🎚️ THE 3 VO SPEED REGIMES:
1. **Contemplative / Somatic Cadence (1.3 – 1.6 WPS):**
   - High emotional gravitas, elegiac or horror narration. Extended vowel sustains, deep chest resonance.
2. **Cinematic Baseline (1.7 – 2.0 WPS — OPTIMAL SWEET SPOT):**
   - Standard storytelling, documentary, character voiceover. Crystal clear articulation and organic breath pauses.
3. **High-Urgency Hook / Trailer (2.1 – 2.4 WPS):**
   - Rapid-fire promotional or action hooks. Tight syllables, high energy.
   - ❌ **UPPER CEILING:** Strictly forbidden $> 2.4\text{ WPS}$ (causes rapid gibberish, dropped syllables, or chipmunk compression).
   - ❌ **LOWER FLOOR:** Strictly forbidden $< 1.3\text{ WPS}$ (causes sluggish pacing, unnatural dragging, and clip overrun).

### 3. 🔊 MASTERING & DUCKING SPECIFICATIONS:
- **Master Level:** Mastered to **-14 LUFS** vocal clarity.
- **Acoustic Proximity:** Large-diaphragm condenser proximity (intimate 10–15cm cardioid capture, clean pop-filter, dry acoustics).
- **Dynamic Vocal-Pocket Ducking:** Foley and environmental bed MUST duck by **-4dB to -6dB at 2.5kHz** synchronized precisely with the voiceover window `[Start.s–End.s]`.
- **Anti-Mouth-Flapping Biometric Lock:** During VO, all characters visible in frame MUST be explicitly locked with: `lips closed in resting state, 0% mouth moving for VO`.
