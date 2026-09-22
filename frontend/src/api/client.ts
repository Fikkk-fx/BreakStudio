import axios from 'axios';
import { Job, GalleryItem } from '../types';

// Support runtime API base URL for production backend
// Set VITE_API_BASE_URL env var to point to your deployed backend
// e.g. VITE_API_BASE_URL=https://your-backend.railway.app
const API_BASE = import.meta.env.VITE_API_BASE_URL || '';

const api = axios.create({
  baseURL: `${API_BASE}/api`,
});

export const generateImage = async (data: any, imageFile?: File): Promise<Job> => {
  const formData = new FormData();
  formData.append('data', JSON.stringify(data));
  if (imageFile) formData.append('image', imageFile);
  const response = await api.post<Job>('/generate/image', formData);
  return response.data;
};

export const generateVideo = async (data: any, imageFile?: File, lastFrameFile?: File, audioFile?: File): Promise<Job> => {
  const formData = new FormData();
  formData.append('data', JSON.stringify(data));
  if (imageFile) formData.append('image', imageFile);
  if (lastFrameFile) formData.append('last_frame_image', lastFrameFile);
  if (audioFile) formData.append('audio', audioFile);
  const response = await api.post<Job>('/generate/video', formData);
  return response.data;
};

export const editVideo = async (data: any, videoFile: File, imageFiles?: File[]): Promise<Job> => {
  const formData = new FormData();
  formData.append('data', JSON.stringify(data));
  formData.append('video', videoFile);
  if (imageFiles) {
    imageFiles.forEach(file => formData.append('images', file));
  }
  const response = await api.post<Job>('/generate/edit-video', formData);
  return response.data;
};

// FIX BUG 2: endpoint was '/upload', correct path is '/generate/upload'
export const uploadFile = async (file: File): Promise<{ url: string }> => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await api.post<{ url: string }>('/generate/upload', formData);
  return response.data;
};

export const getJobs = async (params?: any): Promise<{ data: Job[], total: number }> => {
  const response = await api.get('/jobs', { params });
  return response.data;
};

export const getJob = async (id: string): Promise<Job> => {
  const response = await api.get<Job>(`/jobs/${id}`);
  return response.data;
};

export const deleteJob = async (id: string): Promise<void> => {
  await api.delete(`/jobs/${id}`);
};

export const getGallery = async (params?: any): Promise<{ data: GalleryItem[], total: number }> => {
  const response = await api.get('/gallery', { params });
  return response.data;
};

export const downloadGalleryItem = (id: string): void => {
  window.open(`${API_BASE}/api/gallery/${id}/download`, '_blank');
};

export const deleteGalleryItem = async (id: string): Promise<void> => {
  await api.delete(`/gallery/${id}`);
};
