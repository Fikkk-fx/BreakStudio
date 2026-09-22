import os
import sys
import json

# Ensure current working directory is in sys.path
sys.path.insert(0, os.path.abspath("."))

from pruna_client import PrunaClient

prompt_path = os.path.join("scratch", "draft_fashion_prompt.txt")
if not os.path.isfile(prompt_path):
    print(f"Error: {prompt_path} not found")
    sys.exit(1)

with open(prompt_path, "r", encoding="utf-8") as f:
    prompt = f.read().strip()

print("="*80)
print("PRUNA AI VIDEO DISPATCH: UGC FASHION 360-DEGREE ORBIT (15s)")
print("="*80)
print(f"Model: p-video-2-pro")
print(f"Resolution: 768p")
print(f"Duration: 15s")
print(f"Mode: quality")
print(f"Aspect Ratio: 16:9")
print(f"Prompt Length: {len(prompt)} characters")
print("="*80)

client = PrunaClient()
print("[*] Initiating video generation request...")

try:
    res = client.generate_video_2_pro(
        prompt=prompt,
        duration=15,
        resolution="768p",
        mode="quality",
        aspect_ratio="16:9",
        wait=True
    )
    
    print("\n" + "="*80)
    print("[PREDICTION COMPLETED]")
    print("="*80)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    
    gen_url = res.get("generation_url")
    if gen_url:
        os.makedirs("outputs", exist_ok=True)
        output_path = os.path.join("outputs", "ugc_fashion_360_orbit_15s.mp4")
        print(f"\n[*] Downloading final video from {gen_url} to {output_path}...")
        client.download_file(gen_url, output_path)
        print(f"[SUCCESS] Video file successfully saved to {output_path}")
    else:
        print(f"[WARNING] No direct generation_url found in response: {res}")
except Exception as e:
    print(f"\n[ERROR] Generation failed: {e}", file=sys.stderr)
    sys.exit(1)
