---
name: progressive-state-chain-and-decision-gate-codex
description: "Progressive state evolution (A->B->C), the 3-gate state creation decision protocol, temporal causality guards, asset census reconciliation, and crowd-mass texture collapse."
---

# 🧬 19. PROGRESSIVE STATE CHAIN & DECISION GATE CODEX

## §BA-DECIDE — THE 3-GATE STATE CREATION DECISION PROTOCOL
Deciding when a physical change warrants generating a new **STATE REF ASSET SHEET** must follow a strict 3-gate deterministic filter to prevent wasted sheets (over-sheeting) or broken visual continuity (under-sheeting):

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE 3-GATE DECISION PROTOCOL (§BA-DECIDE)                     │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ GATE 1: CAUSE?                                                                          │
│   Is there an explicit, visible physical cause or tagged timeskip (§BA-CAUSE)?          │
│   └── NO  ──► REUSE EXISTING STATE SHEET (0% Uncaused Evolution).                       │
│   └── YES ──► Proceed to Gate 2.                                                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ GATE 2: PERSISTS?                                                                       │
│   Does the physical change outlast the current clip into Clip N+1 (§BA-PERSIST)?       │
│   └── NO  ──► L1 TRANSIENT (Splash, dust, breath fog) -> Handle inside clip, NO SHEET.  │
│   └── YES ──► Proceed to Gate 3.                                                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ GATE 3: VISIBLE?                                                                        │
│   Is the change above the visual noticeability threshold in upcoming framings?         │
│   └── NO  ──► Sub-threshold micro-detail -> Log in ledger value only, NO SHEET.        │
│   └── YES ──► ALL 3 PASSED -> GENERATE EXACTLY ONE NEW STATE SHEET (State B, C, etc.). │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### ⚡ STATE EFFICIENCY LAWS:
1. **MERGE SAME-CLIP CHANGES:** Multiple physical wounds or stains occurring on one character in the SAME clip merge into **EXACTLY 1 NEW STATE SHEET** (e.g. `SILAS-B` carries both the torn collar and the cheek laceration).
2. **NO SPECULATIVE STATES:** Never generate sheets for hypothetical states not reached in the actual screenplay.
3. **SINGLE-CLIP PROJECTS (§BB):** A 1-clip standalone project NEVER requires State B sheets.

---

## §BA-TIME — TEMPORAL CAUSALITY GUARD (ANTI-COPY-AHEAD LAW)
Diffusion prompts must strictly respect story chronology:
- **THE COPY-AHEAD BUG (#110):** A character appearing soaked or wounded in Clip 1 before the rain or fight happens in Clip 2.
- **CHRONOLOGICAL STATE CEILING:** For any clip $N$, the prompt MUST ONLY copy State IDs ($SID$) whose cause event occurred at or before clip $N$ ($t_{\text{cause}} \le N$).
- **MANDATORY VERIFICATION READ-BACK:**
  > *"Klip 2 memuat Silas State A (Pristine). Klip 3 memuat Silas State B (Lacerated), yang dipicu oleh benturan kaca di Klip 2 detik 08.5s."*

---

## §BA-CHAIN — RATCHET PROGRESSION & PRESERVATION
- **PROGRESSIVE EDITING:** Each subsequent asset sheet (State B, State C) is edited directly from the previous state image, never from State A baseline.
- **MONOTONIC DECAY (§BA-PATH):** Damage accumulates in one direction ($A \rightarrow B \rightarrow C$). Wounds scab and scar; they never magically disappear without an explicit medical treatment event.
- **HEADLESS PANEL 1 PRESERVATION (Mandate 7):** When editing State B damage sheets, **Panel 1 MUST REMAIN 100% HEADLESS AND HAIRLESS** (`'PRESERVE STRICTLY HEADLESS & HAIRLESS STATUS ON PANEL 1'`).

---

## §F-CENSUS & §F-CENSUS RECONCILE — 3-WAY EQUALITY PARITY
At Turn 4 (Asset Specifications), the agent systematically walks all 10 asset categories:
1. People (Named Hero Cast)
2. Animals / Creatures
3. Vehicles / Transports
4. Tactical Handled Props
5. Rooms / Environments (1 EnvSheet per distinct room)
6. Screens / Photos / Documents
7. On-Screen Text / Logos
8. Wardrobe Variants
9. Progressive State Variants (State B / C)
10. Crowd / Extras Mass

### 📊 THE THREE-WAY EQUALITY ASSERTION:
After generating all asset sheet prompts, the agent MUST perform a line-by-line count verification and state:
> `Delivered N sheets == census N == intake N. Match confirmed.`

---

## §G-REWRITE — LOSSLESS PRECISE REWRITE PROTOCOL
When transitioning between Text-to-Video and Multimodal Ref-to-Video mode:
1. **CONSERVE ALL BEATS & TIMESTAMPS:** 100% preservation of all prose actions, facial FACS tags, lens mm, and Kelvin values. 0% dropped beats (#103).
2. **MODE PURITY:** Use **EXACTLY ONE BINDING METHOD** per prompt — either the `@Image1..@ImageN` multimodal reference matrix OR inline descriptive character passports, **NEVER MIX BOTH** (#86).
3. **DIFF PROOF:** Confirm mathematically that only identity tags were bound without shifting scene timing.

---

## §CROWD-MASS — CROWD TEXTURE COLLAPSE (ANTI-OVERLOAD LAW)
In crowded scenes with $6+$ people:
1. **HEROES GET SHEETS; CROWD GETS TEXTURE:** Hero characters get individual 4-panel sheets and precise anchors (`§BG-CAST`). The background crowd is collapsed into **1 SINGLE UNTRACKED ROW** in the ledger.
2. **PROMPT DECLARATION:**
   ```text
   CROWD MASS (1 Entity, Untracked Texture):
   Exactly 6 background patrons, generic attire, depth-of-field blur.
   IDENTITY: Unlocked (faces may drift across cuts).
   MOTION: Collective ambient café murmur, sipping coffee, reading.
   BANNED: 0% staring into camera lens, 0% abrupt wandering.
   ```
3. This prevents diffusion cross-attention overload and keeps hero faces 100% stable (#116).
