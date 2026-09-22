import subprocess
import json

prompt_mode3 = """FORMAT: Single continuous 15-second mobile UGC fashion documentary sequence
ASPECT RATIO: 16:9 widescreen landscape
FRAME RATE: 24fps, 180° rotary shutter (1/48s natural motion blur)
SENSOR: iPhone 16 Pro Max 24mm ProRes Log handheld emulation | ISO 400 | 14-stop dynamic range
COLOR GRADE: PAL-UGC-01 Raw Stadium Realism — 50% concrete brutalist grey, 25% emerald pitch green spill, 15% saturated retro team kit primaries, 10% diffuse daylight highlight, authentic warm skin tones, natural shadow toe roll-off

LOCATION — ENV_ID [STADIUM_TUNNEL_APPROACH]: Monumental concrete stadium tunnel concourse opening out toward the sunlit grass pitch. Late afternoon 16:30 overcast sunbeams cutting through high stadium archways at 5400K daylight. Raw exposed ribbed concrete columns, damp tarmac walkways with subtle reflective patches. Right boundary: industrial steel mesh gates. Left boundary: polished yellow safety handrails. Background depth elements: distant green stadium pitch grass and towering tiered stadium grandstands under floodlight pylons. Strict Crowd Quota: Exactly 4 distant background groundkeepers in neon bibs standing stationary beside sideline barriers (0% morphing).

GLOBAL CHARACTER LOCK — ENSEMBLE: Five distinct stylish young women (Asian and European heritage) wearing authentic 1990s retro football jerseys styled into modern high-street terrace fashion:
1. Maya (22yo East Asian, Indonesian heritage): 165cm, sleek shoulder-length black bob hair, sharp jawline, wearing 1996 geometric jacquard emerald-green team jersey with white ribbed V-neck collar, embroidered crest on left chest, high-waisted raw indigo denim trousers.
2. Chloe (23yo European, French heritage): 172cm, wavy tousled honey-blonde hair in messy top-knot, athletic frame, wearing 1988 tricolor cobalt-blue jersey with bold red and white chest horizontal bands, vintage flock sponsor lettering, paired with black pleated tennis skirt.
3. Hana (21yo East Asian, Japanese heritage): 163cm, cropped dark brown pixie cut, wearing 1994 monochrome black-and-white vertical striped retro jersey with retro polo collar, relaxed beige cargo pants with utility straps.
4. Elena (24yo European, Italian heritage): 175cm, olive complexion, slicked-back dark ponytail, sculpted cheekbones, wearing 1990 azure-blue vintage team kit featuring tonal diamond watermarks and gold bullion thread badge, dark navy track pants with retro side-striping.
5. Sarah (22yo European, British heritage): 168cm, light freckled fair skin, auburn shoulder-length layered curls, wearing 1998 claret-and-sky quartered football jersey with retro white script flocking, vintage track shorts and white athletic crew socks.
PROPS: Maya carries vintage metallic sports sunglasses perched atop head; Chloe wears stainless steel chain wristwatch.
FRAMING DIRECTIVE: Dynamic eye-level handheld smartphone framing along 180-degree spatial axis; strictly no tripod or mechanical gimbal stabilization.

LIGHTING: Key — Natural afternoon daylight at 5400K pouring through stadium archway from top-left. Fill — Soft ambient bounce from concrete walls and floor at 1:2.8 ratio. Rim — Soft daylight halo separating shoulder silhouettes from darker concrete background.
CAMERA RIG: Biomechanical handheld smartphone camera rig operating with 1.0x real-time Newtonian velocity, organic 8-12Hz micro-shake, subtle framing drift, 1-2 degree canted angle variance, and natural autofocus breathing.

**[PROSE]:**
At 0.0s [24mm Prime lens, f/2.2, focus 2.5m, eye level]: Handheld camera faces backward as the five-woman ensemble (Maya, Chloe, Hana, Elena, and Sarah) bursts into the concrete tunnel entrance. They walk with uncoordinated raw energy, candidly bantering, laughing with spontaneous zygomatic AU12 smiles and AU6 eye crinkles, walking haphazardly past each other without uniform formation, authentic raw street presence.

[HARD CUT: 2.0s | REFRAME]
At 2.0s [28mm Prime lens, f/2.0, focus 1.8m, medium three-quarter tracking]: Handheld operator steps backward into stadium light, revealing the vibrant vintage team kits in full view. Maya in emerald jersey and Chloe in cobalt tricolor kit stride forward side-by-side, proudly displaying their retro embroidered club crests, while Elena and Hana step alongside, sunlight catching the glossy polyester jacquard sheen.

[HARD CUT: 6.0s | REFRAME]
At 6.0s [50mm Prime lens, f/1.8, focus 0.7m, close chest detail]: Close handheld tracking on Maya's emerald-green retro kit. Maya reaches up with left hand, tugging the crisp white ribbed V-neck collar, showcasing the tactile tactile micro-mesh weave and dense gold bullion embroidery of the vintage team crest catching specular highlights.

[HARD CUT: 8.0s | REFRAME]
At 8.0s [50mm Prime lens, f/1.8, focus 0.65m, over-shoulder close detail]: Handheld angle swings behind Chloe's back as she spins playfully. The camera focuses on the velvety raised flock typography and retro squad number printed across the royal blue fabric, feeling the authentic tactile fuzz and vintage stitching along the shoulder seams.

[HARD CUT: 10.0s | REFRAME]
At 10.0s [40mm Prime lens, f/2.0, focus 0.8m, dynamic low-angle torso close-up]: Handheld camera drops slightly to waist level, capturing Hana's monochrome striped kit tucked effortlessly into utilitarian cargo pants, and Sarah adjusting the claret-and-sky contrast rib sleeve cuff with right fingers, displaying the lustrous retro knit texture.

[HARD CUT: 11.5s | REFRAME]
At 11.5s [35mm Prime lens, f/2.0, focus 0.9m, dynamic medium profile]: Handheld operator circles briskly around Elena as she gestures toward the illuminated stadium bowl. The camera captures the tonal diamond watermark patterns embedded into her azure-blue fabric shifting under direct natural sunlight.

[HARD CUT: 13.0s | REFRAME]
At 13.0s [24mm Prime lens, f/2.2, focus 2.2m, wide group composition]: Handheld camera steps back to capture Maya, Chloe, Hana, Elena, and Sarah assembled shoulder-to-shoulder in one cohesive wide frame at the tunnel threshold. The vast green pitch and empty grandstands expand behind them. They halt together into confident editorial poses, smiling naturally with subtle head tilts; locked settle stance held firmly from 14.2s to 15.0s with closed lips, steady posture, and natural chest breathing into final visual hold.

**[CAMERA & PHYSICS LOCK]:**
Handheld smartphone CMOS physics operating under 1.0x real-time Newtonian velocity. Continuous 8-12Hz micro-tremor, natural PDAF autofocus breathing, and subtle greasy lens halation. Eye-level mobile framing respecting 180-degree spatial axis.

**[RENDER & ACTING LOCK]:**
Authentic UGC fashion energy. Natural micro-expressions with zygomatic AU12 and orbicularis AU6 smile crinkles. Skin micro-texture with genuine pores and natural daylight highlights.

**[SPATIAL ACOUSTICS & DIEGETIC AUDIO]:**
Acoustic profile: Rhythmic football beat soundtrack perfectly synchronized with the visuals from 0.0s to 15.0s without voiceover.
Music Bed: Driving 128 BPM energetic football breakbeat with heavy kick transients, syncopated snare snaps, and rolling 808 sub-bass groove driving the visual momentum.
Diegetic Foley layers:
[1] Rubber sole sneakers squeaking and scuffing rhythmically against polished concrete floor.
[2] Crisp synthetic friction and whisper rustle of retro polyester jersey fabrics during movement.
[3] Distant reverberant stadium concourse acoustic decay (RT60 1.5s) with subtle ambient pre-match terrace murmur.
Acoustics: Raw mobile microphone capture with 80Hz high-pass filter, natural wind muffling, and transient clarity.
"""

with open("scratch/test_prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt_mode3.strip())

import prompt_auditor
res = prompt_auditor.audit_turn5_prompt(prompt_mode3.strip(), clip_duration=15.0, selected_mode=3)
print(json.dumps(res, indent=2))
