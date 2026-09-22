import os
import sys
import asyncio
import json
import uuid
import datetime
from typing import Optional, List, Dict, Any
import logging

from .config import settings
from . import database as db
from .schemas import ImageGenerateRequest, VideoGenerateRequest, VideoEditRequest

# Add parent dir to sys.path to import pruna_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from pruna_client import PrunaClient
except ImportError as e:
    logging.error(f"Could not import PrunaClient: {e}")
    PrunaClient = None

logger = logging.getLogger(__name__)

class PrunaService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrunaService, cls).__new__(cls)
            cls._instance.client = PrunaClient(api_key=settings.PRUNA_AI_API_KEY) if PrunaClient else None
        return cls._instance

    async def _poll_job(self, job_id: str, prediction_id: str, model_name: str = ""):
        if not self.client:
            return
            
        start_time = datetime.datetime.utcnow()
        try:
            while True:
                # get_prediction_status is the correct method in PrunaClient
                status_res = await asyncio.to_thread(self.client.get_prediction_status, prediction_id)
                status = str(status_res.get('status', 'processing')).lower()
                
                updates = {'status': status}
                if status == 'succeeded':
                    output_url = status_res.get('generation_url')
                    if not output_url and isinstance(status_res.get('output'), dict):
                        output_url = status_res['output'].get('generation_url')
                    elif not output_url and isinstance(status_res.get('output'), str) and status_res['output'].startswith('http'):
                        output_url = status_res['output']

                    updates['output_url'] = output_url
                    
                    if output_url:
                        clean_url = output_url.split('?')[0]
                        file_ext = clean_url.split('.')[-1] if '.' in clean_url else ''
                        if not file_ext or len(file_ext) > 4:
                            file_ext = 'mp4' if 'video' in model_name.lower() else 'jpg'
                        
                        output_filename = f"{job_id}.{file_ext}"
                        output_path = os.path.join(settings.OUTPUT_DIR, output_filename)
                        
                        # Download output locally
                        await asyncio.to_thread(self.client.download_file, output_url, output_path)
                        updates['output_path'] = os.path.join('outputs', output_filename)
                    
                    end_time = datetime.datetime.utcnow()
                    updates['elapsed_seconds'] = round((end_time - start_time).total_seconds(), 1)
                    await db.update_job(job_id, updates)
                    break
                    
                elif status == 'failed':
                    error_msg = status_res.get('error') or status_res.get('message') or 'Prediction generation failed'
                    updates['error'] = str(error_msg)
                    end_time = datetime.datetime.utcnow()
                    updates['elapsed_seconds'] = round((end_time - start_time).total_seconds(), 1)
                    await db.update_job(job_id, updates)
                    break
                    
                else:
                    await db.update_job(job_id, updates)
                    
                await asyncio.sleep(3.0)
                
                if (datetime.datetime.utcnow() - start_time).total_seconds() > 600:
                    await db.update_job(job_id, {'status': 'failed', 'error': 'Timeout waiting for completion (600s)'})
                    break
                    
        except Exception as e:
            logger.error(f"Error polling job {job_id}: {e}")
            await db.update_job(job_id, {'status': 'failed', 'error': str(e)})

    async def generate_image(self, job_id: str, request: ImageGenerateRequest, image_file_path: Optional[str] = None):
        if not self.client:
            await db.update_job(job_id, {'status': 'failed', 'error': 'PrunaClient not initialized. Check PRUNA_AI_API_KEY.'})
            return

        try:
            model_name = request.effective_model
            res = None

            if model_name == "p-image-ideogram":
                res = await asyncio.to_thread(
                    self.client.generate_image_ideogram,
                    prompt=request.prompt,
                    thinking=request.effective_thinking or "high",
                    image_size=request.image_size or "1K",
                    aspect_ratio=request.aspect_ratio or "9:16",
                    prompt_upsampling=True if request.prompt_upsampling is not False else False,
                    output_format=request.output_format or "jpg",
                    output_quality=request.output_quality or 80,
                    seed=request.seed,
                    wait=False
                )
            elif model_name == "flux-dev":
                res = await asyncio.to_thread(
                    self.client.generate_flux_dev,
                    prompt=request.prompt,
                    speed_mode=request.speed_mode or "Juiced 🔥 (default)",
                    num_inference_steps=request.num_inference_steps or 28,
                    guidance=request.guidance or 3.5,
                    aspect_ratio=request.aspect_ratio or "9:16",
                    image_size=1024,
                    output_format=request.output_format or "jpg",
                    output_quality=request.output_quality or 80,
                    seed=request.seed if request.seed is not None else -1,
                    wait=False
                )
            elif model_name == "flux-dev-lora":
                res = await asyncio.to_thread(
                    self.client.generate_flux_dev_lora,
                    prompt=request.prompt,
                    lora=request.lora,
                    lora_scale=request.lora_scale or 1.0,
                    extra_lora=request.extra_lora,
                    extra_lora_scale=request.extra_lora_scale or 1.0,
                    image=image_file_path,
                    prompt_strength=request.prompt_strength or 0.8,
                    num_outputs=request.num_outputs or 1,
                    num_inference_steps=request.num_inference_steps or 28,
                    guidance=request.guidance or 3.0,
                    aspect_ratio=request.aspect_ratio or "9:16",
                    megapixels=request.megapixels or "1",
                    speed_mode=request.speed_mode or "Juiced 🧃",
                    seed=request.seed,
                    wait=False
                )
            else:
                # Generic fallback via create_prediction (no wait arg)
                input_params = request.model_dump(
                    exclude_none=True, 
                    exclude={'model', 'model_name', 'thinking_level'}
                )
                if image_file_path:
                    input_params['image'] = await asyncio.to_thread(self.client.resolve_media_input, image_file_path)
                res = await asyncio.to_thread(self.client.create_prediction, model_name, input_params)

            prediction_id = res.get('id') if isinstance(res, dict) else None
            
            if prediction_id:
                await db.update_job(job_id, {'prediction_id': prediction_id, 'status': 'processing'})
                asyncio.create_task(self._poll_job(job_id, prediction_id, model_name))
            else:
                error_msg = res.get('error') or res.get('message') or 'No prediction ID returned from Pruna AI'
                await db.update_job(job_id, {'status': 'failed', 'error': str(error_msg)})
                
        except Exception as e:
            logger.error(f"Error in generate_image: {e}")
            await db.update_job(job_id, {'status': 'failed', 'error': str(e)})

    async def generate_video(
        self, 
        job_id: str, 
        request: VideoGenerateRequest, 
        image_path: Optional[str] = None, 
        last_frame_path: Optional[str] = None, 
        audio_path: Optional[str] = None
    ):
        if not self.client:
            await db.update_job(job_id, {'status': 'failed', 'error': 'PrunaClient not initialized. Check PRUNA_AI_API_KEY.'})
            return

        try:
            model_name = request.effective_model
            res = None

            if model_name == "p-video-2-pro":
                res = await asyncio.to_thread(
                    self.client.generate_video_2_pro,
                    prompt=request.prompt,
                    image=image_path,
                    last_frame_image=last_frame_path,
                    duration=request.duration or 5,
                    resolution=request.resolution or "768p",
                    mode=request.mode or "speed",
                    prompt_upsampler=request.prompt_upsampler or "turbo",
                    aspect_ratio=request.aspect_ratio or "9:16",
                    seed=request.seed,
                    wait=False
                )
            elif model_name == "p-video-2":
                res = await asyncio.to_thread(
                    self.client.generate_video_2,
                    prompt=request.prompt,
                    duration=request.duration or 5,
                    image=image_path,
                    last_frame_image=last_frame_path,
                    audio=audio_path,
                    resolution=request.resolution if request.resolution in ["720p", "1080p"] else "720p",
                    fps=request.fps or 24,
                    aspect_ratio=request.aspect_ratio or "9:16",
                    draft=request.draft or False,
                    save_audio=True if request.save_audio is not False else False,
                    prompt_upsampling=True if request.prompt_upsampling is not False else False,
                    disable_safety_filter=True if request.disable_safety_filter is not False else False,
                    seed=request.seed,
                    wait=False
                )
            else:
                # Generic fallback via create_prediction (no wait arg)
                input_params = request.model_dump(exclude_none=True, exclude={'model', 'model_name'})
                if image_path:
                    input_params['image'] = await asyncio.to_thread(self.client.resolve_media_input, image_path)
                if last_frame_path:
                    input_params['last_frame_image'] = await asyncio.to_thread(self.client.resolve_media_input, last_frame_path)
                if audio_path:
                    input_params['audio'] = await asyncio.to_thread(self.client.resolve_media_input, audio_path)
                res = await asyncio.to_thread(self.client.create_prediction, model_name, input_params)

            prediction_id = res.get('id') if isinstance(res, dict) else None
            
            if prediction_id:
                await db.update_job(job_id, {'prediction_id': prediction_id, 'status': 'processing'})
                asyncio.create_task(self._poll_job(job_id, prediction_id, model_name))
            else:
                error_msg = res.get('error') or res.get('message') or 'No prediction ID returned from Pruna AI'
                await db.update_job(job_id, {'status': 'failed', 'error': str(error_msg)})
                
        except Exception as e:
            logger.error(f"Error in generate_video: {e}")
            await db.update_job(job_id, {'status': 'failed', 'error': str(e)})

    async def edit_video(self, job_id: str, request: VideoEditRequest, video_path: str, image_paths: Optional[List[str]] = None):
        if not self.client:
            await db.update_job(job_id, {'status': 'failed', 'error': 'PrunaClient not initialized. Check PRUNA_AI_API_KEY.'})
            return

        try:
            res = await asyncio.to_thread(
                self.client.edit_video,
                video=video_path,
                prompt=request.prompt,
                images=image_paths,
                draft=request.draft or False,
                save_audio=True if request.save_audio is not False else False,
                prompt_upsampling=True if request.prompt_upsampling is not False else False,
                seed=request.seed,
                wait=False
            )

            prediction_id = res.get('id') if isinstance(res, dict) else None
            
            if prediction_id:
                await db.update_job(job_id, {'prediction_id': prediction_id, 'status': 'processing'})
                asyncio.create_task(self._poll_job(job_id, prediction_id, "p-video-edit"))
            else:
                error_msg = res.get('error') or res.get('message') or 'No prediction ID returned from Pruna AI'
                await db.update_job(job_id, {'status': 'failed', 'error': str(error_msg)})
                
        except Exception as e:
            logger.error(f"Error in edit_video: {e}")
            await db.update_job(job_id, {'status': 'failed', 'error': str(e)})

    async def get_status(self, prediction_id: str) -> dict:
        if not self.client:
            return {'error': 'PrunaClient not initialized'}
        return await asyncio.to_thread(self.client.get_prediction_status, prediction_id)

pruna_service = PrunaService()
