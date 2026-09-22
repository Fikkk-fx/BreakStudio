import subprocess
import json

test_prompt = """FORMAT: Single continuous 30-second one-take street UGC documentary sequence
ASPECT RATIO: 9:16 vertical (social mobile native)
FRAME RATE: 30fps, 180° rotary shutter (1/60s natural motion blur)
SENSOR: iPhone 16 Pro Max 24mm ProRes Log handheld emulation | ISO 500 | 14-stop dynamic range
COLOR GRADE: PAL-UGC-01 Raw Street Realism — 55% wet slate gray base, 25% muted navy and olive secondary, 15% burnt amber terrace accent, 5% overcast skylight highlight, natural skin tones, soft contrast, natural shadow toe roll-off

LOCATION — ENV_ID [STREET_STADIUM_APPROACH]: Brick-walled industrial alleyway leading toward monumental concrete stadium plaza, 16:45 overcast late afternoon, cool 5200K diffused daylight. Wet asphalt pavement with reflective puddle patches and cast-iron manhole covers. Left boundary: red Victorian brick facade and green wooden pub door. Right boundary: rusted corrugated steel fence and concrete lampposts. Background depth elements: towering concrete stadium floodlight pylons piercing the grey sky. Strict Crowd Quota: Exactly 6 distant background football supporters in dark coats walking toward stadium (0% static crowd, 0% morphing).

GLOBAL CHARACTER LOCK — CALLUM: 29yo British-Celtic terrace casual supporter, burly stocky robust build, 182cm, broad shoulders, weathered masculine facial contour, short textured taper crop dark hair, subtle 2-day beard stubble, observant slate-blue eyes with specular catchlights, natural skin micro-pores and cold-air cheek flushing.
OUTFIT: Deep navy technical micro-ripstop nylon hooded windbreaker with stand-up storm collar, metallic front zip, dual zip chest pockets, layered over crisp olive-drab cotton pique polo shirt; relaxed straight-leg dark indigo raw selvedge denim trousers with clean single cuff break; vintage navy suede low-top terrace sneakers with off-white leather stripes and gum rubber soles.
PROPS: Stainless steel sports chronograph watch on left wrist; silver signet ring on right pinky finger; box of matches in left jacket pocket.
FRAMING DIRECTIVE: Dynamic handheld eye-level and chest-level mobile framing; strictly no tripod or cinematic gimbal stabilization.

LIGHTING: Key — Cool diffused overcast skylight at 5200K from high top-left. Fill — Soft ambient bounce off wet asphalt and red brick walls at 1:2.5 ratio. Rim — Subtle cool atmospheric separation along shoulders from stadium floodlight glow. Technique: Natural raw overcast daylight with realistic smartphone auto-exposure micro-adjustments.

CAMERA RIG: Handheld smartphone camera rig with organic operator physics: 1.0x real-time Newtonian velocity, subtle 8-12Hz micro-shake, slight framing drift, organic 1-2 degree canted angle variance, and natural autofocus breathing. Strictly zero gimbal stabilization, zero tripod stability, zero cinematic dolly track movement.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SHOT 1 [0.0s → 4.0s]
Lens: 24mm f/2.2 | Focus: 1.5m
FRAMING: Medium shot, handheld camera facing Callum leaning against red brick pub wall, watching street corner.
CHARACTER LOCK: CALLUM (exact: navy technical windbreaker, olive polo, raw denim, suede gum-sole sneakers). Callum shifts weight between boots, checking his stainless steel wristwatch on left wrist, exhaling visible breath vapor into chilly air, observing empty cross-street. Background: damp alleyway, puddles reflecting grey sky.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 4.0s | REFRAME]

SHOT 2 [4.0s → 6.0s]
Lens: 28mm f/2.2 | Focus: 1.2m
FRAMING: Two-shot medium framing, handheld operator stepping backward slightly as second burly mate enters frame right.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, raw denim). Callum steps forward from wall, clasping hands firmly in traditional terrace grip with incoming stocky friend in olive Harrington jacket, exchanging respectful head nods.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 6.0s | REFRAME]

SHOT 3 [6.0s → 8.0s]
Lens: 35mm f/2.0 | Focus: 1.0m
FRAMING: Over-the-shoulder medium-close framing on third crew member stepping into group circle.
CHARACTER LOCK: CALLUM (exact: navy windbreaker). Third stocky mate in stone-grey hooded jacket strikes disposable flint lighter with sharp flick, cupping flame against wind to ignite cigarette, drifting wisps of grey tobacco smoke past Callum's shoulder.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 8.0s | REFRAME]

SHOT 4 [8.0s → 10.0s]
Lens: 24mm f/2.2 | Focus: 1.8m
FRAMING: Group establishing wide-medium shot capturing all four burly companions assembled on street corner.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, raw denim, suede sneakers). The four stocky men form a tight unit outside pub corner, pulling up high neck zips and adjusting jacket cuffs, unified collective readiness before setting off.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 10.0s | REFRAME]

SHOT 5 [10.0s → 12.0s]
Lens: 24mm f/2.2 | Focus: 2.0m
FRAMING: Low-angle tracking shot moving backward ahead of group as they walk shoulder-to-shoulder along wet tarmac.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, raw denim). Group strides with synchronized heavy cadence; Callum occupies center-left, hands thrust into jacket slash pockets, eyes locked forward toward distant stadium floodlights.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 12.0s | REFRAME]

SHOT 6 [12.0s → 14.0s]
Lens: 50mm f/1.8 | Focus: 0.8m
FRAMING: Close-up tracking profile on Callum's technical jacket torso in motion.
CHARACTER LOCK: CALLUM (exact: navy technical windbreaker). Handheld camera tracks beside Callum's chest, capturing tactile micro-ripstop crinkle nylon fabric, heavy molded zipper teeth, and woven utility chest pocket seam details as fabric shifts with his gait.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 14.0s | REFRAME]

SHOT 7 [14.0s → 16.0s]
Lens: 35mm f/2.2 | Focus: 0.9m
FRAMING: Low-angle ground-skimming tracking shot focusing down at marching footwear on wet asphalt.
CHARACTER LOCK: CALLUM (exact: suede gum-sole sneakers, raw denim cuff). Callum's navy suede gum-sole trainers step firmly across asphalt edge and splash through shallow puddle water, followed closely by companions' leather terrace boots.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 16.0s | REFRAME]

SHOT 8 [16.0s → 18.0s]
Lens: 24mm f/2.2 | Focus: 2.2m
FRAMING: Medium frontal group tracking shot at eye level, operator walking backward at steady speed.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, olive polo, raw denim). All four men walk four-abreast in purposeful march, burly broad shoulders filling the vertical 9:16 mobile frame, breath mist forming in cool air.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 18.0s | REFRAME]

SHOT 9 [18.0s → 20.0s]
Lens: 50mm f/1.8 | Focus: 0.7m
FRAMING: Tight detail close-up on jacket collar fastening.
CHARACTER LOCK: CALLUM (exact: navy windbreaker). Callum raises his right hand, gripped with silver signet ring, grasping metal zipper puller and fastening storm collar all the way up to chin level, fabric stretching taut across muscular neck.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 20.0s | REFRAME]

SHOT 10 [20.0s → 22.0s]
Lens: 35mm f/2.0 | Focus: 1.4m
FRAMING: Over-the-shoulder rear tracking shot following behind Callum's back.
CHARACTER LOCK: CALLUM (exact: navy windbreaker back yoke, raw denim). Camera captures ergonomic storm-flap back construction of navy jacket, structured taper cut of raw denim, and relaxed rolling gait of a seasoned matchday regular.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 22.0s | REFRAME]

SHOT 11 [22.0s → 24.0s]
Lens: 24mm f/2.2 | Focus: 3.0m
FRAMING: Wide dynamic tracking shot as group turns corner into stadium approach boulevard.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, raw denim). Massive concrete stadium grandstand and luminous 60-meter floodlight towers emerge into view, casting soft high-angle spill across wet tarmac.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 24.0s | REFRAME]

SHOT 12 [24.0s → 25.5s]
Lens: 40mm f/2.0 | Focus: 1.1m
FRAMING: Medium-close side profile tracking shot showcasing inner layered garment.
CHARACTER LOCK: CALLUM (exact: navy windbreaker unzipped two inches showing olive polo collar). Side angle highlights crisp ribbed collar of olive cotton polo snug beneath windbreaker neck, jawline firm and determined.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 25.5s | REFRAME]

SHOT 13 [25.5s → 27.0s]
Lens: 24mm f/2.2 | Focus: 2.5m
FRAMING: Handheld follow shot behind group navigating through yellow crowd-control steel crash barriers.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, raw denim, suede sneakers). Callum guides his path past steel barricade, companions falling into single-file entry formation outside turnstile plaza.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 27.0s | REFRAME]

SHOT 14 [27.0s → 28.5s]
Lens: 28mm f/2.2 | Focus: 1.2m
FRAMING: Over-the-shoulder close follow shot tracking Callum reaching the turnstile gate.
CHARACTER LOCK: CALLUM (exact: navy windbreaker, signet ring on right hand). Callum extends right hand to push revolving steel bar of mechanical stadium turnstile, stepping into narrow concrete concourse portal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HARD CUT: 28.5s | REFRAME]

SHOT 15 [28.5s → 30.0s]
Lens: 24mm f/2.2 | Focus: 2.0m
FRAMING: Medium follow shot from rear-quarter inside dark concourse archway, revealing emerald green illuminated pitch ahead.
CHARACTER LOCK: CALLUM (exact: navy technical windbreaker, raw denim, suede sneakers). Callum pushes through turnstile exit into shadowed tunnel, footsteps ringing out, gazing toward bright green grass and roaring matchday arena; settle stance locked from 29.2s to 30.0s, holding stance while looking forward into stadium bowl as final visual hold.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUDIO: 100% diegetic street and matchday acoustic landscape without voiceover or non-diegetic music bed.
Volume Hierarchy: Environmental matchday ambience at 0dB reference, foley transient peaks at -2dB to 0dB.
Foley layers:
[1] Heavy synchronized rubber-sole footwear scuffs and wet asphalt splashes across pavement.
[2] Crisp synthetic friction and technical crinkle-nylon rustle of windbreakers during brisk walking.
[3] Mechanical metallic click of disposable lighter spark and metal zipper puller slide.
[4] Metallic clanking and ratchet rotation sound of heavy steel turnstile barrier bars at 27.5s-28.5s.
[5] Distant reverberant stadium terrace singing, sub-bass terrace drums, and low crowd roar echoing between brick facades (RT60 1.2s wet outdoor street decay transitioning to RT60 0.6s concrete concourse).
Acoustics: Raw mobile microphone capture with 80Hz high-pass filter, natural wind-muff flutter, and authentic ambient street stereo separation.
"""

with open("test_prompt.txt", "w", encoding="utf-8") as f:
    f.write(test_prompt)

res = subprocess.run(["python", "prompt_auditor.py", "test_prompt.txt", "--duration", "30", "--mode", "3", "--json"], capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
