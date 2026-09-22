import { useState, useRef, ChangeEvent, DragEvent } from 'react';
import { UploadCloud, X } from 'lucide-react';

interface FileUploaderProps {
  accept?: string;
  onFileSelected: (file: File | null) => void;
  label?: string;
  preview?: boolean;
}

export default function FileUploader({ accept = '*/*', onFileSelected, label = 'Upload File', preview = true }: FileUploaderProps) {
  const [file, setFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleFile = (newFile: File | null) => {
    setFile(newFile);
    onFileSelected(newFile);
    
    if (newFile && preview) {
      const url = URL.createObjectURL(newFile);
      setPreviewUrl(url);
    } else {
      if (previewUrl) URL.revokeObjectURL(previewUrl);
      setPreviewUrl(null);
    }
  };

  const onChange = (e: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0] || null;
    handleFile(selectedFile);
  };

  const onDragOver = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const onDragLeave = () => {
    setIsDragging(false);
  };

  const onDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const clearFile = (e: React.MouseEvent) => {
    e.stopPropagation();
    handleFile(null);
    if (inputRef.current) inputRef.current.value = '';
  };

  return (
    <div className="flex flex-col gap-2">
      {label && <span className="text-sm font-medium text-zinc-300">{label}</span>}
      <div
        className={`relative border-2 border-dashed rounded-lg p-6 flex flex-col items-center justify-center text-center cursor-pointer transition-colors ${
          isDragging ? 'border-indigo-500 bg-indigo-500/10' : 'border-zinc-700 bg-zinc-800 hover:bg-zinc-750'
        }`}
        onClick={() => inputRef.current?.click()}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
      >
        <input type="file" className="hidden" ref={inputRef} accept={accept} onChange={onChange} />
        
        {file ? (
          <div className="w-full flex flex-col items-center">
            {preview && previewUrl && (
              <div className="relative w-full max-h-48 overflow-hidden rounded mb-4 flex justify-center bg-zinc-900">
                {file.type.startsWith('video/') ? (
                  <video src={previewUrl} className="max-h-48 object-contain" controls />
                ) : (
                  <img src={previewUrl} alt="Preview" className="max-h-48 object-contain" />
                )}
              </div>
            )}
            <div className="flex items-center justify-between w-full p-2 bg-zinc-900 rounded border border-zinc-700">
              <span className="text-sm truncate max-w-[80%]">{file.name}</span>
              <button onClick={clearFile} className="p-1 hover:bg-zinc-700 rounded text-zinc-400 hover:text-white">
                <X size={16} />
              </button>
            </div>
          </div>
        ) : (
          <div className="flex flex-col items-center gap-2 py-4 text-zinc-400">
            <UploadCloud size={32} />
            <p className="text-sm">Click to browse or drag & drop</p>
          </div>
        )}
      </div>
    </div>
  );
}
