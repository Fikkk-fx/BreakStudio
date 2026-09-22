# 📱 BreakStudio — Raw UGC & Social Mobile Studio

Full-stack AI-powered video production studio for **Hyper-Realistic Raw UGC, TikTok/Reels/Shorts, Street Interviews, and Social Commerce**, integrated with **[Pruna AI](https://pruna.ai)** image & video generation engines.

---

## 🗂️ Struktur Project

```
BreakStudio/
├── backend/                    # FastAPI server
│   ├── routes/                 # API endpoints (generate, jobs, gallery, ws)
│   ├── prompts/                # Prompt templates
│   ├── rules/                  # Production codex & rules (48 modules)
│   ├── outputs/                # Generated media output
│   ├── uploads/                # Uploaded assets
│   ├── pruna_client.py         # Pruna AI REST client (zero dependencies)
│   ├── prompt_auditor.py       # Pre-generation prompt linter & auditor
│   ├── skill_rules_reader.py   # Rules parser & extractor
│   ├── test_suite.py           # Integration test suite
│   ├── main.py                 # FastAPI app entrypoint
│   ├── config.py               # App configuration
│   ├── database.py             # SQLite database setup
│   ├── pruna_service.py        # Pruna AI service layer
│   ├── schemas.py              # Pydantic request/response schemas
│   └── requirements.txt        # Python dependencies
├── frontend/                   # React + Vite + TypeScript
│   ├── src/
│   │   ├── api/                # API client
│   │   ├── components/         # UI components
│   │   ├── pages/              # Page views
│   │   ├── stores/             # Zustand state
│   │   └── types/              # TypeScript types
│   ├── public/assets/          # Static assets
│   ├── index.html
│   ├── package.json
│   └── vite.config.ts
├── .env.example                # Template environment variables
├── .gitignore
├── vercel.json                 # Vercel deployment config
├── run_backend.bat             # Start backend (Windows)
├── run_frontend.bat            # Start frontend (Windows)
└── start_studio.bat            # Start both (Windows)
```

---

## ⚙️ Setup & Instalasi

### Prerequisites
- Python 3.10+
- Node.js 18+
- [Pruna AI API Key](https://pruna.ai)

### 1. Clone Repository
```bash
git clone https://github.com/Fikkk-fx/BreakStudio.git
cd BreakStudio
```

### 2. Konfigurasi Environment
```bash
cp .env.example .env
```
Buka `.env` dan isi nilai berikut:
```env
PRUNA_AI_API_KEY=your_pruna_api_key_here
```
> ⚠️ **Jangan pernah commit file `.env`!** File ini sudah masuk `.gitignore`.

### 3. Install Backend
```bash
cd backend
pip install -r requirements.txt
```

### 4. Install Frontend
```bash
cd frontend
npm install
```

---

## 🚀 Menjalankan Aplikasi

### Cara Cepat (Windows)
Double-click **`start_studio.bat`** — akan membuka backend & frontend sekaligus.

### Manual
```bash
# Terminal 1 — Backend (dari root project)
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

# Terminal 2 — Frontend
cd frontend
npm run dev
```

Buka browser: **http://localhost:5173**
- API Docs: **http://localhost:8000/docs**

---

## 🤖 Pruna AI Models

| Model | Kegunaan | Output |
|---|---|---|
| `p-image-ideogram` | Gambar dengan tipografi tajam | JPG/PNG |
| `flux-dev` | Gambar fotorealistik | JPG/PNG |
| `flux-dev-lora` | Gambar dengan LoRA kustom | JPG/PNG |
| `p-video-2-pro` | Video flagship + audio bawaan | MP4 |
| `p-video-2` | Video fleksibel 1–20 detik | MP4 |
| `p-video-edit` | Video-to-video editing | MP4 |

---

## 🛠️ CLI Usage (Backend Tools)

### Generasi Gambar
```bash
# p-image-ideogram
python -m backend.pruna_client image \
  --model p-image-ideogram \
  --prompt "4-Panel Raw Character Sheet, Indonesian barista, white background" \
  --aspect-ratio 9:16 \
  --output backend/outputs/charsheet.jpg

# flux-dev
python -m backend.pruna_client image \
  --model flux-dev \
  --prompt "Hyper-realistic Jakarta street food stall, smartphone 24mm f/1.7" \
  --aspect-ratio 9:16 \
  --output backend/outputs/street.jpg
```

### Generasi Video
```bash
# p-video-2-pro
python -m backend.pruna_client video \
  --model p-video-2-pro \
  --prompt "Handheld smartphone footage of street vendor, 9Hz micro-shake" \
  --image backend/outputs/charsheet.jpg \
  --duration 5 \
  --resolution 768p \
  --output backend/outputs/clip_01.mp4
```

### Audit Prompt
```bash
python -m backend.prompt_auditor "your prompt here" --duration 15 --mode 2
```

---

## 🌐 Deploy (Vercel)

Frontend di-deploy otomatis ke Vercel dari folder `frontend/`.

Set environment variable di Vercel dashboard:
- (Tidak ada env khusus untuk frontend — API key hanya digunakan di backend)

---

## 📄 License

Private project. All rights reserved.