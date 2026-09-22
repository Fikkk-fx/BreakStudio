import { useState } from 'react';
import PromptEditor from '../components/PromptEditor';
import JobStatusCard from '../components/JobStatusCard';
import FileUploader from '../components/FileUploader';
import { editVideo } from '../api/client';
import { Job, VideoEditRequest } from '../types';
import { useJobStore } from '../stores/jobStore';
import { Plus, X } from 'lucide-react';

export default function VideoEditPage() {
  const [model] = useState('p-video-edit');
  const [prompt, setPrompt] = useState('');
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [referenceImages, setReferenceImages] = useState<(File | null)[]>([null]);
  const [draft, setDraft] = useState(false);
  const [seed, setSeed] = useState<number | undefined>();
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [currentJob, setCurrentJob] = useState<Job | null>(null);

  const addJob = useJobStore(state => state.addJob);

  const handleImageChange = (index: number, file: File | null) => {
    const newImages = [...referenceImages];
    newImages[index] = file;
    setReferenceImages(newImages);
  };

  const addImageField = () => {
    if (referenceImages.length < 4) {
      setReferenceImages([...referenceImages, null]);
    }
  };

  const removeImageField = (index: number) => {
    const newImages = [...referenceImages];
    newImages.splice(index, 1);
    setReferenceImages(newImages.length ? newImages : [null]);
  };

  const handleSubmit = async () => {
    if (!prompt || !videoFile) return;
    setIsSubmitting(true);
    try {
      const data: VideoEditRequest = { model, prompt, draft, seed };
      const validImages = referenceImages.filter(f => f !== null) as File[];
      
      const job = await editVideo(data, videoFile, validImages.length ? validImages : undefined);
      setCurrentJob(job);
      addJob(job);
    } catch (error) {
      console.error(error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto flex flex-col gap-8 pb-10">
      <header>
        <h1 className="text-3xl font-bold">✂️ Video Editing</h1>
        <p className="text-zinc-400 mt-2">Modify existing videos with text instructions and reference images.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 flex flex-col gap-6">
          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-4">
            <FileUploader accept="video/*" onFileSelected={setVideoFile} label="Source Video (Required)" />

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Edit Instructions</label>
              <PromptEditor value={prompt} onChange={setPrompt} placeholder="E.g., Make it look like watercolor animation..." />
            </div>

            <div>
              <div className="flex justify-between items-center mb-2">
                <label className="text-sm font-medium text-zinc-300">Reference Images (Up to 4)</label>
                {referenceImages.length < 4 && (
                  <button onClick={addImageField} className="text-xs flex items-center gap-1 text-indigo-400 hover:text-indigo-300">
                    <Plus size={14} /> Add Image
                  </button>
                )}
              </div>
              <div className="grid grid-cols-2 gap-4">
                {referenceImages.map((_, index) => (
                  <div key={index} className="relative">
                    <FileUploader accept="image/*" onFileSelected={(f) => handleImageChange(index, f)} label={`Image ${index + 1}`} />
                    {referenceImages.length > 1 && (
                      <button onClick={() => removeImageField(index)} className="absolute -top-2 -right-2 bg-red-500 rounded-full p-1 text-white hover:bg-red-600">
                        <X size={12} />
                      </button>
                    )}
                  </div>
                ))}
              </div>
            </div>

            <button 
              onClick={handleSubmit} 
              disabled={!prompt || !videoFile || isSubmitting}
              className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-medium py-3 rounded-lg transition-colors mt-2"
            >
              {isSubmitting ? 'Processing...' : 'Apply Edit'}
            </button>
          </div>

          {currentJob && (
            <div>
              <h2 className="text-xl font-bold mb-4">Current Edit Job</h2>
              <JobStatusCard job={currentJob} />
            </div>
          )}
        </div>

        <div className="flex flex-col gap-6">
          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-5">
            <h3 className="font-semibold text-lg border-b border-zinc-800 pb-3">Edit Settings</h3>
            
            <div className="flex items-center gap-2">
              <input type="checkbox" id="draft" checked={draft} onChange={(e) => setDraft(e.target.checked)} className="w-4 h-4 rounded bg-zinc-800 border-zinc-700" />
              <label htmlFor="draft" className="text-sm text-zinc-300">Draft Quality (Faster)</label>
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Seed (Optional)</label>
              <input type="number" className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" placeholder="Random" value={seed || ''} onChange={(e) => setSeed(e.target.value ? Number(e.target.value) : undefined)} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
