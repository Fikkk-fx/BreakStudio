from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import os
from ..schemas import JobListResponse, JobResponse, StatusResponse
from .. import database as db
from ..config import settings, BACKEND_DIR

router = APIRouter(prefix="/api/jobs", tags=["jobs"])

@router.get("/", response_model=JobListResponse)
async def list_jobs(
    type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    jobs = await db.list_jobs(type_filter=type, status_filter=status, limit=limit, offset=offset)
    total = await db.count_jobs(type_filter=type, status_filter=status)
    return {"jobs": jobs, "data": jobs, "total": total}

@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: str):
    job = await db.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.delete("/{job_id}", response_model=StatusResponse)
async def delete_job(job_id: str):
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
                
    await db.delete_job(job_id)
    return {"status": "success", "message": "Job deleted"}
