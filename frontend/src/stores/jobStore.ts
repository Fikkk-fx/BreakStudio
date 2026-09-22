import { create } from 'zustand';
import { Job } from '../types';
import { getJobs } from '../api/client';

interface JobStore {
  activeJobs: Job[];
  addJob: (job: Job) => void;
  updateJob: (id: string, updates: Partial<Job>) => void;
  removeJob: (id: string) => void;
  refreshJobs: () => Promise<void>;
}

export const useJobStore = create<JobStore>((set) => ({
  activeJobs: [],
  addJob: (job) => set((state) => ({ activeJobs: [job, ...state.activeJobs] })),
  updateJob: (id, updates) => set((state) => ({
    activeJobs: state.activeJobs.map((j) => (j.id === id ? { ...j, ...updates } : j)),
  })),
  removeJob: (id) => set((state) => ({
    activeJobs: state.activeJobs.filter((j) => j.id !== id),
  })),
  refreshJobs: async () => {
    try {
      const response = await getJobs({ status: 'pending,processing' });
      set({ activeJobs: response.data || [] });
    } catch (error) {
      console.error('Failed to fetch active jobs', error);
    }
  },
}));
