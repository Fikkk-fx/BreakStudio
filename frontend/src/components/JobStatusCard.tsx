import { Job } from '../types';
import { useJobStatus } from '../api/websocket';
import { Download } from 'lucide-react';

interface JobStatusCardProps {
  job: Job;
  onViewResult?: (url: string) => void;
  onRerun?: () => void;
}

export default function JobStatusCard({ job, onViewResult, onRerun }: JobStatusCardProps) {
  const isTerminal = job.status === 'succeeded' || job.status === 'failed';
  const { status, elapsedSeconds, error, outputUrl } = useJobStatus(isTerminal ? null : job.id);

  const displayStatus = status || job.status;
  const displayElapsed = elapsedSeconds !== null ? elapsedSeconds : job.elapsed_seconds;
  const displayError = error || job.error;
  const displayOutput = outputUrl || job.output_url;

  const statusColors = {
    pending: 'bg-yellow-500/20 text-yellow-500 border-yellow-500/50',
    processing: 'bg-blue-500/20 text-blue-400 border-blue-500/50',
    succeeded: 'bg-green-500/20 text-green-400 border-green-500/50',
    failed: 'bg-red-500/20 text-red-400 border-red-500/50',
  };

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-5 flex flex-col gap-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <span className="px-2.5 py-1 bg-zinc-800 text-zinc-300 text-xs font-semibold rounded-md uppercase tracking-wider">
            {job.model}
          </span>
          <span className={`px-3 py-1 text-xs font-medium rounded-full border ${statusColors[displayStatus as keyof typeof statusColors]} flex items-center gap-2`}>
            {displayStatus === 'processing' && <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>}
            {displayStatus.charAt(0).toUpperCase() + displayStatus.slice(1)}
          </span>
        </div>
        {displayElapsed !== null && (
          <span className="text-sm text-zinc-500 font-mono">{displayElapsed.toFixed(1)}s</span>
        )}
      </div>

      <p className="text-sm text-zinc-400 line-clamp-2 italic">"{job.prompt}"</p>

      {displayStatus === 'failed' && displayError && (
        <div className="bg-red-500/10 border border-red-500/20 rounded p-3 text-sm text-red-400">
          {displayError}
        </div>
      )}

      {displayStatus === 'succeeded' && displayOutput && (
        <div className="mt-2 flex flex-col gap-3">
          <div className="bg-zinc-950 rounded-lg overflow-hidden border border-zinc-800 flex justify-center items-center">
            {job.type === 'image' ? (
              <img src={displayOutput} alt="Result" className="max-h-64 object-contain" />
            ) : (
              <video src={displayOutput} controls className="max-h-64 object-contain w-full" />
            )}
          </div>
          <div className="flex gap-2">
            <a 
              href={displayOutput} 
              download 
              target="_blank"
              rel="noopener noreferrer"
              className="flex-1 flex items-center justify-center gap-2 bg-zinc-800 hover:bg-zinc-700 text-white py-2 rounded-lg transition-colors text-sm font-medium"
            >
              <Download size={16} /> Download
            </a>
            {onViewResult && (
              <button 
                onClick={() => onViewResult(displayOutput)}
                className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-lg transition-colors text-sm font-medium"
              >
                View Full
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
