from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
import json
from .. import database as db

router = APIRouter(prefix="/ws", tags=["websocket"])

@router.websocket("/jobs/{job_id}")
async def websocket_job_status(websocket: WebSocket, job_id: str):
    await websocket.accept()
    try:
        while True:
            job = await db.get_job(job_id)
            if not job:
                await websocket.send_json({"error": "Job not found"})
                break
                
            await websocket.send_json({
                "id": job["id"],
                "status": job["status"],
                "prediction_id": job.get("prediction_id"),
                "error": job.get("error"),
                "output_url": job.get("output_url"),
                "output_path": job.get("output_path"),
                "elapsed_seconds": job.get("elapsed_seconds")
            })
            
            if job["status"] in ["succeeded", "failed", "deleted"]:
                break
                
            await asyncio.sleep(2.0)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        try:
            await websocket.send_json({"error": str(e)})
        except:
            pass
    finally:
        try:
            await websocket.close()
        except:
            pass
