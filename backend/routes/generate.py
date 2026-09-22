from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, BackgroundTasks
import json
import uuid
import os
import asyncio
from typing import Optional, List
from ..schemas import ImageGenerateRequest, VideoGenerateRequest, VideoEditRequest, JobResponse
from .. import database as db
from ..pruna_service import pruna_service
from ..config import settings

router = APIRouter(prefix="/api/generate", tags=["generate"])

async def save_upload_file(upload_file: UploadFile) -> Optional[str]:
    if not upload_file or not upload_file.filename:
        return None
    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{upload_file.filename}"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)
    content = await upload_file.read()
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path

@router.post("/image", response_model=JobResponse)
async def generate_image(
    background_tasks: BackgroundTasks,
    request: Optional[str] = Form(None),
    data: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    raw_json = request or data
    if not raw_json:
        raise HTTPException(status_code=400, detail="Missing request/data form parameter")
    try:
        req_data = json.loads(raw_json)
        req_obj = ImageGenerateRequest(**req_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request JSON: {str(e)}")

    job_id = str(uuid.uuid4())
    
    image_path = None
    input_files = {}
    if image and image.filename:
        image_path = await save_upload_file(image)
        if image_path:
            input_files['image'] = image_path

    model_name = req_obj.effective_model
    job_data = {
        'id': job_id,
        'type': 'image',
        'model': model_name,
        'prompt': req_obj.prompt,
        'status': 'pending',
        'params': json.dumps(req_obj.model_dump()),
        'input_files': json.dumps(input_files)
    }
    
    created_job = await db.create_job(job_data)
    
    background_tasks.add_task(
        pruna_service.generate_image,
        job_id=job_id,
        request=req_obj,
        image_file_path=image_path
    )
    
    return created_job

@router.post("/video", response_model=JobResponse)
async def generate_video(
    background_tasks: BackgroundTasks,
    request: Optional[str] = Form(None),
    data: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    last_frame_image: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None)
):
    raw_json = request or data
    if not raw_json:
        raise HTTPException(status_code=400, detail="Missing request/data form parameter")
    try:
        req_data = json.loads(raw_json)
        req_obj = VideoGenerateRequest(**req_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request JSON: {str(e)}")

    job_id = str(uuid.uuid4())
    
    image_path = await save_upload_file(image) if image and image.filename else None
    last_frame_path = await save_upload_file(last_frame_image) if last_frame_image and last_frame_image.filename else None
    audio_path = await save_upload_file(audio) if audio and audio.filename else None
    
    input_files = {}
    if image_path: input_files['image'] = image_path
    if last_frame_path: input_files['last_frame_image'] = last_frame_path
    if audio_path: input_files['audio'] = audio_path

    model_name = req_obj.effective_model
    job_data = {
        'id': job_id,
        'type': 'video',
        'model': model_name,
        'prompt': req_obj.prompt,
        'status': 'pending',
        'params': json.dumps(req_obj.model_dump()),
        'input_files': json.dumps(input_files)
    }
    
    created_job = await db.create_job(job_data)
    
    background_tasks.add_task(
        pruna_service.generate_video,
        job_id=job_id,
        request=req_obj,
        image_path=image_path,
        last_frame_path=last_frame_path,
        audio_path=audio_path
    )
    
    return created_job

@router.post("/edit-video", response_model=JobResponse)
async def edit_video(
    background_tasks: BackgroundTasks,
    request: Optional[str] = Form(None),
    data: Optional[str] = Form(None),
    video: UploadFile = File(...),
    images: List[UploadFile] = File(default=[])
):
    raw_json = request or data
    if not raw_json:
        raise HTTPException(status_code=400, detail="Missing request/data form parameter")
    try:
        req_data = json.loads(raw_json)
        req_obj = VideoEditRequest(**req_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request JSON: {str(e)}")

    job_id = str(uuid.uuid4())
    
    video_path = await save_upload_file(video)
    image_paths = []
    for img in images[:4]:
        if img.filename:
            p = await save_upload_file(img)
            if p:
                image_paths.append(p)
            
    input_files = {'video': video_path}
    if image_paths:
        input_files['images'] = image_paths

    job_data = {
        'id': job_id,
        'type': 'edit-video',
        'model': 'p-video-edit',
        'prompt': req_obj.prompt,
        'status': 'pending',
        'params': json.dumps(req_obj.model_dump()),
        'input_files': json.dumps(input_files)
    }
    
    created_job = await db.create_job(job_data)
    
    background_tasks.add_task(
        pruna_service.edit_video,
        job_id=job_id,
        request=req_obj,
        video_path=video_path,
        image_paths=image_paths if image_paths else None
    )
    
    return created_job

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    path = await save_upload_file(file)
    if not path:
        raise HTTPException(status_code=400, detail="Invalid file")
    filename = os.path.basename(path)
    return {
        "filename": file.filename,
        "path": path,
        "url": f"/uploads/{filename}"
    }
