---
name: multi-room-and-object-spatial-logic-codex
description: "Object logic architecture, multi-room house films, doorway handoffs, lighting fixture clearance rules, per-cut coordinate restatement, and screen device air-gaps."
---

# 🏛️ 18. MULTI-ROOM & OBJECT SPATIAL LOGIC CODEX

## §D-ROOMLOCK — OBJECT LOGIC ARCHITECTURE (5 PILLARS)
Every built environment, room, vehicle, weapon, machine, and prop obeys physical architectural logic. A scene cannot simply be "drawn"; it must exist in a functionally coherent 3D coordinate space.

### 🏛️ THE 5 PILLARS OF OBJECT LOGIC:
1. **HUMAN-SCALE ANCHOR:**
   - Every physical element is scaled against standard human biometrics:
     - Standard door: $\approx 2.1\text{m}$ high ($1\text{ head}$ taller than standing adult).
     - Standard ceiling: $2.6\text{m}$–$3.2\text{m}$ high.
     - Dining chair: $\approx 45\text{cm}$ seat height (knee level).
     - Car roof: Head height when seated inside.
     - Blade / Weapon: Forearm length ($30\text{cm}$–$45\text{cm}$).
   - **0% GIGANTIC / SHRUNK PROPS:** Forbids randomly oversized cups, doors, or furniture (#117).
2. **FUNCTIONAL PART PLACEMENT:**
   - Every part sits where its human operability requires:
     - Vehicle steering wheel: Front driver side, directly ahead of instrument cluster.
     - Door handles: Exterior latch edge, $95\text{cm}$–$105\text{cm}$ from floor (never in door center).
     - Windows: Outer wall perimeter facing open exterior.
   - Parts in functionally impossible locations are strictly rejected.
3. **LOGICAL ORIENTATION LOCK:**
   - Openings and lenses face meaningful physical spaces:
     - Windows look OUT into the environment.
     - Muzzle of a firearm points away from the operator.
     - Screens face the viewer/operator.
4. **CIRCULATION & OPERABILITY FLOW:**
   - Architectural routes must be reachable: Door $\rightarrow$ Corridor $\rightarrow$ Room $\rightarrow$ Furniture.
   - Stairs land on an authentic floor slab; elevators align with floor landings.
5. **LIGHT SOURCES & FIXTURE MOUNTING CLEARANCE (§LIGHT-CLEARANCE):**
   - Light originates exclusively from named, visible physical fixtures (fluorescent tubes, tungsten pendants, windows, vehicle headlamps).
   - **CEILING FIXTURE CLEARANCE LAW (§LIGHT-CLEARANCE / #122):**
     - Overhead/pendant lamps MUST be anchored to ceiling architecture at standard ceiling height ($2.5\text{m}$–$3.0\text{m}$), maintaining $\ge 60\text{cm}$–$100\text{cm}$ vertical clearance above a standing person's head.
     - **SEPARATE FIXTURE MOUNT FROM DOWNWARD BEAM CONE:** Do NOT write *"lamp hovering above his head"* (this causes diffusion models to draw a physical bulb floating inches from his scalp). Instead write: *"Ceiling-mounted industrial pendant fixture 2.8m high casts a conical downward pool of 3200K light onto the floor."*
     - **MOTIVATED LOW-FIXTURE TAG:** A low-hanging fixture (within $50\text{cm}$ of a human) is permitted ONLY with an explicit tag: `LOW-FIXTURE CAUSE: [interrogation desk task lamp / 1.9m low basement ceiling / seated dining table pendant]`. Without this tag, hovering lamps are strictly invalid.

---

## §D-ROOMLOCK-MULTI — LONG MULTI-ROOM HOUSE FILMS
In multi-room narrative films (e.g. 2–5 minute films spanning living rooms, hallways, bedrooms, and basements):

1. **SEPARATE PERSISTENCE FOR ROOMS & CHARACTERS:**
   - **Character State Persists per Person:** A character whose clothes get soaked in the garden remains soaked when walking into the library.
   - **Room State Persists per Room:** If a glass shatters on the kitchen floor in Clip 1, the kitchen floor remains shattered and messy when characters re-enter in Clip 5 (`§D-GROUNDTRUTH` saved-state ref).
2. **DOORWAY COORDINATE HANDOFF:**
   - Leaving Room A through the East Doorway ($X=4.0\text{m}, Y=0.0\text{m}$) requires the opening frame of Room B to begin at the West Doorway threshold with matching body momentum and facing.
3. **ADJACENCY MAP:**
   - Every multi-room project establishes a fixed floorplan adjacency map:
     > `Living Room [East Door] <---> [West Door] Hallway [North Door] <---> [South Door] Study Room.`

---

## §D-CUTLOCK — PER-CUT WORLD & SCREEN RESTATEMENT
Because video diffusion models experience complete spatial amnesia at every hard cut:
1. **WORLD POSITION = ANCHOR, SCREEN SIDE = DERIVED:**
   - Entities are anchored to fixed world cardinal coordinates (e.g. `SILAS at North Wall`, `MAYA at South Desk`).
2. **MANDATORY RESTATEMENT PER CUT:**
   - Immediately following every `[HARD CUT]`, restate each entity's world position AND its resulting screen side for the new camera angle:
   ```text
   [HARD CUT: 04.2s | Reverse Over-The-Shoulder from South Wall | MAYA world=South-Desk -> now SCREEN-RIGHT; SILAS world=North-Wall -> now SCREEN-LEFT]
   ```
3. **REVERSE ANGLE MIRRORING LAW:**
   - In a 180° reverse cut, screen sides mirror naturally while world coordinates remain strictly identical. This prevents accidental axis flips (#111).

---

## §BG-SCREEN — DEVICE & SCREEN AIR-GAP (ANTI-MIRROR / ANTI-LEAK)
When a character interacts with a smartphone, tablet, monitor, printed photograph, or map:
1. **METHOD A (Over-The-Shoulder):** Camera positioned behind shoulder looking down at the screen surface; screen text is upright and readable ($0\%$ upside down).
2. **METHOD B (Top-Down Macro Insert):** 90° top-down macro shot of the device held flat in hands.
3. **THE DEVICE AIR-GAP MANDATE (#49):**
   - During macro screen/insert shots, the prose and acting descriptions MUST contain **0% facial or person descriptors**. This eliminates the diffusion bug where the character's face is drawn reflected or embedded inside the screen graphics!
