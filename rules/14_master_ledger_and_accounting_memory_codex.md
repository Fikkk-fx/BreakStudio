---
name: master-ledger-and-accounting-memory-codex
description: "Accounting-grade single project memory, four core registers (entity, state, event/cause, asset sheets), 7-point turn checksum reconciliation, and snapshot-not-pointer prompt self-containment."
---

# 📊 14. MASTER LEDGER & ACCOUNTING MEMORY CODEX (CRADLE-TO-GRAVE SSOT)

## §ML-0 — THE PHILOSOPHY OF MEMORYLESS AI
Diffusion & DiT video models have zero internal memory; every single clip is generated from absolute zero. This codex establishes the **MASTER PROJECT LEDGER** as the ONE single source of truth (SSOT) that remembers everything from the user's initial intake words to the final generated frame. Everything else (prompts, asset sheets, binding matrices, continuity tags) is a direct, strict **DERIVATIVE** of this ledger.

If a prompt, sheet, or script ever disagrees with the master ledger, **THE MASTER LEDGER WINS UNCONDITIONALLY** (§D-PRECEDENCE).

---

## §ML-1 — LIFECYCLE: WHEN IT'S BORN & WHO FEEDS IT
1. **BORN AT TURN 1 (INTAKE):** Initialized directly from the user's raw prompt via `§AT-INTAKE`.
2. **SEEDED WITH MASTER ENTITIES:** Every person (including implied actors), animal, vehicle, room/location, tactical prop, and future damage state is recorded with strict numeric counts. Vague counts require an immediate clarification question (0% silent assumption).
3. **READ & WRITE AT EVERY TURN:**
   - **Turn 1 (Intake):** Seeds Table A & Table B baseline.
   - **Turn 3 (Screenplay):** Verifies all active characters and props appear in the scene.
   - **Turn 4 (Asset Sheets):** Populates Table D (Asset Sheets) directly from Table B SIDs that passed the `§BA-DECIDE` gate.
   - **Turn 5 (Master Video Prompts):** Every clip inlines current Table B state values as a full self-contained snapshot.
   - **Turn 6 / T5 (Ground Truth Audit):** Reconciles real generated video frames back into Table B/C (`§D-GROUNDTRUTH`).

---

## §ML-2 — THE FOUR CORE REGISTERS (THE COMPLETE PROJECT MEMORY)

### 📋 TABLE A: ENTITY REGISTER (Master Physical Count)
Every distinct entity the viewer can visually identify on screen:
| EID | Category | Name / Role | First Appears (Clip) | Last Appears (Clip) | # States | Anchor (Position + Trait) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `E01` | PEOPLE | SILAS (Antagonist) | Clip 1 | Clip 4 | 2 | `SILAS (frame-right, charcoal trench coat)` | 185cm, athletic |
| `E02` | PEOPLE | MAYA (Protagonist) | Clip 1 | Clip 4 | 3 | `MAYA (frame-left, navy utility jacket)` | 168cm, scar on brow |
| `E03` | PROPS | CERAMIC MUG | Clip 1 | Clip 2 | 2 | `CERAMIC MUG (on mahogany desk, 0.4m from Silas)` | Matte beige stoneware |
| `E04` | CROWD | BYSTANDER MASS | Clip 2 | Clip 2 | 1 | `BYSTANDER MASS (background street, east wall)` | Exactly 4 static pedestrians |

> [!IMPORTANT]
> **THE CROWD MASS RULE (§CROWD-MASS / Table A):**
> A crowd mass is counted as **EXACTLY 1 LEDGER ROW** regardless of headcount. The master count reads `"N HEROES + 1 CROWD-MASS"`, never individual headcounts. `§F-CENSUS RECONCILE` skips crowd masses to focus asset sheets on hero characters.

---

### 🔄 TABLE B: STATE REGISTER (Chronological Evolution Matrix)
Tracks every distinct physical version of every entity across runtime:
| SID | EID | State Label | Value (Strict Metric / Units) | Starts At (Clip.Xs) | Cause (→ Table C Event) | Persists? | Sheet # (Table D) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `S01-A` | `E01` | Silas Pristine | Clean charcoal coat, 0% dirt, 0% blood | Clip 1 (0.0s) | Baseline | L4 (Perm) | Sheet 1 |
| `S01-B` | `E01` | Silas Lacerated | 4cm horizontal laceration left jawline, Tier 2 | Clip 3 (4.2s) | `EV-03` Glass shard impact | L3 (Persist) | Sheet 2 |
| `S02-A` | `E02` | Maya Dry | Dry navy jacket, matte hair | Clip 1 (0.0s) | Baseline | L4 (Perm) | Sheet 3 |
| `S02-B` | `E02` | Maya Soaked | 85% water saturation on jacket shoulders & hair | Clip 2 (1.0s) | `EV-01` Heavy rainstorm | L2 (Persist) | Sheet 4 |

- **Strict Unit Standard (§D-UNIT):** Values MUST use metric measurements (`cm`, `%`, `count`, `Kelvin`, `Damage Tier 1–4`), never qualitative adjectives (`"slightly wet"`, `"a bit bloody"`).
- **Monotonic One-Way Evolution (§BA-PATH):** A damaged state cannot jump back to a cleaner state without an explicit documented erase/cleanse event row.

---

### 💥 TABLE C: EVENT / CAUSE LEDGER (Temporal Causality Engine)
Every change in Table B must trace to an exact causal trigger:
| Event ID | Clip # | Timestamp | Physical Action / Cause Event | Affects EID / SID | Direct Physical Consequence | Proportionality Tier (§AL-PROP) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EV-01` | Clip 2 | 0.0s–3.0s | Unsheltered heavy downpour (30mm/hr) | `E02` → `S02-B` | 85% fabric moisture saturation | Tier 1 (Surface Wetting) |
| `EV-02` | Clip 2 | 8.5s | Silas delivers right cross to jaw | `E02` → `S02-C` | 0.5s head recoil + 2cm dermal bruise | Tier 2 (Surface Laceration) |
| `EV-03` | Clip 3 | 4.2s | Shattered window projectile grazing jaw | `E01` → `S01-B` | 4cm linear laceration, active trickle | Tier 2 (Surface Laceration) |

- **Zero-Uncaused Change Law (§BA-CAUSE):** If an entity changes appearance without a matching Event row in Table C, the state change is strictly invalid.
- **Off-Screen Cause Requirement (§BA-OFFSCREEN):** Changes between scenes/timeskips must be explicitly tagged `OFF-SCREEN CAUSE: [Timeskip +2 hours / treated with bandage]`.

---

### 🖼️ TABLE D: ASSET SHEET REGISTER (Production Deliverables)
Maps directly to the final image assets delivered to the user:
| Sheet # | EID / SID Depicted | Asset Sheet Type | Style Mode | Model Generator | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sheet 1 | `E01` / `S01-A` | 4-Panel Raw UGC (#FFFFFF, P1 Headless) | Live-Action Cinema | `openai/gpt-image-2` | Built |
| Sheet 2 | `E01` / `S01-B` | 4-Panel Raw UGC (State B Damaged) | Live-Action Cinema | `openai/gpt-image-2` | Built |
| Sheet 3 | `E02` / `S02-A` | 4-Panel Raw UGC (#FFFFFF, P1 Headless) | Live-Action Cinema | `openai/gpt-image-2` | Built |
| Sheet 4 | `E02` / `S02-B` | 4-Panel Raw UGC (State B Soaked) | Live-Action Cinema | `openai/gpt-image-2` | Built |
| Sheet 5 | `E05` / `S05-A` | Cinematic Set (Empty, 16:9, 0% Humans) | Live-Action Cinema | `openai/gpt-image-2` | Built |

---

## §ML-3 — THE 7-POINT TURN CHECKSUM
Every delivery turn MUST verify and state the following equalities:
1. **INTAKE == TABLE A:** Every entity extracted at `§AT-INTAKE` has an explicit row in Table A.
2. **PROMPTS ⊇ TABLE A:** Every Table A entity is established in the prompt's prose blocks (`§D-INTAKE-MATCH`).
3. **TABLE B ↔ TABLE C:** Every state row has a matching cause event; every event produces a defined state.
4. **TABLE B (Sheet=Yes) == TABLE D:** Sheets needed equals sheets numbered and delivered (`§F-CENSUS RECONCILE`).
5. **THREE-WAY INTEGER PARITY:** `Intake Count N == Census Rows Needing Sheets == Delivered Sheets N`.
6. **LEDGER == SHEETS NUMERICALLY:** Every measurement on asset sheets exactly matches Table B numeric specs (`§D-SYNC`).
7. **SNAPSHOT INTEGRITY:** Every prompt inlines its clip's full state values with 0% pointer phrases (`§ML-6`).

**MANDATORY CHECKSUM LINE (Turn 4 & Turn 5):**
> `Ledger check: intake N == entities N == sheets-needed N == delivered N. All numbers match.`

---

## §ML-6 — SNAPSHOT NOT POINTER LAW (THE HARDWARE ISOLATION MANDATE)
Video diffusion models evaluate prompt tokens in total isolation per clip. Therefore:
1. **0% CROSS-CLIP POINTERS:** Forbidden phrases inside any prompt:
   - ❌ `"as in clip 1"`
   - ❌ `"same wound as before"`
   - ❌ `"carry State B"`
   - ❌ `"unchanged from previous shot"`
   - ❌ `"refer to @Image1 from earlier"`
2. **FULL NUMERIC RE-STATEMENT:** Every carried state MUST be written out in full metric detail in EVERY clip:
   - ✅ `"Silas has a 4cm horizontal laceration along left jawline with coagulated dark red blood line and 15% fabric fraying on left coat lapel."`
3. **LEDGER RESIDES OUTSIDE MODEL TEXT:** The 4 ledger tables, EID/SID codes, and checksum lines belong in directorial planning, NOT inside the copyable video prompt text pasted into the AI video generator.
