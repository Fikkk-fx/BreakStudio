import { ChangeEvent } from 'react';

interface PromptEditorProps {
  value: string;
  onChange: (val: string) => void;
  placeholder?: string;
  maxLength?: number;
}

export default function PromptEditor({ value, onChange, placeholder = 'Enter prompt...', maxLength }: PromptEditorProps) {
  const handleChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    if (maxLength && e.target.value.length > maxLength) return;
    onChange(e.target.value);
  };

  return (
    <div className="relative flex flex-col">
      <textarea
        className="w-full min-h-[150px] p-4 bg-zinc-800 text-zinc-100 border border-zinc-700 rounded-lg focus:outline-none focus:border-indigo-500 font-mono resize-y"
        value={value}
        onChange={handleChange}
        placeholder={placeholder}
      />
      {maxLength && (
        <span className="absolute bottom-2 right-4 text-xs text-zinc-500">
          {value.length} / {maxLength}
        </span>
      )}
    </div>
  );
}
