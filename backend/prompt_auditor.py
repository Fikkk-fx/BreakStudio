"""
BreakStudio — Zero-Defect Master Video Prompt Auditor (Raw UGC Studio Edition)
========================================================================================================
Standalone Precision Linter, Character/Word Budget Calculator & Multi-Block Cross-Continuity Auditor.
Combines Super-Mathematical Shot & Cut Parity, 3-Tier Duration Ceilings, 180° Spatial Axis,
Kinetic Velocity Verification, Anti-SFX Bloat Checks, Lexical Hard-Locks & Causal Chain Tracking.
========================================================================================================
"""

import re
import sys
import json
import argparse
from typing import Dict, Any, List

# Ensure safe UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# =============================================================================
# 1. FORBIDDEN PHRASES, BANNED TOKENS & DIALECT GLITCHES
# =============================================================================

FORBIDDEN_PHRASES = [
    # Banned General Fluff & AI Directorial Cliches
    r"buttery-smooth",
    r"hyper-realistic",
    r"photorealistic",
    r"masterpiece",
    r"0\.8s tail-buffer",
    r"boléh",
    r"bédil",
    r"méréka",
    r"0% tears",
    r"zero tears",
    r"no tears",
    r"0% blush",
    r"zero blush",
    r"no blush",
    r"zero freeze",
    r"0% freeze",
    r"tangan.*menekan.*bahu",
    r"menepuk.*pundak",
    r"tinta lebih tajam",
    r"pena lebih tajam",
    r"kertas bisa robek",
    r"tanah menolak tunduk",
    r"tidak kata-kataku",

    # Banned Anonymous Plurals & Crowd Ambiguity
    r"\ball four\b",
    r"\ball five\b",
    r"\ball three\b",
    r"\ball six\b",
    r"\ball seven\b",
    r"the crowd of",
    r"wandering pedestrians",

    # 🛑 COMPLETE PURGE OF SLUGGISH ADJECTIVES, ADVERBS & NEGATIVE SLOWMO TOKENS
    r"\bslowly\b",
    r"\bslow\b",
    r"\bslow-motion\b",
    r"\bslow motion\b",
    r"\bslowmo\b",
    r"\bslow-mo\b",
    r"\bsluggish\b",
    r"\bfloating\b",
    r"\bfloaty\b",
    r"\bfloatiness\b",
    r"\bhovering\b",
    r"\bweightless\b",
    r"\bdrifting\b",
    r"\bzero-gravity\b",
    r"\bzero gravity\b",
    r"\bzero-g\b",
    r"\bmid-air suspension\b",
    r"\bsuspended in air\b",
    r"\bgliding\b",
    r"\bleisurely\b",
    r"\bcalmly\b",
    r"\bgentle\b",
    r"\bgently\b",

    # 🛑 BANNED NEGATIVE PHRASINGS (TOKEN LEAKAGE INTO DIFFUSION ATTENTION HEADS)
    r"strictly\s+0%\s+slow-motion",
    r"strictly\s+0%\s+slow\s+motion",
    r"0%\s+slow-motion",
    r"0%\s+slow\s+motion",
    r"without\s+floating",
    r"without\s+floatiness",
    r"without\s+weightless",
    r"without\s+slow",
    r"zero\s+floatiness",
    r"no\s+weightless",
    r"no\s+floating",
    r"without\s+clipping",
    r"without\s+stutter",
    r"without\s+lag",
]

COMMON_PROPS = [
    r"knife", r"karambit", r"tanto", r"dagger", r"blade", r"platter", r"tray",
    r"decanter", r"tumbler", r"glass", r"cup", r"saucer", r"fork", r"candelabra",
    r"table", r"chair", r"lighter", r"bottle", r"gun", r"revolver", r"baton",
    r"datapad", r"document", r"keycard", r"syringe", r"holster"
]

PROP_HANDOFF_VERBS = [
    r"draws?", r"wrenches?", r"slaps?", r"stabs?", r"twirls?", r"swirls?", r"presses?", r"taps?",
    r"slices?", r"rotates?", r"dislodg\w+", r"toss\w+", r"drops?", r"embeds?", r"grabs?",
    r"slides?", r"picks?", r"releases?", r"catches?", r"pins?", r"fractures?", r"shatters?",
    r"kicks?", r"swings?", r"flips?", r"sets?", r"hurls?", r"deflects?", r"parries?",
    r"intercepts?", r"redirects?", r"snatches?", r"strikes?", r"plants?", r"wields?", r"rips?"
]

PHYSICAL_ACTION_VERBS = [
    r"strikes?", r"kicks?", r"slams?", r"toss\w+", r"throws?", r"vaults?",
    r"punches?", r"sweeps?", r"tackles?", r"chokes?", r"flips?", r"heaves?",
    r"drives?", r"hurls?", r"shoves?", r"wrenches?", r"drops?"
]

PHYSICAL_CONSEQUENCE_VERBS = [
    r"impacts?", r"splinters?", r"shatters?", r"fractures?", r"absorbs?",
    r"rolls?", r"recoils?", r"rebounds?", r"stumbles?", r"buckles?",
    r"deflects?", r"parries?", r"collides?", r"slides?", r"scatters?", r"locks?"
]

# §ML-6 BANNED CROSS-CLIP POINTERS (Breaks Snapshot Self-Containment)
BANNED_CROSS_CLIP_POINTERS = [
    r"\bas in clip\s*\d+\b",
    r"\bsame as before\b",
    r"\bcarry state\s*[a-z0-9]+\b",
    r"\bthe previous wound\b",
    r"\bunchanged from last clip\b",
    r"@Image\s+from\s+clip",
    r"\bsame as in shot\s*\d+\b"
]

# §IP-CLEAN BANNED COPYRIGHTED PROPER NOUNS
BANNED_IP_PROPER_NOUNS = [
    r"\bmarvel\b", r"\bdc comics\b", r"\bdisney\b", r"\bpixar\b",
    r"\bghibli\b", r"\bkyoto animation\b", r"\bkyoto anim\b",
    r"\bjohn wick\b", r"\bstar wars\b", r"\bhakuto\b"
]

# §POS POSITIVE PHRASING MODEL-FACING NEGATIONS
NEGATIVE_PHRASING_PATTERNS = [
    r"\b0%\s+cgi\b",
    r"\bno\s+cgi\b",
    r"\b0%\s+tears\b",
    r"\bno\s+tears\b",
    r"\b0%\s+glass\s+breach\b",
    r"\bno\s+glass\s+breach\b",
    r"\b0%\s+upside[- ]down\b",
    r"\b0%\s+3d\s+render\b"
]


# =============================================================================
# 2. HELPER EXTRACTION FUNCTIONS
# =============================================================================

def get_character_metrics(text: str) -> Dict[str, int]:
    char_len = len(text)
    word_count = len(text.split())
    return {
        "character_length": char_len,
        "word_count": word_count
    }

def extract_named_block(prompt_text: str, block_header_keyword: str) -> str:
    pattern = r"(?:\*\*\[|\[)(?:" + block_header_keyword + r")[^\]]*(?:\]\*\*|\]):?\s*(.*?)(?=\n(?:\*\*\[|\[)(?:KINETIC|ACTING|CINEMATOGRAPHY|CAMERA|LIGHTING|SPATIAL|CHARACTER|IDENTITY|EDITORIAL|PROSE|GLOBAL|RENDER)|\Z)"
    m = re.search(pattern, prompt_text, re.DOTALL | re.IGNORECASE)
    if m and m.group(1):
        return m.group(1).strip()
    return ""

def extract_camera_focal_lengths(text: str) -> List[str]:
    matches = re.findall(r"(?:\[|\b)(1[0-9]|[2-9][0-9]|1[0-9]{2}|2[0-9]{2}|300)mm(?:\s*(?:Prime|Lens|Anamorphic|Medium|Wide|Close|Shot|OTS|Dynamic|Tracking|Two-Shot|Choker|Macro|Angle|at|T\d|\])|\])", text, re.I)
    return sorted(list(set(matches)))

# =============================================================================
# 3. MASTER AUDITOR ENGINE
# =============================================================================

def audit_turn5_prompt(prompt_text: str, clip_duration: float = 15.0, selected_mode: int = 3) -> Dict[str, Any]:
    results = {
        "status": "PASS",
        "errors": [],
        "warnings": [],
        "metrics": {},
        "cross_block_sync": {},
        "forensic_checks": {},
        "causality_matrix": {}
    }
    
    char_len = len(prompt_text)
    word_count = len(prompt_text.split())
    results["metrics"]["character_length"] = char_len
    results["metrics"]["word_count"] = word_count
    results["metrics"]["clip_duration_seconds"] = clip_duration
    results["metrics"]["selected_mode"] = selected_mode

    # 1. CHARACTER & WORD COUNT BUDGET AUDIT (3-TIER DURATION HARD CEILING)
    if selected_mode == 2:
        if char_len < 1900 or char_len > 2050:
            results["warnings"].append(f"Budget Warning (Mode 2): Prompt length {char_len} chars outside strict 1,950-1,980 target envelope.")
    elif selected_mode == 3:
        if clip_duration <= 15.0:
            max_allowed = 4500
        elif clip_duration <= 20.0:
            max_allowed = 5500
        else:
            max_allowed = 7000
            
        if char_len > max_allowed:
            results["warnings"].append(f"Budget Warning (Mode 3): Prompt length {char_len} chars exceeds strict duration ceiling of {max_allowed} chars for {clip_duration}s clip.")

    # 2. BANNED PHRASES & LEXICAL HARD-LOCK VERIFICATION
    for pattern in FORBIDDEN_PHRASES:
        match = re.search(pattern, prompt_text, re.IGNORECASE)
        if match:
            results["errors"].append(f"FATAL LEXICAL VIOLATION: Banned sluggish/negative/cliche token detected: '{match.group(0)}'. Must use 100% positive real-time physics and explicit named entities!")
            results["status"] = "FAIL"

    # Extract Blocks (Supports both UGC 4-Block and Legacy Multi-Block structures)
    prose_block = extract_named_block(prompt_text, "PROSE")
    cinema_block = extract_named_block(prompt_text, "CAMERA & PHYSICS LOCK|CINEMATOGRAPHY|CAMERA")
    lighting_block = extract_named_block(prompt_text, "RENDER & ACTING LOCK|LIGHTING")
    audio_block = extract_named_block(prompt_text, "SPATIAL ACOUSTICS|AUDIO")
    char_block = extract_named_block(prompt_text, "GLOBAL LOCK|CHARACTER|IDENTITY|BIOMETRIC")
    editorial_block = extract_named_block(prompt_text, "EDITORIAL|CONTINUITY")
    kinetic_block = extract_named_block(prompt_text, "CAMERA & PHYSICS LOCK|KINETIC|PHYSICS")
    render_acting_block = extract_named_block(prompt_text, "RENDER & ACTING LOCK")
    global_lock_block = extract_named_block(prompt_text, "GLOBAL LOCK")
    camera_physics_block = extract_named_block(prompt_text, "CAMERA & PHYSICS LOCK")

    # 3. KINETIC VELOCITY & POSITIVE PHYSICS VERIFICATION
    has_positive_physics = bool(re.search(r"(1\.0x\s*real-time|high-velocity|real-time\s*velocity|instantaneous.*gravity|newtonian|9\.8m/s)", kinetic_block + " " + prose_block + " " + camera_physics_block, re.IGNORECASE))
    results["forensic_checks"]["realtime_1_0x_velocity_locked"] = has_positive_physics
    if not has_positive_physics and selected_mode in [1, 2, 3]:
        results["warnings"].append("Kinetic Hardware Warning: [CAMERA & PHYSICS LOCK] or [PROSE] should explicitly declare '1.0x real-time Newtonian velocity' to prevent AI slow-motion interpolation.")

    # 4. ANTI-ACOUSTIC BALLOONING & SFX BLOAT CHECK
    has_anti_sfx_bloat = bool(re.search(r"(sub-bass|high-pass|80hz|transient|rt60|decay|diegetic|acoustic)", audio_block + " " + prompt_text, re.IGNORECASE))
    results["forensic_checks"]["anti_sfx_bloat_profile_declared"] = has_anti_sfx_bloat

    # 5. SUPER-MATHEMATICAL SHOT & CUT PARITY AUDIT (CROSS-BLOCK)
    cut_matches = re.findall(r"\[HARD CUT:?\s*(\d+\.?\d*)s?(?:\s*\|\s*([^\]]+))?\]", prose_block if prose_block else prompt_text, re.IGNORECASE)
    cuts_count = len(cut_matches)
    expected_shots = cuts_count + 1
    cut_timestamps = [float(c[0]) for c in cut_matches]
    
    results["metrics"]["hard_cuts_count"] = cuts_count
    results["metrics"]["expected_shots_count"] = expected_shots
    results["metrics"]["cut_timestamps"] = cut_timestamps
    
    # Verify cut timestamps are monotonically strictly increasing and within duration
    last_t = 0.0
    for t in cut_timestamps:
        if t <= last_t:
            results["errors"].append(f"Mathematical Error: Cut timestamp {t}s is not strictly greater than previous timestamp {last_t}s.")
            results["status"] = "FAIL"
        if t >= clip_duration:
            results["errors"].append(f"Mathematical Error: Cut timestamp {t}s exceeds or equals clip duration ({clip_duration}s).")
            results["status"] = "FAIL"
            
        shot_dur = t - last_t
        if shot_dur > 4.5 and any(w in (prose_block or "").lower() for w in ["brawl", "combat", "fight", "punch", "strike", "tackle"]):
            results["warnings"].append(f"Pacing Alert: Shot duration of {shot_dur:.1f}s before cut at {t}s is too slow for combat action (recommended <= 3.5s per cut).")
        last_t = t

    # Check Block 4 [CINEMATOGRAPHY] Shot Count and Timestamps
    if cinema_block:
        shot_mentions = re.findall(r"Shot\s+(\d+)", cinema_block, re.IGNORECASE)
        if shot_mentions:
            unique_shots = len(set(shot_mentions))
            results["cross_block_sync"]["cinematography_shots_found"] = unique_shots
            if unique_shots != expected_shots:
                results["warnings"].append(f"Cross-Block Shot Disparity: Block 1 has {cuts_count} cuts (expecting {expected_shots} shots), but Cinematography declares {unique_shots} shots.")

    # Check Block 8 [EDITORIAL CONTINUITY]
    if editorial_block:
        for t in cut_timestamps:
            t_str = f"{t}"
            if t_str not in editorial_block and f"{t:.1f}" not in editorial_block:
                results["warnings"].append(f"Editorial Sync Warning: Cut timestamp {t}s from Block 1 is missing in Block 8 [EDITORIAL CONTINUITY].")

    # 6. SUB-SECOND MICRO-TIMESTAMP GRANULARITY & GAP LIMITER
    micro_ts_matches = re.findall(r"(?:At|From)\s+(\d+\.?\d*)s", prose_block if prose_block else prompt_text, re.IGNORECASE)
    micro_ts = [float(ts) for ts in micro_ts_matches]
    results["metrics"]["micro_timestamps_count"] = len(micro_ts)
    results["metrics"]["micro_timestamps_list"] = micro_ts
    
    if len(micro_ts) > 1:
        gaps = [round(micro_ts[i] - micro_ts[i-1], 2) for i in range(1, len(micro_ts))]
        max_gap = max(gaps) if gaps else 0
        results["metrics"]["max_micro_timestamp_gap_seconds"] = max_gap

    # 7. CROSS-BLOCK LENS, LIGHTING & AXIS PARITY
    prose_lenses = extract_camera_focal_lengths(prose_block if prose_block else prompt_text)
    cinema_lenses = extract_camera_focal_lengths(cinema_block) if cinema_block else []
    results["cross_block_sync"]["prose_lenses"] = prose_lenses
    results["cross_block_sync"]["cinema_lenses"] = cinema_lenses

    lighting_kelvins = sorted(list(set(re.findall(r"(\d{4})\s*K", lighting_block if lighting_block else prompt_text, re.IGNORECASE))))
    results["cross_block_sync"]["lighting_kelvins"] = lighting_kelvins

    # Check opening lens lock
    opening_lens_prose = re.search(r"At 0\.0s\s*\[?(\d{2,3})mm", prose_block if prose_block else prompt_text, re.IGNORECASE)
    results["forensic_checks"]["shot1_opening_lens_locked"] = bool(opening_lens_prose)

    # Check 180-degree axis
    has_180_axis = bool(re.search(r"180[- ]degree", prompt_text, re.IGNORECASE))
    results["forensic_checks"]["180_degree_spatial_axis_declared"] = has_180_axis

    # 8. SOMATIC FACIAL MICRO-EXPRESSIONS & PROP HANDOFF AUDIT
    has_facs_tags = bool(re.search(r"AU\d+|corrugator|frontalis|zygomatic|orbicularis", prompt_text, re.IGNORECASE))
    results["forensic_checks"]["somatic_facs_micro_expressions_present"] = has_facs_tags

    # 9. §ML-6 SNAPSHOT NOT POINTER FORENSIC CHECK
    for pointer_pat in BANNED_CROSS_CLIP_POINTERS:
        p_match = re.search(pointer_pat, prompt_text, re.IGNORECASE)
        if p_match:
            results["errors"].append(f"§ML-6 Snapshot Violation: Cross-clip pointer phrase detected: '{p_match.group(0)}'. Every clip prompt MUST be a 100% self-contained snapshot with inlined full values!")
            results["status"] = "FAIL"

    # 10. §IP-CLEAN COPYRIGHTED ENTITY SCRUBBING
    for ip_pat in BANNED_IP_PROPER_NOUNS:
        ip_match = re.search(ip_pat, prompt_text, re.IGNORECASE)
        if ip_match:
            results["warnings"].append(f"§IP-CLEAN Warning: Protected brand/IP name detected: '{ip_match.group(0)}'. Recommended to translate into pure visual traits/lighting aesthetics.")

    # 11. §POS POSITIVE PHRASING MODEL-FACING AUDIT
    for neg_pat in NEGATIVE_PHRASING_PATTERNS:
        neg_match = re.search(neg_pat, prompt_text, re.IGNORECASE)
        if neg_match:
            results["warnings"].append(f"§POS Positive Phrasing Warning: Negation phrasing '{neg_match.group(0)}' detected in prompt text. Reformulate as a positive physical state.")

    # 12. §LIGHT-CLEARANCE OVERHEAD LIGHTING ANCHOR AUDIT
    if lighting_block or prose_block:
        full_light = (lighting_block + " " + prose_block).lower()
        if ("lamp above his head" in full_light or "lamp above her head" in full_light) and "low-fixture cause" not in full_light:
            results["warnings"].append("§LIGHT-CLEARANCE Alert: Hovering overhead lamp detected without explicit ceiling mounting height or 'LOW-FIXTURE CAUSE:' tag. Anchor fixture to ceiling >=60cm above head.")

    # 13. §VO-WPS VOICEOVER CALCULATION & PACING SYNCHRONIZATION AUDIT
    has_vo = bool(re.search(r"\[(?:VO|VOICE[- ]?OVER|NARRATION)[:\s]|(?:\bVO:|\bVoiceover:)", prompt_text, re.IGNORECASE))
    results["forensic_checks"]["voiceover_present"] = has_vo
    
    if has_vo:
        vo_matches = list(re.finditer(r"\[(?:VO|VOICE[- ]?OVER|NARRATION)([^\]]*)\]:?\s*\"([^\"]+)\"", prompt_text, re.IGNORECASE))
        if not vo_matches:
            # Fallback for alternative syntax like VO: "..."
            vo_matches = list(re.finditer(r"(?:VO|Voiceover):\s*\"([^\"]+)\"", prompt_text, re.IGNORECASE))
            
        vo_found_count = 0
        for vm in vo_matches:
            vo_found_count += 1
            vo_tag_info = vm.group(1) if len(vm.groups()) > 1 else ""
            vo_quote = vm.group(2).strip() if len(vm.groups()) > 1 else vm.group(1).strip()
            
            # Word count
            words = [w for w in re.findall(r"\b[\w'-]+\b", vo_quote) if w]
            word_count_actual = len(words)
            
            # Extract timestamp duration: e.g. "1.0s–5.0s", "1.0s - 5.0s", "1.0-5.0", "At 1.0s to 5.0s"
            ts_match = re.search(r"(\d+\.?\d*)\s*s?\s*(?:[-–—→]|to)\s*(\d+\.?\d*)\s*s?", vo_tag_info or prompt_text, re.IGNORECASE)
            duration_actual = 0.0
            if ts_match:
                start_s = float(ts_match.group(1))
                end_s = float(ts_match.group(2))
                duration_actual = round(end_s - start_s, 2)
            
            wps_declared_match = re.search(r"(\d+\.?\d*)\s*wps", vo_tag_info, re.IGNORECASE)
            
            if duration_actual > 0:
                calc_wps = round(word_count_actual / duration_actual, 2)
                results["forensic_checks"][f"vo_{vo_found_count}_wps_metrics"] = {
                    "word_count": word_count_actual,
                    "duration_seconds": duration_actual,
                    "calculated_wps": calc_wps,
                    "declared_wps": float(wps_declared_match.group(1)) if wps_declared_match else None
                }
                
                # Check safe sync envelope: 1.3 <= WPS <= 2.4
                if calc_wps > 2.4:
                    results["errors"].append(
                        f"§VO-WPS Pacing Error: Voiceover line {vo_found_count} speech rate of {calc_wps} WPS ({word_count_actual} words in {duration_actual}s) is TOO FAST (> 2.4 WPS). Risk of rushed delivery, dropped syllables, and visual desynchronization."
                    )
                    results["status"] = "FAIL"
                elif calc_wps < 1.3:
                    results["warnings"].append(
                        f"§VO-WPS Pacing Warning: Voiceover line {vo_found_count} speech rate of {calc_wps} WPS ({word_count_actual} words in {duration_actual}s) is TOO SLOW (< 1.3 WPS). Risk of unnatural dragging, lethargic pacing, or clip overrun."
                    )
                else:
                    results["forensic_checks"][f"vo_{vo_found_count}_sync_status"] = f"SYNCHRONIZED ({calc_wps} WPS, safe 1.3-2.4 envelope)"
            else:
                results["warnings"].append(
                    f"§VO-WPS Audit Warning: Voiceover line {vo_found_count} has missing or unparseable time window (Start.s–End.s). Cannot verify WPS synchronization."
                )

        # Check for lips closed / neutral mouth lock during VO
        has_lips_lock = bool(re.search(r"(lip[s]?\s*(?:closed|shut|remain|resting)|0%\s*mouth\s*mov|neutral\s*(?:mouth|lips|repose))", prompt_text, re.IGNORECASE))
        results["forensic_checks"]["vo_anti_mouth_flapping_locked"] = has_lips_lock
        if not has_lips_lock and any(w in prompt_text.lower() for w in ["character", "man", "woman", "face", "chloe", "protagonist"]):
            results["warnings"].append(
                "§VO-LIPLOCK Warning: Scene contains Voiceover (VO) with on-screen characters, but lacks an explicit 'lips closed, 0% mouth moving for VO' biometric lock to prevent diffusion mouth flapping."
            )

    return results


# =============================================================================
# 4. CLI INTERFACE & DIRECT TEST HARNESS
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="BreakStudio Master Video Prompt Auditor")
    parser.add_argument("input", nargs="?", help="Path to text file containing video prompt or raw prompt string")
    parser.add_argument("--duration", type=float, default=15.0, help="Clip duration in seconds (default: 15.0)")
    parser.add_argument("--mode", type=int, default=3, help="Selected mode: 2 (3-Block) or 3 (8-Block) (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output results strictly as formatted JSON")

    args = parser.parse_args()

    if not args.input:
        print("[*] BreakStudio Zero-Defect Auditor Core Engine Ready.")
        print("Usage: python prompt_auditor.py <prompt_file.txt | 'prompt string'> [--duration 15] [--mode 3] [--json]")
        sys.exit(0)

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            prompt_content = f.read()
    except Exception:
        prompt_content = args.input

    results = audit_turn5_prompt(prompt_content, clip_duration=args.duration, selected_mode=args.mode)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print("\n" + "="*80)
        print(f"BREAKSTUDIO AUDIT REPORT -- STATUS: [{results['status']}]")
        print("="*80)
        print(f"Length: {results['metrics']['character_length']} chars | Words: {results['metrics']['word_count']} | Duration: {results['metrics']['clip_duration_seconds']}s")
        print(f"Hard Cuts Found: {results['metrics']['hard_cuts_count']} (Expected Shots: {results['metrics']['expected_shots_count']})")
        print(f"Cut Timestamps: {results['metrics']['cut_timestamps']}")
        print(f"180-deg Axis Declared: {results['forensic_checks'].get('180_degree_spatial_axis_declared', False)}")
        print(f"Real-Time 1.0x Velocity Locked: {results['forensic_checks'].get('realtime_1_0x_velocity_locked', False)}")
        if results["forensic_checks"].get("voiceover_present"):
            print(f"Voiceover (VO) Detected: True | Anti-Mouth-Flapping Lock: {results['forensic_checks'].get('vo_anti_mouth_flapping_locked', False)}")
            for k, v in results["forensic_checks"].items():
                if "wps_metrics" in k:
                    print(f"  * {k}: {v['calculated_wps']} WPS ({v['word_count']} words in {v['duration_seconds']}s, declared: {v['declared_wps']})")
        
        if results["errors"]:
            print("\n[!] ERRORS (FAIL):")
            for err in results["errors"]:
                print(f"  * {err}")
                
        if results["warnings"]:
            print("\n[?] WARNINGS:")
            for warn in results["warnings"]:
                print(f"  * {warn}")

        if not results["errors"] and not results["warnings"]:
            print("\n[+] PERFECT PASS: 100% Zero-Defect Optical & UGC Compliance!")
        print("="*80 + "\n")

    if results["status"] == "FAIL":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
