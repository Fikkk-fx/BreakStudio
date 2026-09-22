import { useState } from 'react';
import PromptEditor from '../components/PromptEditor';
import JobStatusCard from '../components/JobStatusCard';
import FileUploader from '../components/FileUploader';
import { generateImage } from '../api/client';
import { Job, ImageGenerateRequest } from '../types';
import { useJobStore } from '../stores/jobStore';

export default function ImageGenPage() {
  const [model, setModel] = useState('p-image-ideogram');
  const [prompt, setPrompt] = useState('');
  const [aspectRatio, setAspectRatio] = useState('1:1');
  const [seed, setSeed] = useState<number | undefined>();
  const [thinkingLevel, setThinkingLevel] = useState('low');
  const [imageSize, setImageSize] = useState('1K');
  const [promptUpsampling, setPromptUpsampling] = useState(true);
  const [speedMode, setSpeedMode] = useState('fast');
  const [numInferenceSteps, setNumInferenceSteps] = useState(20);
  const [guidance, setGuidance] = useState(3.5);
  const [lora, setLora] = useState('');
  const [loraScale, setLoraScale] = useState(0.8);
  const [referenceImage, setReferenceImage] = useState<File | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [currentJob, setCurrentJob] = useState<Job | null>(null);

  const addJob = useJobStore(state => state.addJob);

  const handleSubmit = async () => {
    if (!prompt) return;
    setIsSubmitting(true);
    try {
      const data: ImageGenerateRequest = { model, prompt, aspect_ratio: aspectRatio, seed };
      if (model === 'p-image-ideogram') {
        data.thinking_level = thinkingLevel;
        data.image_size = imageSize;
        data.prompt_upsampling = promptUpsampling;
      } else if (model === 'flux-dev') {
        data.speed_mode = speedMode;
        data.num_inference_steps = numInferenceSteps;
        data.guidance = guidance;
      } else if (model === 'flux-dev-lora') {
        data.lora = lora;
        data.lora_scale = loraScale;
      }

      const job = await generateImage(data, referenceImage || undefined);
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
        <h1 className="text-3xl font-bold">🖼️ Image Generation</h1>
        <p className="text-zinc-400 mt-2">Generate high-quality images using various models.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 flex flex-col gap-6">
          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-4">
            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Model</label>
              <select 
                className="w-full bg-zinc-800 border border-zinc-700 text-white rounded-lg p-3 focus:outline-none focus:border-indigo-500"
                value={model} onChange={(e) => setModel(e.target.value)}
              >
                <option value="p-image-ideogram">p-image-ideogram</option>
                <option value="flux-dev">flux-dev</option>
                <option value="flux-dev-lora">flux-dev-lora</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Prompt</label>
              <PromptEditor value={prompt} onChange={setPrompt} placeholder="Describe the image you want to generate..." />
            </div>

            <button 
              onClick={handleSubmit} 
              disabled={!prompt || isSubmitting}
              className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 disabled:hover:bg-indigo-600 text-white font-medium py-3 rounded-lg transition-colors mt-2"
            >
              {isSubmitting ? 'Submitting...' : 'Generate Image'}
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
              <div className="flex flex-wrap gap-2">
                {['1:1', '16:9', '9:16', '4:3', '3:4'].map(ratio => (
                  <button 
                    key={ratio}
                    onClick={() => setAspectRatio(ratio)}
                    className={`px-3 py-1.5 rounded border text-sm font-medium transition-colors ${
                      aspectRatio === ratio ? 'bg-indigo-600 border-indigo-500 text-white' : 'bg-zinc-800 border-zinc-700 text-zinc-300 hover:bg-zinc-700'
                    }`}
                  >
                    {ratio}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-zinc-300 mb-2">Seed (Optional)</label>
              <input 
                type="number" 
                className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" 
                placeholder="Random"
                value={seed || ''}
                onChange={(e) => setSeed(e.target.value ? Number(e.target.value) : undefined)}
              />
            </div>
          </div>

          <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-5">
            <h3 className="font-semibold text-lg border-b border-zinc-800 pb-3">Model Specific</h3>
            
            {model === 'p-image-ideogram' && (
              <>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Thinking Level</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={thinkingLevel} onChange={(e) => setThinkingLevel(e.target.value)}>
                    <option value="low">Low</option>
                    <option value="high">High</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Image Size</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={imageSize} onChange={(e) => setImageSize(e.target.value)}>
                    <option value="1K">1K</option>
                    <option value="2K">2K</option>
                  </select>
                </div>
                <div className="flex items-center gap-2 mt-2">
                  <input type="checkbox" id="upsampling" checked={promptUpsampling} onChange={(e) => setPromptUpsampling(e.target.checked)} className="w-4 h-4 rounded bg-zinc-800 border-zinc-700 text-indigo-600 focus:ring-indigo-600 focus:ring-offset-zinc-900" />
                  <label htmlFor="upsampling" className="text-sm text-zinc-300">Prompt Upsampling</label>
                </div>
              </>
            )}

            {model === 'flux-dev' && (
              <>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Speed Mode</label>
                  <select className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" value={speedMode} onChange={(e) => setSpeedMode(e.target.value)}>
                    <option value="fast">Fast</option>
                    <option value="quality">Quality</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Inference Steps ({numInferenceSteps})</label>
                  <input type="range" min="1" max="50" value={numInferenceSteps} onChange={(e) => setNumInferenceSteps(Number(e.target.value))} className="w-full" />
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">Guidance ({guidance})</label>
                  <input type="range" min="1" max="10" step="0.1" value={guidance} onChange={(e) => setGuidance(Number(e.target.value))} className="w-full" />
                </div>
              </>
            )}

            {model === 'flux-dev-lora' && (
              <>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">LoRA Reference</label>
                  <input type="text" className="w-full bg-zinc-800 border border-zinc-700 rounded p-2 text-white" placeholder="Model ID" value={lora} onChange={(e) => setLora(e.target.value)} />
                </div>
                <div>
                  <label className="block text-sm text-zinc-300 mb-1">LoRA Scale ({loraScale})</label>
                  <input type="range" min="0" max="1" step="0.05" value={loraScale} onChange={(e) => setLoraScale(Number(e.target.value))} className="w-full" />
                </div>
                <FileUploader accept="image/*" onFileSelected={setReferenceImage} label="Reference Image" />
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
