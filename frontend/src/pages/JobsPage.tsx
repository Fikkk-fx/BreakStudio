import React, { useState, useEffect, useCallback } from 'react';
import { getJobs, deleteJob } from '../api/client';
import { Job, parseJobField } from '../types';
import { formatDistanceToNow } from 'date-fns';
import { Trash2, ChevronDown, ChevronUp, RefreshCw } from 'lucide-react';
import JobStatusCard from '../components/JobStatusCard';


export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);
  const [typeFilter, setTypeFilter] = useState<string>('all');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [expandedJobId, setExpandedJobId] = useState<string | null>(null);
  const [page, setPage] = useState(1);
  const limit = 20;

  const loadJobs = async () => {
    try {
      const params: any = { limit, offset: (page - 1) * limit };
      if (typeFilter !== 'all') params.type = typeFilter;
      if (statusFilter !== 'all') params.status = statusFilter;
      
      const res = await getJobs(params);
      setJobs(res.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    loadJobs();
  }, [typeFilter, statusFilter, page]);

  useEffect(() => {
    // Auto refresh every 10s if there are pending/processing jobs
    const hasActive = jobs.some(j => j.status === 'pending' || j.status === 'processing');
    if (!hasActive) return;
    
    const interval = setInterval(loadJobs, 10000);
    return () => clearInterval(interval);
  }, [jobs]);

  const handleDelete = async (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!confirm('Delete this job record?')) return;
    try {
      await deleteJob(id);
      setJobs(jobs.filter(j => j.id !== id));
    } catch (err) {
      console.error(err);
    }
  };

  const statusColors = {
    pending: 'bg-yellow-500/20 text-yellow-500 border-yellow-500/50',
    processing: 'bg-blue-500/20 text-blue-400 border-blue-500/50',
    succeeded: 'bg-green-500/20 text-green-400 border-green-500/50',
    failed: 'bg-red-500/20 text-red-400 border-red-500/50',
  };

  return (
    <div className="max-w-6xl mx-auto flex flex-col gap-6 pb-10">
      <header className="flex flex-col md:flex-row justify-between items-start md:items-end gap-4">
        <div>
          <h1 className="text-3xl font-bold">ðŸ“‹ Jobs History</h1>
          <p className="text-zinc-400 mt-2">Track your generation tasks and background processing.</p>
        </div>
        <div className="flex flex-wrap gap-3">
          <select 
            value={typeFilter} onChange={e => { setTypeFilter(e.target.value); setPage(1); }}
            className="bg-zinc-900 border border-zinc-800 text-sm rounded-lg px-3 py-2 focus:outline-none"
          >
            <option value="all">All Types</option>
            <option value="image">Image</option>
            <option value="video">Video</option>
            <option value="edit-video">Edit Video</option>
          </select>
          <select 
            value={statusFilter} onChange={e => { setStatusFilter(e.target.value); setPage(1); }}
            className="bg-zinc-900 border border-zinc-800 text-sm rounded-lg px-3 py-2 focus:outline-none"
          >
            <option value="all">All Statuses</option>
            <option value="pending">Pending</option>
            <option value="processing">Processing</option>
            <option value="succeeded">Succeeded</option>
            <option value="failed">Failed</option>
          </select>
          <button onClick={loadJobs} className="p-2 bg-zinc-800 hover:bg-zinc-700 rounded-lg text-zinc-300" title="Refresh">
            <RefreshCw size={18} />
          </button>
        </div>
      </header>

      {loading ? (
        <div className="flex justify-center py-20"><RefreshCw className="animate-spin text-zinc-500" size={32} /></div>
      ) : (
        <div className="bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden flex flex-col">
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-zinc-950/50 border-b border-zinc-800 text-xs uppercase tracking-wider text-zinc-500">
                  <th className="p-4 font-semibold w-12"></th>
                  <th className="p-4 font-semibold">Status</th>
                  <th className="p-4 font-semibold">Type</th>
                  <th className="p-4 font-semibold">Model</th>
                  <th className="p-4 font-semibold w-1/3">Prompt</th>
                  <th className="p-4 font-semibold">Created</th>
                  <th className="p-4 font-semibold text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-zinc-800 text-sm">
                {jobs.length === 0 ? (
                  <tr><td colSpan={7} className="p-8 text-center text-zinc-500">No jobs found matching criteria.</td></tr>
                ) : (
                  jobs.map(job => (
                    <React.Fragment key={job.id}>
                      <tr 
                        className={`hover:bg-zinc-800/50 cursor-pointer transition-colors ${expandedJobId === job.id ? 'bg-zinc-800/30' : ''}`}
                        onClick={() => setExpandedJobId(expandedJobId === job.id ? null : job.id)}
                      >
                        <td className="p-4 text-zinc-500">
                          {expandedJobId === job.id ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                        </td>
                        <td className="p-4">
                          <span className={`px-2.5 py-1 text-[11px] font-medium rounded-full border flex items-center gap-1.5 w-max ${statusColors[job.status]}`}>
                            {job.status === 'processing' && <span className="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse"></span>}
                            {job.status.toUpperCase()}
                          </span>
                        </td>
                        <td className="p-4 capitalize text-zinc-300">{job.type.replace('-', ' ')}</td>
                        <td className="p-4">
                          <span className="px-2 py-1 bg-zinc-800 rounded text-xs text-zinc-300">{job.model}</span>
                        </td>
                        <td className="p-4">
                          <p className="truncate max-w-xs text-zinc-400" title={job.prompt}>{job.prompt}</p>
                        </td>
                        <td className="p-4 text-zinc-400 whitespace-nowrap">
                          {formatDistanceToNow(new Date(job.created_at))} ago
                        </td>
                        <td className="p-4 text-right">
                          <button onClick={(e) => handleDelete(job.id, e)} className="p-1.5 text-zinc-500 hover:text-red-400 rounded-md hover:bg-zinc-800 transition-colors" title="Delete record">
                            <Trash2 size={16} />
                          </button>
                        </td>
                      </tr>
                      {expandedJobId === job.id && (
                        <tr className="bg-zinc-950/30">
                          <td colSpan={7} className="p-6 border-b border-zinc-800">
                            <div className="max-w-3xl">
                              <JobStatusCard job={job} />
                              <div className="mt-4 grid grid-cols-2 gap-4 text-xs">
                                <div>
                                  <h4 className="font-semibold text-zinc-500 mb-2 uppercase tracking-wider">Parameters</h4>
                                  <pre className="bg-zinc-900 border border-zinc-800 p-3 rounded-lg overflow-x-auto text-zinc-300 font-mono">
                                    {JSON.stringify(job.params, null, 2)}
                                  </pre>
                                </div>
                                <div>
                                  <h4 className="font-semibold text-zinc-500 mb-2 uppercase tracking-wider">Details</h4>
                                  <div className="bg-zinc-900 border border-zinc-800 p-3 rounded-lg flex flex-col gap-2 text-zinc-300">
                                    <div className="flex justify-between border-b border-zinc-800/50 pb-1"><span>Job ID:</span><span className="font-mono text-[10px]">{job.id}</span></div>
                                    <div className="flex justify-between border-b border-zinc-800/50 pb-1"><span>Duration:</span><span>{job.elapsed_seconds ? `${job.elapsed_seconds.toFixed(1)}s` : '-'}</span></div>
                                    <div className="flex justify-between border-b border-zinc-800/50 pb-1"><span>Created:</span><span>{new Date(job.created_at).toLocaleString()}</span></div>
                                    <div className="flex justify-between pb-1"><span>Updated:</span><span>{new Date(job.updated_at).toLocaleString()}</span></div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </td>
                        </tr>
                      )}
                    </React.Fragment>
                  ))
                )}
              </tbody>
            </table>
          </div>
          <div className="p-4 border-t border-zinc-800 flex justify-between items-center bg-zinc-900">
            <span className="text-sm text-zinc-400">Page {page}</span>
            <div className="flex gap-2">
              <button 
                onClick={() => setPage(p => Math.max(1, p - 1))} 
                disabled={page === 1}
                className="px-3 py-1 bg-zinc-800 hover:bg-zinc-700 disabled:opacity-50 disabled:hover:bg-zinc-800 rounded text-sm transition-colors"
              >
                Previous
              </button>
              <button 
                onClick={() => setPage(p => p + 1)}
                disabled={jobs.length < limit}
                className="px-3 py-1 bg-zinc-800 hover:bg-zinc-700 disabled:opacity-50 disabled:hover:bg-zinc-800 rounded text-sm transition-colors"
              >
                Next
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
