import { useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import ImageGenPage from './pages/ImageGenPage';
import VideoGenPage from './pages/VideoGenPage';
import VideoEditPage from './pages/VideoEditPage';
import GalleryPage from './pages/GalleryPage';
import JobsPage from './pages/JobsPage';
import { useJobStore } from './stores/jobStore';

export default function App() {
  const refreshJobs = useJobStore(state => state.refreshJobs);

  useEffect(() => {
    refreshJobs();
    const interval = setInterval(refreshJobs, 10000);
    return () => clearInterval(interval);
  }, [refreshJobs]);

  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Navigate to="/image" replace />} />
        <Route path="image" element={<ImageGenPage />} />
        <Route path="video" element={<VideoGenPage />} />
        <Route path="edit" element={<VideoEditPage />} />
        <Route path="gallery" element={<GalleryPage />} />
        <Route path="jobs" element={<JobsPage />} />
      </Route>
    </Routes>
  );
}
