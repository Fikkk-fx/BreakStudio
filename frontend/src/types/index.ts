export interface Job {
  id: string;
  type: 'image' | 'video' | 'edit-video';
  model: string;
  prompt: string;
  status: 'pending' | 'processing' | 'succeeded' | 'failed' | 'deleted';
  // params & input_files may arrive as parsed object or raw JSON string
  params: Record<string, any> | string | null;
  input_files: Record<string, string> | string | null;
  prediction_id: string | null;
  output_url: string | null;
  output_path: string | null;
  error: string | null;
  created_at: string;
  updated_at: string;
  elapsed_seconds: number | null;
}

export interface GalleryItem {
  id: string;
  job_id: string;
  type: 'image' | 'video';
  url: string;
  thumbnail_url?: string;
  prompt: string;
  model: string;
  output_path?: string | null;
  elapsed_seconds?: number | null;
  created_at: string;
}

export interface ImageGenerateRequest {
  model: string;
  prompt: string;
  aspect_ratio?: string;
  seed?: number;
  output_format?: string;
  output_quality?: number;
  thinking_level?: string;
  image_size?: string;
  prompt_upsampling?: boolean;
  speed_mode?: string;
  num_inference_steps?: number;
  guidance?: number;
  lora?: string;
  lora_scale?: number;
}

export interface VideoGenerateRequest {
  model: string;
  prompt: string;
  duration?: number;
  resolution?: string;
  mode?: string;
  prompt_upsampler?: string;
  fps?: number;
  draft?: boolean;
  aspect_ratio?: string;
  seed?: number;
}

export interface VideoEditRequest {
  model: string;
  prompt: string;
  draft?: boolean;
  seed?: number;
}

// Helper to safely parse params/input_files which may be JSON string or object
export function parseJobField<T>(field: T | string | null | undefined): T | null {
  if (field === null || field === undefined) return null;
  if (typeof field === 'string') {
    try {
      return JSON.parse(field) as T;
    } catch {
      return null;
    }
  }
  return field as T;
}
