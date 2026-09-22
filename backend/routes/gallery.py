from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from typing import Optional, List
import os
from ..schemas import GalleryItem, GalleryResponse, StatusResponse
from .. import database as db
from ..config import settings, BACKEND_DIR

router = APIRouter(prefix="/api/gallery", tags=["gallery"])

@router.get("/", response_model=GalleryResponse)
async def list_gallery(
    type: Optional[str] = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    jobs = await db.get_gallery(type_filter=type, limit=limit, offset=offset)
    total = await db.count_jobs(type_filter=type, status_filter='succeeded')
    items = []
    for job in jobs:
        prompt_trunc = job['prompt'][:100] + "..." if job['prompt'] and len(job['prompt']) > 100 else (job['prompt'] or "")
        rel_path = job.get('output_path') or ''
        normalized_path = rel_path.replace('\\', '/') if rel_path else ''
        url = f"/{normalized_path}" if normalized_path else (job.get('output_url') or '')
        
        items.append(GalleryItem(
            id=job['id'],
            job_id=job['id'],
            type=job['type'],
            model=job['model'],
            prompt=prompt_trunc,
            url=url,
            thumbnail_url=url if job['type'] == 'image' else None,
            output_path=job.get('output_path'),
            created_at=job['created_at'],
            elapsed_seconds=job.get('elapsed_seconds')
        ))
    return {"items": items, "data": items, "total": total}

@router.get("/{job_id}/download")
async def download_gallery_item(job_id: str):
    job = await db.get_job(job_id)
    if not job or not job.get('output_path'):
        raise HTTPException(status_code=404, detail="File not found")
        
    full_path = os.path.join(BACKEND_DIR, job['output_path'])
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found on disk")
        
    filename = os.path.basename(full_path)
    return FileResponse(path=full_path, filename=filename)

@router.delete("/{job_id}", response_model=StatusResponse)
async def delete_gallery_item(job_id: str):
    job = await db.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
        
    if job.get('output_path'):
        full_path = os.path.join(BACKEND_DIR, job['output_path'])
        if os.path.exists(full_path):
            try:
                os.remove(full_path)
            except Exception:
                pass
                
    await db.update_job(job_id, {'output_path': None, 'output_url': None, 'status': 'deleted'})
    return {"status": "success", "message": "Gallery item deleted"}
