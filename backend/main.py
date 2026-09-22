from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
from contextlib import asynccontextmanager

from .config import settings
from .database import init_db
from .routes import generate, jobs, gallery, ws

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create directories before mounting static files
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
    await init_db()
    yield

app = FastAPI(title="BreakStudio API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure dirs exist before mounting (startup may not have run yet during import)
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.OUTPUT_DIR, exist_ok=True)

app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
app.mount("/outputs", StaticFiles(directory=settings.OUTPUT_DIR), name="outputs")

app.include_router(generate.router)
app.include_router(jobs.router)
app.include_router(gallery.router)
app.include_router(ws.router)

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "BreakStudio"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
