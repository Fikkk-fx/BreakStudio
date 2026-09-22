import { useState, useEffect } from 'react';
import { getGallery, deleteGalleryItem, downloadGalleryItem } from '../api/client';
import { GalleryItem } from '../types';
import { formatDistanceToNow } from 'date-fns';
import { Download, Trash2, Eye, Copy, RefreshCw } from 'lucide-react';

export default function GalleryPage() {
  const [items, setItems] = useState<GalleryItem[]>([]);
  const [filter, setFilter] = useState<'all' | 'image' | 'video'>('all');
  const [loading, setLoading] = useState(true);
  const [previewItem, setPreviewItem] = useState<GalleryItem | null>(null);
  
  // Pagination
  const [offset, setOffset] = useState(0);
  const [hasMore, setHasMore] = useState(true);
  const limit = 12;

  const loadGallery = async (reset = false) => {
    try {
      if (reset) {
        setLoading(true);
        setOffset(0);
      }
      const currentOffset = reset ? 0 : offset;
      const response = await getGallery({ 
        type: filter === 'all' ? undefined : filter,
        limit,
        offset: currentOffset
      });
      
      if (reset) {
        setItems(response.data);
      } else {
        setItems(prev => [...prev, ...response.data]);
      }
      
      setHasMore(response.data.length === limit);
      if (!reset) setOffset(currentOffset + limit);
      else setOffset(limit);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadGallery(true);
  }, [filter]);

  const handleDelete = async (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!confirm('Are you sure you want to delete this item?')) return;
    try {
      await deleteGalleryItem(id);
      setItems(items.filter(item => item.id !== id));
      if (previewItem?.id === id) setPreviewItem(null);
    } catch (error) {
      console.error(error);
    }
  };

  const handleDownload = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    downloadGalleryItem(id);
  };

  const handleCopyPrompt = (prompt: string, e: React.MouseEvent) => {
    e.stopPropagation();
    navigator.clipboard.writeText(prompt);
  };

  return (
    <div className="max-w-6xl mx-auto flex flex-col gap-6 pb-10">
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold">📁 Gallery</h1>
          <p className="text-zinc-400 mt-2">Browse and manage your generated creations.</p>
        </div>
        <div className="flex bg-zinc-900 rounded-lg p-1 border border-zinc-800">
          {(['all', 'image', 'video'] as const).map(t => (
            <button
              key={t}
              onClick={() => setFilter(t)}
              className={`px-4 py-2 rounded-md text-sm font-medium capitalize transition-colors ${
                filter === t ? 'bg-indigo-600 text-white' : 'text-zinc-400 hover:text-white hover:bg-zinc-800'
              }`}
            >
              {t}
            </button>
          ))}
        </div>
      </header>

      {loading && items.length === 0 ? (
        <div className="flex justify-center py-20"><RefreshCw className="animate-spin text-zinc-500" size={32} /></div>
      ) : items.length === 0 ? (
        <div className="text-center py-32 bg-zinc-900/50 rounded-xl border border-zinc-800 border-dashed">
          <p className="text-zinc-400 text-lg">No items found.</p>
          <p className="text-zinc-500 text-sm mt-2">Generate some content to see it here.</p>
        </div>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {items.map(item => (
              <div 
                key={item.id} 
                className="group relative bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden cursor-pointer hover:border-indigo-500/50 transition-all flex flex-col"
                onClick={() => setPreviewItem(item)}
              >
                <div className="aspect-video bg-zinc-950 flex items-center justify-center relative overflow-hidden">
                  {item.type === 'video' ? (
                    <video src={item.url} poster={item.thumbnail_url} className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
                  ) : (
                    <img src={item.url} className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" loading="lazy" />
                  )}
                  <div className="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 flex items-center justify-center gap-3 transition-opacity">
                    <button onClick={(e) => { e.stopPropagation(); setPreviewItem(item); }} className="p-2 bg-zinc-800 hover:bg-zinc-700 rounded-full text-white" title="View Full"><Eye size={18} /></button>
                    <button onClick={(e) => handleDownload(item.id, e)} className="p-2 bg-indigo-600 hover:bg-indigo-700 rounded-full text-white" title="Download"><Download size={18} /></button>
                    <button onClick={(e) => handleDelete(item.id, e)} className="p-2 bg-red-600 hover:bg-red-700 rounded-full text-white" title="Delete"><Trash2 size={18} /></button>
                  </div>
                </div>
                <div className="p-4 flex flex-col gap-2">
                  <div className="flex justify-between items-center">
                    <span className="px-2 py-0.5 bg-zinc-800 text-zinc-300 text-[10px] font-semibold rounded uppercase tracking-wider">{item.model}</span>
                    <span className="text-xs text-zinc-500">{formatDistanceToNow(new Date(item.created_at))} ago</span>
                  </div>
                  <p className="text-sm text-zinc-300 line-clamp-2" title={item.prompt}>{item.prompt}</p>
                </div>
              </div>
            ))}
          </div>
          {hasMore && (
            <div className="flex justify-center mt-8">
              <button onClick={() => loadGallery()} className="px-6 py-2 bg-zinc-800 hover:bg-zinc-700 rounded-lg text-sm font-medium transition-colors">
                {loading ? 'Loading...' : 'Load More'}
              </button>
            </div>
          )}
        </>
      )}

      {/* Preview Modal */}
      {previewItem && (
        <div className="fixed inset-0 z-50 bg-black/90 flex flex-col p-4 md:p-10 backdrop-blur-sm" onClick={() => setPreviewItem(null)}>
          <div className="flex justify-end mb-4 gap-4">
            <button onClick={(e) => handleDownload(previewItem.id, e)} className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 rounded-lg text-white font-medium"><Download size={16}/> Download</button>
            <button onClick={() => setPreviewItem(null)} className="px-4 py-2 bg-zinc-800 hover:bg-zinc-700 rounded-lg text-white font-medium">Close</button>
          </div>
          <div className="flex-1 flex flex-col md:flex-row gap-8 overflow-hidden">
            <div className="flex-1 flex items-center justify-center bg-zinc-950 border border-zinc-800 rounded-xl overflow-hidden" onClick={e => e.stopPropagation()}>
              {previewItem.type === 'video' ? (
                <video src={previewItem.url} controls autoPlay className="max-w-full max-h-full object-contain" />
              ) : (
                <img src={previewItem.url} className="max-w-full max-h-full object-contain" />
              )}
            </div>
            <div className="w-full md:w-80 bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex flex-col gap-4 overflow-y-auto" onClick={e => e.stopPropagation()}>
              <h3 className="font-bold text-lg border-b border-zinc-800 pb-2">Details</h3>
              <div><span className="text-xs text-zinc-500 uppercase tracking-wider">Model</span><p className="text-sm font-medium mt-1">{previewItem.model}</p></div>
              <div><span className="text-xs text-zinc-500 uppercase tracking-wider">Type</span><p className="text-sm font-medium mt-1 capitalize">{previewItem.type}</p></div>
              <div><span className="text-xs text-zinc-500 uppercase tracking-wider">Created</span><p className="text-sm font-medium mt-1">{new Date(previewItem.created_at).toLocaleString()}</p></div>
              <div>
                <div className="flex justify-between items-center"><span className="text-xs text-zinc-500 uppercase tracking-wider">Prompt</span><button onClick={(e) => handleCopyPrompt(previewItem.prompt, e)} className="text-indigo-400 hover:text-indigo-300 p-1"><Copy size={14}/></button></div>
                <div className="text-sm bg-zinc-950 p-3 rounded-lg border border-zinc-800 mt-1 max-h-40 overflow-y-auto text-zinc-300 leading-relaxed">{previewItem.prompt}</div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
