#!/usr/bin/env python3
"""
Pruna AI Live End-to-End Test Suite for Director O.S. V20.5
===========================================================
Executes live tests across image and video models and saves all outputs in `test_results/`.
"""

import os
import sys
import json
import time

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from pruna_client import PrunaClient

OUTPUT_DIR = "test_results"

def run_suite():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tests": []
    }

    client = PrunaClient()
    print("=" * 60)
    print("[*] STARTING PRUNA AI LIVE INTEGRATION TEST SUITE")
    print(f"[*] Destination Folder: {os.path.abspath(OUTPUT_DIR)}")
    print("=" * 60)

    # ---------------------------------------------------------
    # TEST 1: File Upload (Asset Ingestion)
    # ---------------------------------------------------------
    print("\n[TEST 1/3] Testing File Ingestion (/v1/files)...")
    sample_file = os.path.join(OUTPUT_DIR, "sample_asset.txt")
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Director O.S. V20.5 UGC Production Test Asset - Timestamp: " + time.ctime())
    
    t0 = time.time()
    try:
        remote_url = client.upload_file(sample_file)
        elapsed = round(time.time() - t0, 2)
        print(f"[SUCCESS] Upload Succeeded in {elapsed}s: {remote_url}")
        report["tests"].append({
            "name": "upload_file",
            "status": "PASS",
            "elapsed_seconds": elapsed,
            "result_url": remote_url
        })
    except Exception as e:
        print(f"[FAIL] Upload Failed: {e}")
        report["tests"].append({
            "name": "upload_file",
            "status": "FAIL",
            "error": str(e)
        })

    # ---------------------------------------------------------
    # TEST 2: p-image-ideogram (Turn 4a UGC Asset Generation)
    # ---------------------------------------------------------
    print("\n[TEST 2/3] Testing p-image-ideogram (Turn 4a CharSheet/UGC Plate)...")
    ideogram_prompt = (
        "Raw smartphone selfie of a friendly Indonesian barista smiling inside a busy Jakarta cafe, "
        "natural warm morning light, candid imperfect camera angle, 9:16 vertical ratio, photorealistic"
    )
    ideogram_out = os.path.join(OUTPUT_DIR, "test_01_ideogram_ugc.jpg")
    t0 = time.time()
    try:
        res = client.generate_image_ideogram(
            prompt=ideogram_prompt,
            thinking="low",
            image_size="1K",
            aspect_ratio="9:16",
            wait=True
        )
        gen_url = res.get("generation_url")
        print(f"Downloading image from: {gen_url}")
        client.download_file(gen_url, ideogram_out)
        elapsed = round(time.time() - t0, 2)
        size_kb = round(os.path.getsize(ideogram_out) / 1024, 1)
        print(f"[SUCCESS] p-image-ideogram Succeeded in {elapsed}s ({size_kb} KB) -> {ideogram_out}")
        report["tests"].append({
            "name": "p-image-ideogram",
            "status": "PASS",
            "elapsed_seconds": elapsed,
            "output_file": ideogram_out,
            "file_size_kb": size_kb,
            "generation_url": gen_url
        })
    except Exception as e:
        print(f"[FAIL] p-image-ideogram Failed: {e}")
        report["tests"].append({
            "name": "p-image-ideogram",
            "status": "FAIL",
            "error": str(e)
        })

    # ---------------------------------------------------------
    # TEST 3: flux-dev (Turn 4a Photorealistic Asset Generation)
    # ---------------------------------------------------------
    print("\n[TEST 3/3] Testing flux-dev (Turn 4a Photorealistic Street Plate)...")
    flux_prompt = (
        "Hyper-realistic Indonesian street food cart at twilight in Bandung, glowing incandescent bulb, "
        "steaming kettle, raw smartphone CMOS sensor 24mm f/1.7, 9:16 vertical"
    )
    flux_out = os.path.join(OUTPUT_DIR, "test_02_flux_dev_ugc.jpg")
    t0 = time.time()
    try:
        res = client.generate_flux_dev(
            prompt=flux_prompt,
            speed_mode="Juiced 🔥 (default)",
            aspect_ratio="9:16",
            wait=True
        )
        gen_url = res.get("generation_url")
        print(f"Downloading image from: {gen_url}")
        client.download_file(gen_url, flux_out)
        elapsed = round(time.time() - t0, 2)
        size_kb = round(os.path.getsize(flux_out) / 1024, 1)
        print(f"[SUCCESS] flux-dev Succeeded in {elapsed}s ({size_kb} KB) -> {flux_out}")
        report["tests"].append({
            "name": "flux-dev",
            "status": "PASS",
            "elapsed_seconds": elapsed,
            "output_file": flux_out,
            "file_size_kb": size_kb,
            "generation_url": gen_url
        })
    except Exception as e:
        print(f"[FAIL] flux-dev Failed: {e}")
        report["tests"].append({
            "name": "flux-dev",
            "status": "FAIL",
            "error": str(e)
        })

    # Save summary report
    report_file = os.path.join(OUTPUT_DIR, "test_report.json")
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n[REPORT] Test report saved to: {report_file}")
    print("=" * 60)
    print("[*] ALL TESTS EXECUTED!")
    print("=" * 60)

if __name__ == "__main__":
    run_suite()
