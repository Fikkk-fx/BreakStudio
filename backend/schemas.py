from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict, Any, Union
import json

class ImageGenerateRequest(BaseModel):
    model: Optional[str] = None
    model_name: Optional[str] = None
    prompt: str
    aspect_ratio: Optional[str] = '9:16'
    thinking: Optional[str] = None
    thinking_level: Optional[str] = None
    image_size: Optional[str] = None
    speed_mode: Optional[str] = None
    guidance: Optional[float] = None
    num_inference_steps: Optional[int] = None
    lora: Optional[str] = None
    lora_scale: Optional[float] = None
    seed: Optional[int] = None
    output_format: Optional[str] = None
    output_quality: Optional[int] = None
    extra_lora: Optional[str] = None
    extra_lora_scale: Optional[float] = None
    prompt_strength: Optional[float] = None
    num_outputs: Optional[int] = None
    megapixels: Optional[str] = None
    prompt_upsampling: Optional[bool] = None

    @property
    def effective_model(self) -> str:
        return self.model or self.model_name or 'p-image-ideogram'

    @property
    def effective_thinking(self) -> Optional[str]:
        return self.thinking or self.thinking_level

class VideoGenerateRequest(BaseModel):
    model: Optional[str] = None
    model_name: Optional[str] = None
    prompt: str
    duration: Optional[int] = 5
    resolution: Optional[str] = None
    mode: Optional[str] = None
    aspect_ratio: Optional[str] = None
    fps: Optional[int] = None
    draft: Optional[bool] = None
    seed: Optional[int] = None
    prompt_upsampler: Optional[str] = None
    save_audio: Optional[bool] = None
    prompt_upsampling: Optional[bool] = None
    disable_safety_filter: Optional[bool] = None

    @property
    def effective_model(self) -> str:
        return self.model or self.model_name or 'p-video-2-pro'

class VideoEditRequest(BaseModel):
    model: Optional[str] = 'p-video-edit'
    prompt: str
    draft: Optional[bool] = None
    seed: Optional[int] = None
    save_audio: Optional[bool] = None
    prompt_upsampling: Optional[bool] = None

def _parse_json_field(v: Any) -> Any:
    """Parse a field that may be a JSON string into a dict/list."""
    if isinstance(v, str):
        try:
            return json.loads(v)
        except (json.JSONDecodeError, ValueError):
            return v
    return v

class JobResponse(BaseModel):
    id: str
    type: str
    model: str
    prompt: str
    status: str
    params: Optional[Any] = None
    input_files: Optional[Any] = None
    prediction_id: Optional[str] = None
    output_url: Optional[str] = None
    output_path: Optional[str] = None
    error: Optional[str] = None
    created_at: str
    updated_at: str
    elapsed_seconds: Optional[float] = None

    @field_validator('params', 'input_files', mode='before')
    @classmethod
    def parse_json_strings(cls, v):
        return _parse_json_field(v)

class JobListResponse(BaseModel):
    jobs: List[JobResponse]
    data: List[JobResponse]
    total: int

class GalleryItem(BaseModel):
    id: str
    job_id: str
    type: str
    model: str
    prompt: str
    url: str
    thumbnail_url: Optional[str] = None
    output_path: Optional[str] = None
    created_at: str
    elapsed_seconds: Optional[float] = None

class GalleryResponse(BaseModel):
    items: List[GalleryItem]
    data: List[GalleryItem]
    total: int

class StatusResponse(BaseModel):
    status: str
    message: str
