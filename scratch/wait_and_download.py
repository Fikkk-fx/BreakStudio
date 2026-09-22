import os
import sys
import time
import json
import urllib.request

prediction_id = "a4c7p4ksr5rmy0d0rq9bcs7c2c"
output_path = os.path.join("outputs", "ugc_fashion_360_orbit_15s.mp4")
os.makedirs("outputs", exist_ok=True)

key = "pru_IwuwIn1Gce5Axm70zp4wfGbx8sssd2Vs"
headers = {"apikey": key}

print(f"[*] Monitoring Pruna AI prediction ID: {prediction_id}")
print(f"[*] Target output path: {output_path}")

poll_interval = 10
max_wait = 1800  # 30 minutes
start_time = time.time()

while time.time() - start_time < max_wait:
    try:
        req = urllib.request.Request(f"https://api.pruna.ai/v1/predictions/status/{prediction_id}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            status = data.get("status")
            elapsed = int(time.time() - start_time)
            print(f"[{elapsed}s] Status: {status}")
            
            if status == "succeeded":
                gen_url = data.get("generation_url")
                print(f"[SUCCESS] Generation finished in {elapsed}s!")
                print(f"[*] Downloading video from: {gen_url}")
                urllib.request.urlretrieve(gen_url, output_path)
                file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
                print(f"[SUCCESS] Video saved to {output_path} ({file_size_mb:.2f} MB)")
                
                # Save metadata report
                report_path = os.path.join("outputs", "ugc_fashion_360_orbit_15s_metadata.json")
                with open(report_path, "w", encoding="utf-8") as f:
                    json.dump({
                        "prediction_id": prediction_id,
                        "status": status,
                        "elapsed_seconds": elapsed,
                        "file_size_mb": round(file_size_mb, 2),
                        "output_video": output_path,
                        "generation_url": gen_url,
                        "model": "p-video-2-pro",
                        "resolution": "768p",
                        "duration": 15,
                        "mode": "quality",
                        "aspect_ratio": "16:9"
                    }, f, indent=2)
                sys.exit(0)
            elif status == "failed":
                print(f"[ERROR] Prediction failed: {data}")
                sys.exit(1)
    except Exception as e:
        print(f"[WARNING] Polling error: {e}")

    time.sleep(poll_interval)

print("[TIMEOUT] Maximum wait time exceeded.")
sys.exit(1)
