import { NavLink, Outlet } from 'react-router-dom';
import { Image, Video, Scissors, FolderOpen, ClipboardList } from 'lucide-react';

export default function Layout() {
  const navItems = [
    { to: '/image', icon: <Image size={20} />, label: 'Image Generation' },
    { to: '/video', icon: <Video size={20} />, label: 'Video Generation' },
    { to: '/edit', icon: <Scissors size={20} />, label: 'Video Editing' },
    { to: '/gallery', icon: <FolderOpen size={20} />, label: 'Gallery' },
    { to: '/jobs', icon: <ClipboardList size={20} />, label: 'Jobs' },
  ];

  return (
    <div className="flex h-screen bg-zinc-950 text-zinc-100 overflow-hidden font-sans">
      <aside className="w-64 bg-zinc-900 border-r border-zinc-800 flex flex-col">
        <div className="p-6">
          <h1 className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-indigo-600 bg-clip-text text-transparent">
            BreakStudio
          </h1>
        </div>
        <nav className="flex-1 px-4 space-y-2">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-indigo-600 text-white'
                    : 'text-zinc-400 hover:bg-zinc-800 hover:text-zinc-100'
                }`
              }
            >
              {item.icon}
              <span className="font-medium">{item.label}</span>
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="flex-1 overflow-auto p-8 relative">
        <Outlet />
      </main>
    </div>
  );
}
