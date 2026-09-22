# 📱 Director O.S. V20.5 — Raw UGC & Social Mobile Studio Edition (Pruna AI Integrated)

Standalone Directorial AI Agent Skill specialized for **Hyper-Realistic Biological Raw UGC, TikTok/Reels/Shorts, Street Interviews, Bystander Viral Formats, Social Commerce, and Smartphone CMOS Physics**, natively powered by **Pruna AI** Image & Video Engines.

---

## ⚡ Pruna AI Direct Integration

Sistem ini terintegrasi penuh dengan **Pruna AI REST API** (`https://api.pruna.ai/v1`) untuk eksekusi langsung aset pra-produksi dan rendering video mobile native 9:16:

### 🌟 Model yang Didukung:
1. **`p-image-ideogram`** (Turn 4a): Generasi aset gambar dengan rendering teks & tipografi tajam, level *thinking* terkalibrasi, aspek rasio 9:16 & 1:1, resolusi 1K/2K.
2. **`flux-dev`** (Turn 4a): Generasi gambar fotorealistik berbasis Flux.1-dev dengan mode *speed optimization* (`Juiced 🔥`, `Extra Juiced 🔥`).
3. **`flux-dev-lora`** (Turn 4a): Generasi gambar dengan integrasi kustom HuggingFace LoRA untuk konsistensi karakter / *brand style lock*.
4. **`p-video-2-pro`** (Turn 6): Flagship AI video generation dengan first/last-frame conditioning, audio tersinkronisasi bawaan, resolusi 480p/768p (24fps), dan mode `speed`/`quality`/`cost`.
5. **`p-video-2`** (Turn 6): Generasi video fleksibel berdurasi 1–20 detik, resolusi 720p/1080p (24/48fps), dan input pengkondisian audio eksternal.
6. **`p-video-edit`** (Turn 6): Video-to-video editing hingga 15 detik dipandu prompt teks dan s/d 4 gambar referensi.

---

## 📁 Struktur Repository

- **`pruna_client.py`**: Client & CLI Python berstandar *production* (zero external dependencies) untuk upload file otomatis, pembuatan prediksi, polling status asinkron, dan download output.
- **`.env` / `.env.example`**: Konfigurasi kunci API (`PRUNA_AI_API_KEY`).
- **`SKILL.md`**: Master entrypoint skill dengan spesifikasi lengkap:
  - **The 18 Ironclad Production Mandates V20.5 (UGC Edition)** (Jendela timestamp dialog & 0.8s tail-buffer, dynamic reframes, kuota kerumunan eksak, skoring diegetik -4dB ducking, batas kata WPS, 10 pilar komposisi mobile 9:16, dsb.)
  - **6-Step Interactive Production Flow (Turn 1–6)** & Header Navigasi Anti-Lupa
  - **UGC Mobile Directorial Engines & Smartphone Optics Codex** (iPhone 16 Pro Max ProRes Log, Galaxy S24 Ultra, Pixel 9 Pro; panjang fokal 13mm–120mm; micro-shake 8–12Hz; greasy lens halation; auto-exposure/autofocus breathing)
  - **Biological Raw UGC Studio** (The Anti-Influencer Golden Rule, The 7 Pillars of Raw UGC, 4-Cut Bystander Progression, 80/20 Selfie Screen-Look Drift, Somatic Fidgeting, Unscripted Speech Repairs)
  - **Universal 6-Layer Locked Prompt Architecture (SSOT - Module 24)**
  - **Master UGC Color Palette & Grading Library (`PAL-UGC`, `PAL-COM`, `PAL-STR`)**
  - **Master Natural Lighting Composition Codex (Module 26)** (6-Phase Solar Cycle, Ambient Light Physics, Portrait Patterns)
  - **Master Visual Techniques & Optical Effects Codex (Module 27)** (46 Master Techniques: Fast Motion, Collage, Duplication, Zoetrope, Motion Blur, Speed Ramp, Fixed Cam, Timelapse, Step-Printing, Flash Cut, Wipe Transition, Quick Cut, Strobe, Stutter, Point Cloud, Glitch, Seamless Transition, Cut-ins, Fourth Wall, Color Shift, Bullet Time, Super Zoom, Match Motion, Zoom In/Low Frame Rate, Jump Cut, etc. — Strictly 0% SFX)
  - **Master Directorial Pruna AI Codex (Module 28)** (`rules/28_pruna_ai_model_and_dispatch_codex.md`)
  - **4-Panel Raw Character Sheet Generator (Asset Lock)** & Master Negative Prompt Hardware Lock
  - **Inline Generation Protocols** (Turn 4a Image via Pruna `p-image-ideogram`/`flux-dev`, Turn 6 Video via Pruna `p-video-2-pro`/`p-video-2`)
- **`prompt_auditor.py`**: Skrip standalone Python untuk audit pra-generasi, kalkulator densitas karakter/kata, dan verifikasi zero-defect prompt UGC.
- **`rules/`**: Kumpulan 47 modul dan codex teknis lengkap (file Markdown) yang mencakup seluruh pipeline pra-produksi hingga eksekusi prompt AI video.

---

## 🚀 Cara Penggunaan & CLI Dispatch

### 1. Konfigurasi Kunci API:
Pastikan file `.env` berisi:
```env
PRUNA_AI_API_KEY=pru_IwuwIn1Gce5Axm70zp4wfGbx8sssd2Vs
```

### 2. Generasi Gambar (Turn 4a):
```bash
# Menggunakan p-image-ideogram (Typographic & CharSheet):
python pruna_client.py image \
  --model p-image-ideogram \
  --prompt "4-Panel Raw Character Sheet of Indonesian barista, white background" \
  --aspect-ratio 9:16 \
  --output assets/charsheet.jpg

# Menggunakan flux-dev (Photorealistic):
python pruna_client.py image \
  --model flux-dev \
  --prompt "Hyper-realistic Jakarta night street food stall, smartphone CMOS 24mm f/1.7" \
  --aspect-ratio 9:16 \
  --output assets/street_stall.jpg
```

### 3. Generasi Video (Turn 6):
```bash
# Menggunakan p-video-2-pro (Flagship Video + Audio Bawaan):
python pruna_client.py video \
  --model p-video-2-pro \
  --prompt "Handheld smartphone footage of a street vendor laughing and pouring iced tea. Natural 9Hz micro-shake." \
  --image assets/charsheet.jpg \
  --duration 5 \
  --resolution 768p \
  --aspect-ratio 9:16 \
  --output outputs/clip_01.mp4

# Menggunakan p-video-2 (Kondisi Audio Eksternal):
python pruna_client.py video \
  --model p-video-2 \
  --prompt "Young woman talking excitedly to the camera in bedroom" \
  --audio voiceovers/narration.mp3 \
  --resolution 1080p \
  --aspect-ratio 9:16 \
  --output outputs/clip_02.mp4
```

### 4. Video Editing:
```bash
python pruna_client.py edit-video \
  --video outputs/raw.mp4 \
  --prompt "Change background into a bustling modern cafe" \
  --output outputs/edited.mp4
```

### 5. Audit Prompt Otomatis:
```bash
python prompt_auditor.py <prompt_file.txt | "prompt string"> [--duration 15] [--mode 2|3] [--json]
```