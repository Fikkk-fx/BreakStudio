---
name: 05b-indonesian-phonetics-and-etaling-codex
description: "Indonesian Phonetics & KBBI-Verified Dual-'E' (Pepet [ə] vs Taling [e]) Engine, Dictionary Lookup Priority, and Mathematical Word-Budget Calculator."
---

# 🇮🇩 BREAKSTUDIO — MODULE 05B: THE MASTER INDONESIAN PHONETICS & KBBI E-TALING CODEX
========================================================================================================
KBBI-VERIFIED DUAL-'E' PHONETICS ENGINE (PEPET ê [ə] VS TALING é [e]) & LIP-SYNC DISSECTION (V20.5)
========================================================================================================

This module provides the **MULTILINGUAL INDONESIAN PHONETICS & DIACRITIC ANCHORING ENGINE**.
When generating scenes with spoken Indonesian dialogue, this engine guarantees 100% accurate lip-sync and vowel articulation across all AI video and TTS models.

---

## 📚 SECTION I: THE DUAL-'E' PHONETIC ENGINE (PEPET VS TALING)

The Indonesian language features two distinct phonetic values for the letter 'e':
1. **Pepet ê [ə]** (Mid Central Vowel): Pronounced /uh/ as in *bê-sar*, *gê-lap*, *tê-pat*, *kê-ras*.
2. **Taling é [e]** (Close-Mid Front Vowel): Pronounced /ay/ as in *mé-ja*, *tém-bok*, *bé-sok*, *dé-sa*.

### ✍️ DIACRITIC ANCHORING LAW:
* In all spoken Indonesian dialogue inside `[PROSE]` and `[ACTING]`, words containing **Taling** MUST be marked with the diacritic `é` (e.g., `"Lampu méja menyala di dépan témbok!"`).
* Words containing **Pepet** remain unmarked `e` (e.g., `besar`, `gelap`, `keras`).

---

## ⛔ SECTION II: FALSE TALING TRAPS (100% PEPET — STRICTLY FORBIDDEN FROM TALING MARKING)
The following common root words are **100% PEPET ê [ə]** and must NEVER be accented with `é`:
`besar, gelap, keras, lekas, penat, redam, sesal, tenang, tepat, lelah, terbang, menang, sedih, tegak, pedih`.

---

## 📖 SECTION III: PRIORITY KBBI DICTIONARY LOOKUP
* System prioritizes lookup in `rules/05d_indonesian_e_taling_dictionary.md` (117 verified root entries).
* 3-Tier Resolution Order:
  1. Primary: Exact match in `rules/05d_indonesian_e_taling_dictionary.md`.
  2. Secondary: Morphological root inference (e.g., prefix `men-` + `témbak` = `menémbak`).
  3. Tertiary: Flagged LLM phonetic fallback for rare colloquial words.

## 🎙️🔤 SECTION V: EXHAUSTIVE WORD-BY-WORD PHONETIC TRANSCRIPTION IN BLOCK 6
Declare phonetic breakdown for every single word in the dialogue line to eliminate accent hallucination.

---

## 🏛️ SECTION III: THE NUSANTARA REGIONAL DIALECTS & CULTURAL SOCIOLINGUISTICS

When characters deliver dialogue in Indonesian regional cultural registers, anchor the pronunciation and lexical syntax accurately:
1. **Jakarta Conversational (Bahasa Gaul / Metropolitan):** Natural particles (*nih, tuh, deh, dong, sih*), contracted verbs (*ngambil, nyari, ngeliat*), fast rhythmic cadence.
2. **Javanese Medok / Central & East Java:** Heavy voiced bilabial and dental stops ([b], [d], [g] with breathy phonation), particle *ta, po'o, rek, lho*, calm restrained pitch or fast Suroboyoan staccato.
3. **Sunda Cultural Register:** Soft melodic intonation, rising question markers, particle *mah, téh, atuh, euy*, polite vocal timbre.
4. **Batak / North Sumatra Register:** Sharp crisp dental plosives, resonant chest projection, direct urgent cadence, particle *bah, da, lek*.
5. **East Indonesia (Manado / Ambon / Papua):** Glottal stops, contracted pronouns (*dong, torang, kitorang*), vibrant open vowel articulation.

---

## 🇯🇵 SECTION IV: THE NIHON CINEMATIC SOCIOLINGUISTIC ENGINE (HONNE VS TATEMAE)

When writing dialogue for Japanese characters or East Asian settings:
1. **Honne (Internal Truth) vs Tatemae (Public Restraint):** Japanese characters prioritize social composure (*Tatemae*) during tense situations, releasing raw emotional fury (*Honne*) only in extreme physical crisis.
2. **Speech Formality Registers:** Distinguish between polite formal business Japanese (*Keigo / Desu-Masu*), informal squad camaraderie (*Tameguchi*), and aggressive Yakuza / CQB guttural imperatives (*Kuso, Yame-ro, Temee*).
3. **Tatami Framing & Deadpan Delivery:** Complement Japanese dialogue with low-angle Tatami framing (Ozu style) or deadpan static wide shots (Kitano style) where violence erupts suddenly without melodramatic windup.