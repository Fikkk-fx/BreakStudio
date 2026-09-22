#!/usr/bin/env python3
"""
Pruna AI Unified Client & CLI Engine for Director O.S. V20.5 (Raw UGC Edition)
================================================================================
Comprehensive client supporting:
- Models:
    1. p-video-2-pro     (Text/Image-to-Video, 480p/768p, speed/quality/cost modes, generated audio)
    2. p-video-2         (Text/Image/Audio-to-Video, 720p/1080p, 24/48fps, duration 1-20s)
    3. p-video-edit      (Video-to-Video editing with prompt & up to 4 reference images)
    4. p-image-ideogram  (Text-to-Image with advanced typography & layout, 1K/2K, thinking levels)
    5. flux-dev          (Photorealistic text-to-image with speed optimization modes)
    6. flux-dev-lora     (Text-to-image & image-to-image with HuggingFace LoRA weights)
- Zero external dependencies (uses standard library urllib)
- Auto-loads PRUNA_AI_API_KEY from .env or environment variable
- Supports direct file uploads (image/video/audio) and automatic polling
"""

import os
import sys
import json
import time
import uuid
import mimetypes
import argparse
import urllib.request
import urllib.error
from typing import Dict, Any, Optional, List, Union

BASE_URL = "https://api.pruna.ai/v1"

def load_env_file(env_path: Optional[str] = None) -> Dict[str, str]:
    """Load key-value pairs from .env file without external dependencies."""
    env_vars = {}
    candidates = [
        env_path,
        os.path.join(os.getcwd(), ".env"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    ]
    for path in candidates:
        if path and os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            k, v = line.split("=", 1)
                            k = k.strip()
                            v = v.strip().strip("'\"")
                            env_vars[k] = v
                break
            except Exception:
                pass
    return env_vars


class PrunaClient:
    """Official Pruna AI REST API Client for Director O.S."""

    def __init__(self, api_key: Optional[str] = None, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")
        env = load_env_file()
        self.api_key = api_key or os.environ.get("PRUNA_AI_API_KEY") or env.get("PRUNA_AI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "PRUNA_AI_API_KEY is required. Provide it via argument, environment variable, or .env file."
            )

    def _headers(self, model: Optional[str] = None, try_sync: bool = False, content_type: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "apikey": self.api_key
        }
        if model:
            headers["Model"] = model
        if try_sync:
            headers["Try-Sync"] = "true"
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def upload_file(self, file_path: str) -> str:
        """
        Upload local file to Pruna AI /v1/files endpoint.
        Returns the remote file URL (urls.get).
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Local file not found: {file_path}")

        boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
        filename = os.path.basename(file_path)
        content_type, _ = mimetypes.guess_type(file_path)
        if not content_type:
            content_type = "application/octet-stream"

        body = bytearray()
        body.extend(f"--{boundary}\r\n".encode("utf-8"))
        body.extend(f'Content-Disposition: form-data; name="content"; filename="{filename}"\r\n'.encode("utf-8"))
        body.extend(f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"))
        with open(file_path, "rb") as f:
            body.extend(f.read())
        body.extend(b"\r\n")
        body.extend(f"--{boundary}--\r\n".encode("utf-8"))

        req = urllib.request.Request(
            f"{self.base_url}/files",
            data=bytes(body),
            headers=self._headers(content_type=f"multipart/form-data; boundary={boundary}"),
            method="POST"
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                file_url = data.get("urls", {}).get("get") or f"{self.base_url}/files/{data.get('id')}"
                return file_url
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Failed to upload file ({e.code} {e.reason}): {err_body}")

    def resolve_media_input(self, media_path_or_url: Optional[str]) -> Optional[str]:
        """Resolves an input that might be a local path or remote URL. If local, uploads it."""
        if not media_path_or_url:
            return None
        if media_path_or_url.startswith("http://") or media_path_or_url.startswith("https://"):
            return media_path_or_url
        if os.path.isfile(media_path_or_url):
            print(f"Uploading local asset to Pruna: {media_path_or_url}...")
            url = self.upload_file(media_path_or_url)
            print(f"Asset uploaded: {url}")
            return url
        return media_path_or_url

    def create_prediction(self, model: str, input_params: Dict[str, Any], try_sync: bool = False) -> Dict[str, Any]:
        """Create prediction request."""
        url = f"{self.base_url}/predictions"
        headers = self._headers(model=model, try_sync=try_sync, content_type="application/json")
        payload = json.dumps({"input": input_params}).encode("utf-8")

        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Prediction failed ({e.code} {e.reason}) for model {model}: {err_body}")

    def get_prediction_status(self, prediction_id: str) -> Dict[str, Any]:
        """Poll status for an asynchronous prediction."""
        url = f"{self.base_url}/predictions/status/{prediction_id}"
        req = urllib.request.Request(url, headers=self._headers(), method="GET")
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Status check failed ({e.code} {e.reason}) for {prediction_id}: {err_body}")

    def wait_for_completion(
        self,
        prediction_id: str,
        poll_interval: float = 3.0,
        timeout: float = 600.0,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """Poll prediction until status is succeeded or failed."""
        start_time = time.time()
        dots = 0
        while True:
            elapsed = time.time() - start_time
            if elapsed > timeout:
                raise TimeoutError(f"Prediction {prediction_id} timed out after {timeout} seconds")

            status_data = self.get_prediction_status(prediction_id)
            status = status_data.get("status", "").lower()

            if verbose:
                dots += 1
                msg = status_data.get("message", "Processing")
                sys.stdout.write(f"\r[{int(elapsed)}s] Status: {status} ({msg}) {'.' * (dots % 4):<3}")
                sys.stdout.flush()

            if status == "succeeded":
                if verbose:
                    print(f"\nCompleted in {elapsed:.1f}s!")
                return status_data
            elif status == "failed":
                if verbose:
                    print("")
                error_msg = status_data.get("error") or status_data.get("message") or "Unknown error"
                raise RuntimeError(f"Prediction failed for {prediction_id}: {error_msg}")

            time.sleep(poll_interval)

    def download_file(self, url: str, output_path: str) -> str:
        """Download remote asset (image/video) to local path."""
        req = urllib.request.Request(url, headers=self._headers())
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        try:
            with urllib.request.urlopen(req) as resp, open(output_path, "wb") as f:
                while True:
                    chunk = resp.read(64 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
            return output_path
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Failed to download {url} ({e.code} {e.reason}): {err_body}")

    # =========================================================================
    # SPECIFIC MODEL GENERATION METHODS
    # =========================================================================

    def generate_image_ideogram(
        self,
        prompt: str,
        thinking: str = "high",
        image_size: str = "1K",
        aspect_ratio: str = "9:16",
        prompt_upsampling: bool = True,
        output_format: str = "jpg",
        output_quality: int = 80,
        seed: Optional[int] = None,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Generate high-quality image with typography via p-image-ideogram."""
        params: Dict[str, Any] = {
            "prompt": prompt,
            "thinking": thinking,
            "image_size": image_size,
            "aspect_ratio": aspect_ratio,
            "prompt_upsampling": prompt_upsampling,
            "output_format": output_format,
            "output_quality": output_quality
        }
        if seed is not None:
            params["seed"] = seed

        res = self.create_prediction("p-image-ideogram", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])

    def generate_flux_dev(
        self,
        prompt: str,
        speed_mode: str = "Juiced 🔥 (default)",
        num_inference_steps: int = 28,
        guidance: float = 3.5,
        aspect_ratio: str = "9:16",
        image_size: int = 1024,
        output_format: str = "jpg",
        output_quality: int = 80,
        seed: int = -1,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Generate photorealistic image via flux-dev."""
        params: Dict[str, Any] = {
            "prompt": prompt,
            "speed_mode": speed_mode,
            "num_inference_steps": num_inference_steps,
            "guidance": guidance,
            "aspect_ratio": aspect_ratio,
            "image_size": image_size,
            "output_format": output_format,
            "output_quality": output_quality,
            "seed": seed
        }
        res = self.create_prediction("flux-dev", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])

    def generate_flux_dev_lora(
        self,
        prompt: str,
        lora: Optional[str] = None,
        lora_scale: float = 1.0,
        extra_lora: Optional[str] = None,
        extra_lora_scale: float = 1.0,
        image: Optional[str] = None,
        prompt_strength: float = 0.8,
        num_outputs: int = 1,
        num_inference_steps: int = 28,
        guidance: float = 3.0,
        aspect_ratio: str = "9:16",
        megapixels: str = "1",
        speed_mode: str = "Juiced 🧃",
        seed: Optional[int] = None,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Generate image with custom HuggingFace LoRA via flux-dev-lora."""
        resolved_img = self.resolve_media_input(image)
        params: Dict[str, Any] = {
            "prompt": prompt,
            "num_outputs": num_outputs,
            "num_inference_steps": num_inference_steps,
            "guidance": guidance,
            "aspect_ratio": aspect_ratio,
            "megapixels": megapixels,
            "speed_mode": speed_mode
        }
        if lora:
            params["lora"] = lora
            params["lora_scale"] = lora_scale
        if extra_lora:
            params["extra_lora"] = extra_lora
            params["extra_lora_scale"] = extra_lora_scale
        if resolved_img:
            params["image"] = resolved_img
            params["prompt_strength"] = prompt_strength
        if seed is not None:
            params["seed"] = seed

        res = self.create_prediction("flux-dev-lora", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])

    def generate_video_2_pro(
        self,
        prompt: str,
        image: Optional[str] = None,
        last_frame_image: Optional[str] = None,
        duration: int = 5,
        resolution: str = "768p",
        mode: str = "speed",
        prompt_upsampler: str = "turbo",
        aspect_ratio: str = "9:16",
        seed: Optional[int] = None,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Generate high-end video via p-video-2-pro with generated audio."""
        resolved_img = self.resolve_media_input(image)
        resolved_last_img = self.resolve_media_input(last_frame_image)

        params: Dict[str, Any] = {
            "prompt": prompt,
            "duration": duration,
            "resolution": resolution,
            "mode": mode,
            "prompt_upsampler": prompt_upsampler,
            "aspect_ratio": aspect_ratio
        }
        if resolved_img:
            params["image"] = resolved_img
        if resolved_last_img:
            params["last_frame_image"] = resolved_last_img
        if seed is not None:
            params["seed"] = seed

        res = self.create_prediction("p-video-2-pro", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])

    def generate_video_2(
        self,
        prompt: str,
        duration: Optional[int] = 5,
        image: Optional[str] = None,
        last_frame_image: Optional[str] = None,
        audio: Optional[str] = None,
        resolution: str = "720p",
        fps: int = 24,
        aspect_ratio: str = "9:16",
        draft: bool = False,
        save_audio: bool = True,
        prompt_upsampling: bool = True,
        disable_safety_filter: bool = True,
        seed: Optional[int] = None,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Generate video via p-video-2 with optional audio conditioning."""
        resolved_img = self.resolve_media_input(image)
        resolved_last_img = self.resolve_media_input(last_frame_image)
        resolved_audio = self.resolve_media_input(audio)

        params: Dict[str, Any] = {
            "prompt": prompt,
            "resolution": resolution,
            "fps": fps,
            "aspect_ratio": aspect_ratio,
            "draft": draft,
            "save_audio": save_audio,
            "prompt_upsampling": prompt_upsampling,
            "disable_safety_filter": disable_safety_filter
        }
        if duration is not None:
            params["duration"] = duration
        if resolved_img:
            params["image"] = resolved_img
        if resolved_last_img:
            params["last_frame_image"] = resolved_last_img
        if resolved_audio:
            params["audio"] = resolved_audio
        if seed is not None:
            params["seed"] = seed

        res = self.create_prediction("p-video-2", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])

    def edit_video(
        self,
        video: str,
        prompt: str,
        images: Optional[List[str]] = None,
        draft: bool = False,
        save_audio: bool = True,
        prompt_upsampling: bool = True,
        seed: Optional[int] = None,
        try_sync: bool = False,
        wait: bool = True
    ) -> Dict[str, Any]:
        """Edit an existing video (up to 15s) using prompt & reference images via p-video-edit."""
        resolved_video = self.resolve_media_input(video)
        resolved_images = []
        if images:
            for img in images:
                resolved_images.append(self.resolve_media_input(img))

        params: Dict[str, Any] = {
            "video": resolved_video,
            "prompt": prompt,
            "draft": draft,
            "save_audio": save_audio,
            "prompt_upsampling": prompt_upsampling
        }
        if resolved_images:
            params["images"] = resolved_images
        if seed is not None:
            params["seed"] = seed

        res = self.create_prediction("p-video-edit", params, try_sync=try_sync)
        if res.get("status") == "succeeded" or not wait or "id" not in res:
            return res
        return self.wait_for_completion(res["id"])


# =============================================================================
# CLI INTERFACE
# =============================================================================

def build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pruna_client.py",
        description="Pruna AI CLI Direct Dispatch Engine for Director O.S. V20.5"
    )
    parser.add_argument("--api-key", help="Pruna API key (overrides .env and env var)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 1. Upload Subcommand
    upload_parser = subparsers.add_parser("upload", help="Upload local asset to Pruna AI")
    upload_parser.add_argument("--file", required=True, help="Local file path to upload")

    # 2. Image Generation Subcommand
    img_parser = subparsers.add_parser("image", help="Generate image with p-image-ideogram, flux-dev, or flux-dev-lora")
    img_parser.add_argument("--model", choices=["p-image-ideogram", "flux-dev", "flux-dev-lora"], default="p-image-ideogram")
    img_parser.add_argument("--prompt", required=True, help="Text prompt")
    img_parser.add_argument("--aspect-ratio", default="9:16", help="Aspect ratio (e.g. 9:16, 1:1, 16:9)")
    img_parser.add_argument("--thinking", default="high", choices=["very low", "low", "medium", "high", "very high"], help="Thinking level for ideogram")
    img_parser.add_argument("--image-size", default="1K", choices=["1K", "2K"], help="Image size budget for ideogram")
    img_parser.add_argument("--speed-mode", default="Juiced 🔥 (default)", help="Speed mode for flux-dev / flux-dev-lora")
    img_parser.add_argument("--lora", help="HuggingFace LoRA repo (for flux-dev-lora)")
    img_parser.add_argument("--lora-scale", type=float, default=1.0)
    img_parser.add_argument("--ref-image", help="Input image for img2img (flux-dev-lora)")
    img_parser.add_argument("--output", help="Save downloaded image to local path")
    img_parser.add_argument("--no-wait", action="store_true", help="Submit async and exit immediately")

    # 3. Video Generation Subcommand
    vid_parser = subparsers.add_parser("video", help="Generate video with p-video-2-pro or p-video-2")
    vid_parser.add_argument("--model", choices=["p-video-2-pro", "p-video-2"], default="p-video-2-pro")
    vid_parser.add_argument("--prompt", required=True, help="Text prompt for video")
    vid_parser.add_argument("--duration", type=int, default=5, help="Video duration in seconds")
    vid_parser.add_argument("--aspect-ratio", default="9:16", help="Aspect ratio (e.g. 9:16, 16:9)")
    vid_parser.add_argument("--resolution", default="768p", help="Resolution: 480p/768p for 2-pro, 720p/1080p for 2")
    vid_parser.add_argument("--mode", default="speed", choices=["speed", "quality", "cost"], help="Mode for p-video-2-pro")
    vid_parser.add_argument("--image", help="First-frame reference image (local path or URL)")
    vid_parser.add_argument("--last-frame-image", help="Last-frame reference image")
    vid_parser.add_argument("--audio", help="Audio condition file for p-video-2")
    vid_parser.add_argument("--fps", type=int, default=24, choices=[24, 48], help="FPS for p-video-2")
    vid_parser.add_argument("--draft", action="store_true", help="Draft mode (faster/cheaper)")
    vid_parser.add_argument("--output", help="Save downloaded video to local path")
    vid_parser.add_argument("--no-wait", action="store_true", help="Submit async and exit immediately")

    # 4. Video Edit Subcommand
    edit_parser = subparsers.add_parser("edit-video", help="Edit video with p-video-edit")
    edit_parser.add_argument("--video", required=True, help="Source video (local path or URL, max 15s)")
    edit_parser.add_argument("--prompt", required=True, help="Editing instruction prompt")
    edit_parser.add_argument("--images", nargs="*", help="Reference images (up to 4)")
    edit_parser.add_argument("--draft", action="store_true", help="Draft mode")
    edit_parser.add_argument("--output", help="Save downloaded edited video to local path")
    edit_parser.add_argument("--no-wait", action="store_true", help="Submit async and exit immediately")

    # 5. Status Subcommand
    status_parser = subparsers.add_parser("status", help="Check prediction status")
    status_parser.add_argument("--id", required=True, help="Prediction ID")
    status_parser.add_argument("--wait", action="store_true", help="Wait until finished")
    status_parser.add_argument("--output", help="Download output if completed")

    return parser


def main():
    parser = build_cli_parser()
    args = parser.parse_args()

    try:
        client = PrunaClient(api_key=args.api_key)
    except Exception as e:
        print(f"[ERROR] Initialization error: {e}", file=sys.stderr)
        sys.exit(1)

    # Automatically resolve prompt from file if path or @file is given
    if hasattr(args, "prompt") and args.prompt:
        prompt_file = args.prompt[1:] if args.prompt.startswith("@") else args.prompt
        if os.path.isfile(prompt_file):
            try:
                with open(prompt_file, "r", encoding="utf-8") as f:
                    args.prompt = f.read().strip()
            except Exception as e:
                print(f"[ERROR] Failed to read prompt file '{prompt_file}': {e}", file=sys.stderr)
                sys.exit(1)

    try:
        if args.command == "upload":
            url = client.upload_file(args.file)
            print(f"[SUCCESS] Uploaded: {url}")
            return

        if args.command == "image":
            wait = not args.no_wait
            print(f"[*] Dispatching image generation to {args.model}...")
            if args.model == "p-image-ideogram":
                res = client.generate_image_ideogram(
                    prompt=args.prompt,
                    thinking=args.thinking,
                    image_size=args.image_size,
                    aspect_ratio=args.aspect_ratio,
                    wait=wait
                )
            elif args.model == "flux-dev":
                res = client.generate_flux_dev(
                    prompt=args.prompt,
                    speed_mode=args.speed_mode,
                    aspect_ratio=args.aspect_ratio,
                    wait=wait
                )
            elif args.model == "flux-dev-lora":
                res = client.generate_flux_dev_lora(
                    prompt=args.prompt,
                    lora=args.lora,
                    lora_scale=args.lora_scale,
                    image=args.ref_image,
                    speed_mode=args.speed_mode,
                    aspect_ratio=args.aspect_ratio,
                    wait=wait
                )
            print(json.dumps(res, indent=2))
            gen_url = res.get("generation_url")
            if gen_url and args.output:
                print(f"[*] Downloading result to {args.output}...")
                client.download_file(gen_url, args.output)
                print(f"[SUCCESS] Saved to {args.output}")

        elif args.command == "video":
            wait = not args.no_wait
            print(f"[*] Dispatching video generation to {args.model}...")
            if args.model == "p-video-2-pro":
                res = client.generate_video_2_pro(
                    prompt=args.prompt,
                    image=args.image,
                    last_frame_image=args.last_frame_image,
                    duration=args.duration,
                    resolution=args.resolution,
                    mode=args.mode,
                    aspect_ratio=args.aspect_ratio,
                    wait=wait
                )
            elif args.model == "p-video-2":
                res = client.generate_video_2(
                    prompt=args.prompt,
                    duration=args.duration,
                    image=args.image,
                    last_frame_image=args.last_frame_image,
                    audio=args.audio,
                    resolution=args.resolution if args.resolution in ["720p", "1080p"] else "720p",
                    fps=args.fps,
                    aspect_ratio=args.aspect_ratio,
                    draft=args.draft,
                    wait=wait
                )
            print(json.dumps(res, indent=2))
            gen_url = res.get("generation_url")
            if gen_url and args.output:
                print(f"[*] Downloading video to {args.output}...")
                client.download_file(gen_url, args.output)
                print(f"[SUCCESS] Video saved to {args.output}")

        elif args.command == "edit-video":
            wait = not args.no_wait
            print("[*] Dispatching video editing to p-video-edit...")
            res = client.edit_video(
                video=args.video,
                prompt=args.prompt,
                images=args.images,
                draft=args.draft,
                wait=wait
            )
            print(json.dumps(res, indent=2))
            gen_url = res.get("generation_url")
            if gen_url and args.output:
                print(f"[*] Downloading edited video to {args.output}...")
                client.download_file(gen_url, args.output)
                print(f"[SUCCESS] Edited video saved to {args.output}")

        elif args.command == "status":
            if args.wait:
                res = client.wait_for_completion(args.id)
            else:
                res = client.get_prediction_status(args.id)
            print(json.dumps(res, indent=2))
            gen_url = res.get("generation_url")
            if gen_url and args.output:
                print(f"[*] Downloading output to {args.output}...")
                client.download_file(gen_url, args.output)
                print(f"[SUCCESS] Saved to {args.output}")

    except Exception as e:
        print(f"[ERROR] Execution failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
