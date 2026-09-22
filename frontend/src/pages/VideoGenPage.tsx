import { useState } from 'react';
import PromptEditor from '../components/PromptEditor';
import JobStatusCard from '../components/JobStatusCard';
import FileUploader from '../components/FileUploader';
import { generateVideo } from '../api/client';
import { Job, VideoGenerateRequest } from '../types';
import { useJobStore } from '../stores/jobStore';

export default function VideoGenPage() {
  const [model, setModel] = useState('p-video-2-pro');
  const [prompt, setPrompt] = useState('');
  const [aspectRatio, setAspectRatio] = useState('16:9');
  const [seed, setSeed] = useState<number | undefined>();
  const [duration, setDuration] = useState(5);
  const [resolution, setResolution] = useState('720p');
  const [mode, setMode] = useState('quality');
  const [promptUpsampler, setPromptUpsampler] = useState('none');
  const [fps, setFps] = useState(24);
  const [draft, setDraft] = useState(false);
  
  const [firstFrame, setFirstFrame] = useState<File | null>(null);
  const [lastFrame, setLastFrame] = useState<File | null>(null);
  const [audioFile, setAudioFile] = useState<File | null>(null);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [currentJob, setCurrentJob] = useState<Job | null>(null);

  const addJob = useJobStore(state => state.addJob);

  const handleSubmit = async () => {
    if (!prompt) return;
    setIsSubmitting(true);
    try {
      const data: VideoGenerateRequest = { model, prompt, aspect_ratio: aspectRatio, seed };
      if (model === 'p-video-2-pro') {
        data.duration = duration;
        data.resolution = resolution;
        data.mode = mode;
        data.prompt_upsampler = promptUpsampler;
      } else if (model === 'p-video-2') {
        data.duration = duration;
        data.resolution = resolution;
        data.fps = fps;
        data.draft = draft;
      }

      const job = await generateVideo(data, firstFrame || undefined, lastFrame || undefined, audioFile || undefined);
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
        <h1 className="text-3xl font-bold">🎥 Video Generation</h1>
        <p className="text-zinc-400 mt-2">Create stunning videos from text and images.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 flex flex-col gap-6">
          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-4">
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Model</label>
              <select className="w-full bg-zinc-800 border border-zinc-700 text-white rounded-lg p-3 focus:outline-none focus:border-indigo-500" value={model} onChange={(e) => setModel(e.target.value)}>
                <option value="p-video-2-pro">p-video-2-pro</option>
                <option value="p-video-2">p-video-2</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Prompt</label>
              <PromptEditor value={prompt} onChange={setPrompt} placeholder="Describe the video action..." />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <FileUploader accept="image/*" onFileSelected={setFirstFrame} label="First Frame (Optional)" />
              <FileUploader accept="image/*" onFileSelected={setLastFrame} label="Last Frame (Optional)" />
            </div>

            <button 
              onClick={handleSubmit} 
              disabled={!prompt || isSubmitting}
              className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-medium py-3 rounded-lg transition-colors mt-2"
            >
              {isSubmitting ? 'Generating...' : 'Generate Video'}
            </button>
          </div>

          {currentJob && (
            <div>
              <h2 className="text-xl font-bold mb-4">Current Generation</h2>
              <JobStatusCard job={currentJob} />
            </div>
          )}
        </div>

        <div className="flex flex-col gap-6">
          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-5">
            <h3 className="font-semibold text-lg border-b border-zinc-800 pb-3">Common Settings</h3>
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Aspect Ratio</label>
              <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={aspectRatio} onChange={(e) => setAspectRatio(e.target.value)}>
                <option value="16:9">16:9 Landscape</option>
                <option value="9:16">9:16 Portrait</option>
                <option value="1:1">1:1 Square</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Seed</label>
              <input type="number" className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" placeholder="Random" value={seed || ''} onChange={(e) => setSeed(e.target.value ? Number(e.target.value) : undefined)} />
            </div>
          </div>

          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-5">
            <h3 className="font-semibold text-lg border-b border-zinc-800 pb-3">Model Specific</h3>
            
            {model === 'p-video-2-pro' && (
              <>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Duration ({duration}s)</label>
                  <input type="range" min="5" max="15" step="1" value={duration} onChange={(e) => setDuration(Number(e.target.value))} className="w-full" />
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Resolution</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={resolution} onChange={(e) => setResolution(e.target.value)}>
                    <option value="480p">480p</option>
                    <option value="768p">768p</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Mode</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={mode} onChange={(e) => setMode(e.target.value)}>
                    <option value="quality">Quality</option>
                    <option value="speed">Speed</option>
                    <option value="cost">Cost</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Prompt Upsampler</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={promptUpsampler} onChange={(e) => setPromptUpsampler(e.target.value)}>
                    <option value="none">None</option>
                    <option value="standard">Standard</option>
                  </select>
                </div>
              </>
            )}

            {model === 'p-video-2' && (
              <>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Duration ({duration}s)</label>
                  <input type="range" min="1" max="20" step="1" value={duration} onChange={(e) => setDuration(Number(e.target.value))} className="w-full" />
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Resolution</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={resolution} onChange={(e) => setResolution(e.target.value)}>
                    <option value="720p">720p</option>
                    <option value="1080p">1080p</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">FPS</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={fps.toString()} onChange={(e) => setFps(Number(e.target.value))}>
                    <option value="24">24</option>
                    <option value="48">48</option>
                  </select>
                </div>
                <div className="flex items-center gap-2">
                  <input type="checkbox" id="draft" checked={draft} onChange={(e) => setDraft(e.target.checked)} className="w-4 h-4 rounded bg-zinc-800 border-zinc-700" />
                  <label htmlFor="draft" className="text-sm text-zinc-300">Draft Mode</label>
                </div>
                <FileUploader accept="audio/*" onFileSelected={setAudioFile} label="Audio Track (Optional)" preview={false} />
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
