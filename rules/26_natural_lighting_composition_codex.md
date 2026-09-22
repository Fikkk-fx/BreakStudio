---
name: 26-natural-lighting-composition-codex
description: "Master Natural Lighting Composition & Ambient Light Physics Codex V20.5: Comprehensive SSOT for Natural Light Direction (Front/Side/Back/Top/Rim), Quality (Hard/Soft/Diffused), 6-Phase Solar Cycle (Blue Hour → Golden Hour → Overcast → Harsh Midday → Afternoon → Dusk), Color Temperature Kelvin Scale (2000K–10000K), 4 Portrait Lighting Patterns (Butterfly/Loop/Rembrandt/Split), Lighting Ratios (1:1 → 8:1), Indoor Window Light Strategies, Motivated & Practical Light Integration, Chiaroscuro & High-Key/Low-Key Modes, and Universal LIT_ID Prompt Binding for Module 24."
---

# ☀️ MODUL 26: NATURAL LIGHTING COMPOSITION & AMBIENT LIGHT PHYSICS CODEX — SSOT V20.5
========================================================================================================
MASTER NATURAL LIGHT DIRECTION, QUALITY, COLOR TEMPERATURE, PORTRAIT PATTERNS & UNIVERSAL LIT_ID PROMPT BINDING
========================================================================================================

Welcome to **Module 26 (Natural Lighting Composition & Ambient Light Physics Codex)**.
This module serves as the authoritative **Single Source of Truth (SSOT)** for all natural lighting composition, ambient light physics, solar cycle timing, portrait lighting patterns, and lighting ratio engineering across Director O.S. V20.5. It directly enforces **Mandat 14 (Pilar 2: Lighting & Ambient Physics)** and integrates into **Modul 24 (Universal Locked Prompt Architecture — Layer 1 `LIGHTING RIG`)**.

> [!IMPORTANT]
> ### 🛑 PRINSIP DASAR LIGHTING NATURAL UGC:
> Seluruh pencahayaan dalam konten Raw UGC **WAJIB** terlihat 100% alami dan tidak berkesan studio.
> **DILARANG KERAS:** Ring light yang terlihat di catchlight mata, softbox refleksi, studio strobe, beauty dish glow, atau sumber cahaya artifisial apa pun yang mengkhianati estetika "direkam spontan dengan HP".
> Satu-satunya sumber cahaya yang diizinkan: **matahari, langit mendung, cahaya jendela, lampu ruangan praktis (lampu meja, neon, TV), cahaya layar HP, dan sumber ambient alami lainnya.**

---

## 🌅 SECTION I: THE 6-PHASE SOLAR CYCLE ENGINE (SSOT)

Setiap fase matahari menghasilkan karakter cahaya yang berbeda secara fundamental. Pemilihan fase WAJIB dideklarasikan secara eksplisit di prompt.

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 6-PHASE SOLAR CYCLE & LIGHT CHARACTER ENGINE                            │
├──────────┬──────────────┬──────────────┬───────────────────────────────────────────────────────────────────┤
│ FASE     │ WAKTU        │ KELVIN       │ KARAKTER CAHAYA & MOOD                                          │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 1. BLUE  │ 04:30–05:45  │ 9000K–12000K │ Biru keunguan lembut, tanpa bayangan keras, ethereal,           │
│    HOUR  │ (pagi) atau  │              │ introspektif, melankolis. Langit = sumber cahaya omnidirectional │
│  (DAWN)  │ 18:30–19:45  │              │ yang sangat merata. Ideal: konten emosional, curhat,            │
│          │ (senja)      │              │ refleksi personal.                                              │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 2.GOLDEN │ 05:45–07:00  │ 2500K–3500K  │ Emas hangat, bayangan panjang & lembut, cahaya directional      │
│   HOUR   │ (pagi) atau  │              │ rendah yang menyapu horizontal. Skin tone = sangat flattering.  │
│ (SUNRISE │ 17:00–18:30  │              │ Highlight roll-off halus. Rim light alami pada rambut & bahu.   │
│ /SUNSET) │ (sore)       │              │ Ideal: lifestyle, beauty, storytelling emosional.               │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 3. OVER- │ Sepanjang    │ 6000K–7500K  │ Langit mendung = softbox raksasa alami. Cahaya merata dari      │
│   CAST   │ hari (cuaca  │              │ segala arah, bayangan sangat lembut hampir hilang. Warna        │
│  (CLOUDY)│ mendung)     │              │ sedikit desaturated & cool-toned. Ideal: product review,        │
│          │              │              │ tutorial, konten informatif, GRWM.                              │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 4. HARSH │ 10:00–14:00  │ 5200K–5800K  │ Matahari tepat di atas, bayangan pendek & sangat keras di bawah │
│  MIDDAY  │ (tengah      │              │ hidung/dagu/alis. Kontras ekstrem, highlight blow-out rentan.    │
│          │ hari)        │              │ WAJIB cari shade/teduhan atau gunakan diffuser alami.            │
│          │              │              │ Ideal: street interview (di bawah teduhan), energi tinggi.      │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 5. AFTER │ 14:00–17:00  │ 4500K–5500K  │ Cahaya mulai melembut & menghangat, bayangan mulai memanjang.   │
│   NOON   │ (siang-sore) │              │ Transisi dari neutral ke warm. Kontras sedang. Versatile        │
│          │              │              │ untuk hampir semua format UGC. Ideal: outdoor casual,           │
│          │              │              │ jalan-jalan, behind-the-scenes.                                 │
├──────────┼──────────────┼──────────────┼───────────────────────────────────────────────────────────────────┤
│ 6. DUSK  │ 19:45–20:30  │ 3000K–4000K  │ Langit gelap keunguan, sisa cahaya ambient sangat lemah.        │
│ /TWILIGHT│              │ + warm       │ Practical lights (lampu jalan, neon toko, layar HP) mulai       │
│          │              │ practicals   │ mendominasi. Mixed color temperature alami. Ideal: night         │
│          │              │              │ vlog, street content malam, atmosphere moody.                   │
└──────────┴──────────────┴──────────────┴───────────────────────────────────────────────────────────────────┘
```

### Aturan Penerapan Solar Cycle:
1. **WAJIB pilih 1 fase spesifik** — jangan pernah menulis "siang hari" tanpa spesifikasi fase.
2. **Bayangan harus konsisten** dengan posisi matahari pada fase yang dipilih (rendah = bayangan panjang, tinggi = bayangan pendek).
3. **Color temperature prompt** harus selaras dengan Kelvin range pada fase tersebut.
4. **Transisi antar fase** (misalnya Golden Hour menuju Dusk) boleh digunakan untuk multi-clip continuity, dengan gradasi warna yang progresif.

---

## 🔦 SECTION II: THE 5-DIRECTION NATURAL LIGHT ENGINE

Arah datangnya cahaya terhadap subjek adalah faktor paling kritis dalam membentuk dimensi, mood, dan kedalaman visual.

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 5-DIRECTION NATURAL LIGHT PLACEMENT ENGINE                             │
├───────────────┬──────────────────────────────────────────────────────────────────────────────────────────┤
│ DIRECTION     │ EFEK VISUAL & PANDUAN PENGGUNAAN                                                        │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. FRONT      │ Cahaya datang dari depan subjek (sejajar kamera). Wajah teriluminasi merata,            │
│    LIGHT      │ bayangan minimal, tekstur & kerut tersembunyi. Terkesan "flat" & 2D.                    │
│               │ ✅ Gunakan: beauty/skincare review, product close-up, konten informatif.                │
│               │ ⚠️ Hindari: konten dramatis atau cinematic — kurang dimensi.                            │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. SIDE       │ Cahaya datang dari samping (45°–90° dari kamera). Menciptakan bayangan yang             │
│    LIGHT      │ membentuk kontur wajah, menonjolkan tekstur kulit, pori-pori, dan dimensi 3D.          │
│    (KEY SIDE) │ ✅ Gunakan: storytime, vlog emosional, street interview, konten dramatis.               │
│               │ 🎯 Posisi 45° = sweet spot untuk UGC — cukup dimensi tanpa terlalu dramatis.           │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. BACK       │ Cahaya datang dari belakang subjek. Menciptakan rim light / edge light pada             │
│    LIGHT      │ rambut & bahu, memisahkan subjek dari background. Wajah cenderung gelap                │
│               │ (silhouette) kecuali ada fill dari reflector atau ambient bounce.                       │
│               │ ✅ Gunakan: golden hour glow, silhouette dramatis, "angelic halo" effect.               │
│               │ ⚠️ WAJIB: Jika backlit, pastikan AE smartphone lock ke wajah, bukan langit.            │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. TOP        │ Cahaya datang dari atas (matahari tengah hari / lampu plafon). Menciptakan              │
│    LIGHT      │ bayangan keras di bawah alis ("raccoon eyes"), bawah hidung, dan bawah dagu.            │
│    (OVERHEAD) │ ⚠️ UMUMNYA TIDAK FLATTERING untuk wajah manusia.                                       │
│               │ ✅ Gunakan: HANYA jika ada diffuser alami (daun pohon, kanopi, payung kafe).            │
│               │ 🎯 Jika terpaksa top light: minta subjek sedikit mendongak ke arah cahaya.             │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 5. RIM /      │ Cahaya datang dari belakang-samping (sekitar 135°–160° dari kamera).                    │
│    EDGE       │ Menciptakan garis cahaya tipis di tepi profil wajah, rambut, atau bahu —               │
│    LIGHT      │ tanpa menerangi wajah secara penuh. Efek separation dari background kuat.              │
│               │ ✅ Gunakan: konten sore/sunset, interview backlit, transisi indoor-outdoor.              │
│               │ 🎯 Kombinasikan dengan ambient fill dari depan untuk look yang balanced.                │
└───────────────┴──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎭 SECTION III: THE 4 PORTRAIT LIGHTING PATTERNS (NATURAL LIGHT ADAPTATION)

Empat pola pencahayaan klasik portraiture yang dapat dicapai secara alami tanpa studio light.

### 3.1 🦋 BUTTERFLY LIGHTING (Paramount Lighting)
- **Setup Natural:** Subjek menghadap jendela besar atau langit terbuka, cahaya datang dari atas-depan, sejajar sumbu hidung.
- **Ciri Khas:** Bayangan simetris berbentuk kupu-kupu di bawah hidung. Tulang pipi teraksentuasi.
- **Mood:** Elegan, glamor, flattering, klasik Hollywood.
- **UGC Use Case:** Beauty/skincare review (cahaya jendela besar dari depan-atas), GRWM tutorial.
- **Prompt Cue:** `Natural butterfly lighting from large window above-center, symmetrical nose shadow, cheekbone highlights`

### 3.2 ➰ LOOP LIGHTING
- **Setup Natural:** Cahaya jendela atau matahari datang dari depan-samping (sekitar 30°–45° dari sumbu kamera), sedikit lebih tinggi dari mata.
- **Ciri Khas:** Bayangan kecil berbentuk loop jatuh dari hidung ke pipi (tidak menyentuh bibir). Dimensi wajah terlihat tanpa drama berlebihan.
- **Mood:** Natural, approachable, hangat, everyday.
- **UGC Use Case:** Vlog casual, storytime, product review — **POLA PALING UMUM & VERSATILE untuk UGC.**
- **Prompt Cue:** `Natural loop lighting, soft shadow loop from nose to cheek at 30-degree angle, warm ambient fill`

### 3.3 🎨 REMBRANDT LIGHTING
- **Setup Natural:** Cahaya jendela atau matahari dari samping (~45°–60°) dan lebih tinggi, sehingga bayangan hidung menyatu dengan bayangan pipi, membentuk segitiga cahaya terbalik di pipi sisi gelap.
- **Ciri Khas:** **Segitiga cahaya (triangle of light)** di pipi sisi bayangan — trademark Rembrandt.
- **Mood:** Dramatis, moody, artistik, introspektif.
- **UGC Use Case:** Storytime emosional/serius, konten curhat mendalam, night vlog dengan satu lampu meja.
- **Prompt Cue:** `Rembrandt triangle lighting from side window, inverted light triangle on shadow cheek, high contrast mood`

### 3.4 ⚡ SPLIT LIGHTING
- **Setup Natural:** Cahaya datang tepat dari samping (90° dari kamera), membagi wajah menjadi dua: setengah terang, setengah gelap.
- **Ciri Khas:** Garis pembagi cahaya/gelap tepat di tengah wajah secara vertikal.
- **Mood:** Intens, misterius, bold, edgy, konfrontatif.
- **UGC Use Case:** Konten kontroversial, hot take, mystery/thriller storytelling, dramatic reveal.
- **Prompt Cue:** `Natural split lighting from 90-degree side window, half face in shadow, dramatic bisect`

---

## 📊 SECTION IV: LIGHTING RATIO ENGINE (CONTRAST CONTROL)

Lighting ratio mengontrol tingkat kontras antara sisi terang (key side) dan sisi gelap (fill/shadow side) pada wajah subjek.

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              LIGHTING RATIO & MOOD MAPPING ENGINE                                       │
├──────────┬────────────┬─────────────────────────────────────────────────────────────────────────────────┤
│ RATIO    │ F-STOP Δ   │ KARAKTER & UGC USE CASE                                                       │
├──────────┼────────────┼─────────────────────────────────────────────────────────────────────────────────┤
│ 1:1      │ 0 stop     │ Flat, tanpa bayangan. Overcast day atau flash frontal.                         │
│          │            │ UGC: Product flat-lay, skincare close-up, bright & airy aesthetic.              │
├──────────┼────────────┼─────────────────────────────────────────────────────────────────────────────────┤
│ 2:1      │ 1 stop     │ Kontras lembut, dimensi subtle. Cahaya jendela + ambient bounce.               │
│          │            │ UGC: Everyday vlog, GRWM, casual review. ★ SWEET SPOT RAW UGC ★               │
├──────────┼────────────┼─────────────────────────────────────────────────────────────────────────────────┤
│ 4:1      │ 2 stop     │ Bayangan pronounced, dimensi kuat. Side window tanpa reflector.               │
│          │            │ UGC: Storytime serius, interview mendalam, konten emosional.                   │
├──────────┼────────────┼─────────────────────────────────────────────────────────────────────────────────┤
│ 8:1      │ 3 stop     │ High contrast, sebagian wajah sangat gelap. Satu sumber cahaya keras.         │
│          │            │ UGC: Konten dramatis/kontroversial, night confession, horror storytelling.     │
├──────────┼────────────┼─────────────────────────────────────────────────────────────────────────────────┤
│ 16:1+    │ 4+ stop    │ Near-silhouette, extreme drama. Backlit tanpa fill sama sekali.               │
│          │            │ UGC: Silhouette artistic, anonymous testimonial, reveal shot.                  │
└──────────┴────────────┴─────────────────────────────────────────────────────────────────────────────────┘
```

### Aturan Lighting Ratio UGC:
1. **Default UGC = 2:1 hingga 3:1** — cukup dimensi untuk look natural, tidak terlalu flat, tidak terlalu dramatis.
2. **DILARANG 1:1 flat** pada konten yang menampilkan wajah manusia (kecuali flat-lay produk) — terlihat seperti ring light murah.
3. **Ratio 4:1 ke atas** memerlukan justifikasi naratif (mood gelap, konflik, misteri).
4. **Pencapaian natural:** Geser subjek mendekati/menjauhi jendela, atau gunakan dinding putih sebagai bounce alami.

---

## 🏠 SECTION V: INDOOR NATURAL LIGHT STRATEGIES

### 5.1 Window Light Mastery (Sumber Indoor #1)

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              WINDOW LIGHT POSITIONING MATRIX                                            │
├─────────────────────┬────────────────────────────────────────────────────────────────────────────────────┤
│ POSISI SUBJEK       │ EFEK & CATATAN                                                                    │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ MENGHADAP JENDELA   │ Front light merata, bayangan minimal. Flattering untuk semua skin tone.           │
│ (0° dari jendela)   │ ✅ Best for: GRWM, beauty review, tutorial makeup. Paling aman & mudah.          │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 45° DARI JENDELA    │ Loop lighting natural. Dimensi wajah muncul, bayangan lembut.                    │
│                     │ ✅ Best for: Vlog, storytime, product review. ★ POSISI PALING VERSATILE ★        │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 90° DARI JENDELA    │ Split/Rembrandt lighting. Separuh wajah terang, separuh gelap.                   │
│ (samping jendela)   │ ✅ Best for: Konten dramatis, storytime serius, artistic portrait.               │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ MEMBELAKANGI        │ Silhouette / backlit. Wajah gelap, rim light pada rambut.                        │
│ JENDELA (180°)      │ ⚠️ HANYA jika ada fill kuat dari lampu depan atau bounce board.                  │
│                     │ Tanpa fill = wajah underexposed, tidak terlihat ekspresi.                        │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ DEKAT JENDELA       │ Cahaya lebih keras & kontras tinggi (sumber relatif kecil ke subjek).            │
│ (< 1 meter)         │ ✅ Best for: Dramatic, edgy, high-contrast content.                              │
├─────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ JAUH DARI JENDELA   │ Cahaya lebih lembut & merata (inverse square law, cahaya menyebar).              │
│ (> 2 meter)         │ ✅ Best for: Even lighting, soft mood, gentle aesthetic.                          │
└─────────────────────┴────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Diffuser & Bounce Alami (Zero-Budget Tools)

| TOOL ALAMI | FUNGSI | CARA KERJA |
|:---|:---|:---|
| **Tirai tipis / vitrase putih** | Diffuser alami | Mengubah harsh direct sunlight menjadi soft wrap-around light. WAJIB untuk jendela yang terkena matahari langsung. |
| **Dinding putih** | Bounce / fill alami | Memantulkan cahaya jendela kembali ke sisi gelap wajah. Semakin dekat subjek ke dinding putih = fill semakin kuat. |
| **Sprei putih / kain putih** | Reflector darurat | Dipegang teman atau disandarkan di kursi, memantulkan cahaya ke area bayangan. |
| **Dinding gelap / kain hitam** | Negative fill | Menyerap cahaya pantul, memperdalam bayangan. Gunakan untuk menaikkan kontras secara natural. |
| **Lantai terang** | Under-fill subtle | Lantai keramik/marmer putih memantulkan cahaya ke bawah dagu, mengurangi bayangan chin. |

### 5.3 Practical Light Integration (Lampu Ruangan)

> [!WARNING]
> ### ⚠️ HUKUM ANTI-MIXED COLOR TEMPERATURE:
> **DILARANG** mencampur cahaya jendela (daylight ~5500K) dengan lampu bohlam kuning (tungsten ~2700K) tanpa deklarasi eksplisit di prompt.
> Mixed color temperature menghasilkan warna kulit yang tidak natural (separuh wajah oranye, separuh biru).
>
> **SOLUSI:**
> 1. **Matikan lampu ruangan** dan gunakan HANYA cahaya jendela, ATAU
> 2. **Tutup jendela** dan gunakan HANYA lampu ruangan, ATAU
> 3. **Deklarasikan mixed lighting** secara eksplisit sebagai pilihan estetis: `mixed daylight-tungsten warm-cool color temperature split`

**Jenis Practical Light yang Diizinkan dalam UGC:**

| PRACTICAL LIGHT | KELVIN RANGE | KARAKTER |
|:---|:---|:---|
| Lampu meja / desk lamp | 2700K–3000K | Warm, intimate, cozy, storytime |
| Lampu neon / fluorescent | 4000K–4500K | Cool neutral, sedikit greenish cast — common di warung/kos |
| Ring light kecil (jika tersembunyi) | 3200K–5600K | Harus di-hide dari catchlight mata — TIDAK boleh terlihat bulat di iris |
| Layar laptop / HP | 5500K–6500K | Cool blue spill pada wajah, modern tech aesthetic |
| Lilin / tealight | 1800K–2200K | Ultra-warm, flickering, romantic, ASMR, intimate |
| LED strip (kamar aesthetic) | 2700K–6500K | Accent color, mood setter, background glow |
| TV / monitor besar | Variable | Color spill dinamis, flickering ambient, night scene fill |

---

## 🌳 SECTION VI: OUTDOOR NATURAL LIGHT STRATEGIES

### 6.1 Harsh Sun Management (Matahari Keras)

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         HARSH SUN SURVIVAL STRATEGIES FOR UGC                                           │
├──────────────────────┬───────────────────────────────────────────────────────────────────────────────────┤
│ STRATEGI             │ IMPLEMENTASI                                                                     │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ OPEN SHADE           │ Pindah ke area teduh terbuka (bawah kanopi, teras, gang antar bangunan).         │
│                      │ Cahaya dari langit terbuka di depan = soft directional fill.                     │
│                      │ ⚠️ Pastikan background tidak over-exposed (bright sky vs dark shade).            │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ TREE CANOPY DAPPLE   │ Dedaunan pohon = diffuser alami. Menciptakan pola cahaya dappled                │
│                      │ (bintik-bintik cahaya) yang organik dan photogenic.                             │
│                      │ ✅ Sangat cocok untuk lifestyle/casual content di taman.                         │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ BUILDING BOUNCE      │ Gedung/tembok putih di seberang = reflector raksasa alami.                       │
│                      │ Cahaya matahari memantul dari gedung → soft fill di wajah subjek.               │
│                      │ ✅ Cocok untuk street interview di trotoar perkotaan.                             │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ BACKLIT + FILL       │ Posisikan subjek membelakangi matahari (backlit), lalu isi wajah dengan         │
│                      │ bounce dari trotoar terang, dinding, atau teman memegang bahan putih.            │
│                      │ ✅ Menghasilkan rim light indah + wajah terang. Look paling "cinematic natural". │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ HAT / VISOR SHADE    │ Topi/visor menciptakan shade portabel pada wajah. Bayangan topi = diffuser.     │
│                      │ ⚠️ Bisa membuat mata terlalu gelap — pastikan ada ambient fill dari bawah.       │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────────────┤
│ SMARTPHONE TRICK     │ Tap & hold wajah pada layar HP untuk AE/AF Lock. Slide exposure ke bawah       │
│                      │ untuk menghindari highlight blow-out pada kulit.                                │
└──────────────────────┴───────────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Weather & Atmosphere Light Modifiers

| KONDISI CUACA | EFEK PADA CAHAYA | MOOD YANG DIHASILKAN |
|:---|:---|:---|
| **Cerah penuh** | Hard directional, kontras tinggi, bayangan tajam | Energik, bold, confident |
| **Mendung tipis** | Medium-soft, sedikit directional, bayangan lembut | Calm, neutral, versatile |
| **Mendung tebal** | Fully diffused, shadowless, flat | Melankolis, reflektif, intimate |
| **Hujan** | Diffused + refleksi basah di permukaan, specular highlights di genangan | Moody, cinematic, dramatic |
| **Kabut / fog** | Scatter extreme, depth compression, atmospheric haze | Mysterious, dreamy, ethereal |
| **Cerah berawan (partly cloudy)** | Intermittent — bergantian hard & soft setiap beberapa menit | Dynamic, unpredictable — WAJIB lock AE |

---

## 🌡️ SECTION VII: COLOR TEMPERATURE & WHITE BALANCE INTEGRATION

### 7.1 Master Kelvin Scale untuk Prompt Engineering

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              MASTER KELVIN COLOR TEMPERATURE SCALE                                      │
├───────────────┬──────────────────────────────────────────────────────────────────────────────────────────┤
│ KELVIN RANGE  │ SUMBER CAHAYA & KARAKTER WARNA                                                         │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ 1800K–2200K   │ Lilin, api, sunset extreme. Ultra-warm amber/oranye.                                   │
│ 2500K–3000K   │ Bohlam tungsten, lampu meja warm. Kuning hangat, cozy, intimate.                       │
│ 3000K–3500K   │ Golden hour, halogen. Warm gold, flattering skin tones.                                │
│ 4000K–4500K   │ Fluorescent, LED neutral. Cool-neutral, sedikit green cast.                            │
│ 5000K–5500K   │ Siang hari cerah, flash. Neutral white, "daylight balanced".                           │
│ 5500K–6500K   │ Siang mendung ringan, layar digital. Cool white, sedikit blue cast.                    │
│ 7000K–8000K   │ Mendung tebal, bayangan outdoor. Cool blue, overcast mood.                             │
│ 9000K–12000K  │ Blue hour, deep shade, langit utara. Deep blue, melankolis.                            │
└───────────────┴──────────────────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 White Balance Rules untuk Prompt

1. **DEKLARASIKAN SELALU** apakah prompt menggunakan "warm" atau "cool" white balance.
2. **Auto WB = DILARANG** di prompt karena menyebabkan inkonsistensi warna antar frame/clip.
3. **Skin tone anchor:** Kulit manusia harus selalu terlihat natural — tidak terlalu oranye (over-warm) dan tidak terlalu biru/abu-abu (over-cool).

---

## 🎬 SECTION VIII: HIGH-KEY vs LOW-KEY LIGHTING MODES

### 8.1 HIGH-KEY (Bright, Airy, Minimal Shadow)

```text
KARAKTERISTIK:
├── Rasio cahaya: 1:1 hingga 2:1 (bayangan sangat minimal)
├── Background: terang, putih, atau warna pastel
├── Mood: ceria, bersih, optimis, professional, trustworthy
├── Color palette: neutral, pastel, desaturated
└── UGC Use Case: Skincare/beauty review, product unboxing premium, tutorial, TikTok Shop

PENCAPAIAN NATURAL:
├── Jendela besar + dinding putih sebagai bounce
├── Overcast day (langit mendung sebagai giant softbox)
├── Subjek dekat jendela dengan vitrase putih
└── Lantai & ceiling terang (triple bounce: atas-bawah-samping)
```

### 8.2 LOW-KEY (Dark, Moody, Heavy Shadow)

```text
KARAKTERISTIK:
├── Rasio cahaya: 4:1 hingga 16:1+ (bayangan dominan)
├── Background: gelap, hitam, atau warna deep
├── Mood: dramatis, misterius, intens, konfrontatif, intimate
├── Color palette: deep tones, desaturated, monochromatic
└── UGC Use Case: Storytime serius, confession, hot take kontroversial, ASMR, night content

PENCAPAIAN NATURAL:
├── Satu lampu meja / desk lamp sebagai satu-satunya sumber (practical-driven)
├── Jendela kecil di ruangan gelap (cahaya directional kuat)
├── Night scene dengan layar HP sebagai key light (cool blue spill)
├── Negative fill: dinding gelap / selimut hitam di sisi bayangan
└── MATIKAN semua lampu kecuali satu sumber termotivasi
```

---

## 🔀 SECTION IX: MOTIVATED & PRACTICAL LIGHTING PHILOSOPHY

> [!NOTE]
> ### 📐 PRINSIP MOTIVATED LIGHTING UNTUK UGC:
> Setiap sumber cahaya dalam frame harus **TERMOTIVASI** — artinya penonton bisa secara logis mengidentifikasi dari mana cahaya itu berasal.
>
> **Contoh BENAR:** Wajah kreator terang karena duduk di samping jendela yang terlihat di frame.
> **Contoh SALAH:** Wajah kreator terang merata tanpa sumber cahaya yang terlihat/tersirat (terkesan studio).

### Motivated Light Checklist:
1. ✅ Apakah sumber cahaya utama (jendela / lampu / matahari) terlihat atau tersirat dalam frame?
2. ✅ Apakah arah bayangan konsisten dengan posisi sumber cahaya?
3. ✅ Apakah color temperature wajah sesuai dengan sumber yang terlihat?
4. ✅ Apakah intensitas cahaya masuk akal untuk jarak sumber ke subjek?
5. ✅ Apakah ada "cahaya parasit" yang tidak punya sumber logis?

---

## 🏷️ SECTION X: UNIVERSAL LIT_ID CATALOG & PROMPT BINDING

Setiap preset lighting di bawah ini memiliki kode **`LIT_ID`** resmi yang dapat langsung dideklarasikan di Layer 1 `LIGHTING RIG:` pada Modul 24.

### 10.1 INDOOR NATURAL PRESETS

| LIT_ID | NAMA PRESET | DESKRIPSI SINGKAT |
|:---|:---|:---|
| `LIT_WIN_FRONT` | Window Front Flat | Jendela besar di depan subjek, cahaya merata, bayangan minimal |
| `LIT_WIN_45` | Window Loop 45° | Jendela 45° dari subjek, loop shadow natural, dimensi lembut |
| `LIT_WIN_90` | Window Split Side | Jendela 90° dari subjek, split/Rembrandt, kontras tinggi |
| `LIT_WIN_BACK` | Window Backlit Glow | Subjek membelakangi jendela, rim light + ambient fill |
| `LIT_WIN_DIFF` | Diffused Window Soft | Jendela dengan vitrase/tirai tipis, ultra-soft wrap light |
| `LIT_PRACT_DESK` | Desk Lamp Warm Single | Satu lampu meja warm sebagai sumber utama, low-key intimate |
| `LIT_PRACT_NEON` | Fluorescent Room Cool | Lampu neon ruangan, cool-neutral, kos/warung aesthetic |
| `LIT_PRACT_CANDLE` | Candlelight Flicker | Cahaya lilin, ultra-warm, flickering, romantic/ASMR |
| `LIT_SCREEN_BLUE` | Screen Spill Night | Layar HP/laptop sebagai key light, cool blue spill pada wajah |
| `LIT_MIXED_DT` | Mixed Daylight-Tungsten | Campuran cahaya jendela + lampu ruangan, warm-cool split |
| `LIT_LED_ACCENT` | LED Strip Accent | LED strip kamar sebagai accent background, mood setter |

### 10.2 OUTDOOR NATURAL PRESETS

| LIT_ID | NAMA PRESET | DESKRIPSI SINGKAT |
|:---|:---|:---|
| `LIT_GOLD_FRONT` | Golden Hour Front | Matahari golden hour dari depan-samping, warm glow, bayangan panjang lembut |
| `LIT_GOLD_BACK` | Golden Hour Backlit | Matahari golden hour dari belakang, rim light emas, halo effect |
| `LIT_GOLD_RIM` | Golden Hour Rim Edge | Matahari golden hour dari belakang-samping, edge light emas di profil |
| `LIT_BLUE_DAWN` | Blue Hour Dawn | Cahaya blue hour pagi, biru keunguan lembut, ethereal, melankolis |
| `LIT_BLUE_DUSK` | Blue Hour Dusk | Cahaya blue hour senja, biru deep, transisi ke practical lights |
| `LIT_OVER_SOFT` | Overcast Soft Wrap | Langit mendung tebal, cahaya omnidirectional lembut, shadowless |
| `LIT_OVER_PART` | Partly Cloudy Dynamic | Langit berawan sebagian, intermittent hard/soft, dynamic |
| `LIT_HARSH_SHADE` | Harsh Sun Open Shade | Matahari keras, subjek di teduhan terbuka, soft fill dari langit |
| `LIT_HARSH_DAPPLE` | Dappled Tree Shade | Matahari melalui kanopi daun, pola bintik organik pada subjek |
| `LIT_HARSH_BOUNCE` | Building Bounce Fill | Matahari memantul dari gedung/tembok putih, soft urban fill |
| `LIT_STREET_NIGHT` | Urban Night Practicals | Malam kota, campuran lampu jalan + neon toko + kendaraan |
| `LIT_RAIN_WET` | Rainy Diffused Specular | Hujan, cahaya diffused + refleksi basah, specular genangan |
| `LIT_FOG_HAZE` | Fog Atmospheric Scatter | Kabut, cahaya tersebar, depth compression, dreamy haze |
| `LIT_NOON_DIRECT` | Direct Noon Overhead | Matahari tengah hari langsung, bayangan keras pendek, kontras extreme |
| `LIT_AFTERNOON` | Afternoon Transitional | Siang menuju sore, cahaya mulai menghangat, kontras sedang |

### 10.3 SPECIAL / HYBRID PRESETS

| LIT_ID | NAMA PRESET | DESKRIPSI SINGKAT |
|:---|:---|:---|
| `LIT_CHIAROSCURO` | Chiaroscuro Natural | Kontras extreme ala Caravaggio, satu sumber kuat + deep shadow |
| `LIT_HIGHKEY_CLEAN` | High-Key Clean Bright | Bright, airy, minimal shadow, beauty/commerce look |
| `LIT_LOWKEY_MOODY` | Low-Key Moody Dark | Dark, shadow-heavy, single motivated source |
| `LIT_SILHOUETTE` | Full Silhouette Backlit | Subjek 100% silhouette, hanya outline terlihat |
| `LIT_BUTTERFLY_WIN` | Butterfly Window Pattern | Pola butterfly dari jendela atas-depan, glamour natural |
| `LIT_REMBRANDT_WIN` | Rembrandt Window Pattern | Pola Rembrandt dari jendela samping, triangle of light |
| `LIT_LOOP_NATURAL` | Loop Natural Ambient | Pola loop dari cahaya ambient, everyday natural look |
| `LIT_SPLIT_DRAMATIC` | Split Dramatic Side | Pola split dari satu sumber samping, half-face shadow |

---

## ✅ SECTION XI: PROMPT INTEGRATION SYNTAX

### 11.1 Layer 1 LIGHTING RIG Declaration Format

Saat mendeklarasikan lighting di Layer 1 Modul 24, gunakan format berikut:

```text
LIGHTING RIG: [LIT_ID] — [deskripsi natural source], [direction], [quality], [color temp], [ratio], [shadow behavior], [motivated source visible in frame]
```

**Contoh lengkap:**

```text
LIGHTING RIG: LIT_WIN_45 — Soft natural window light from left side at 45-degree angle,
warm afternoon daylight ~4800K filtering through thin white curtain (diffused),
2:1 lighting ratio with gentle loop shadow from nose to left cheek,
ambient fill from cream-colored wall bounce on shadow side,
window frame partially visible at frame-left edge (motivated source confirmed),
natural CMOS highlight roll-off on forehead and cheekbone specular,
subtle warm-to-cool gradient across face following window fall-off distance
```

### 11.2 Mandatory Lighting Prompt Checklist

Setiap prompt yang melibatkan karakter manusia **WAJIB** mendeklarasikan minimal:

- [ ] **Sumber cahaya utama** (jendela / matahari / lampu praktis)
- [ ] **Arah cahaya** (front / side / back / top / rim)
- [ ] **Kualitas cahaya** (hard / soft / diffused / dappled)
- [ ] **Color temperature** (Kelvin range atau deskriptif warm/cool/neutral)
- [ ] **Lighting ratio** (rasio atau deskriptif low-contrast / medium / high-contrast)
- [ ] **Motivasi sumber** (apakah sumber terlihat/tersirat dalam frame)
- [ ] **Perilaku bayangan** (arah jatuh, intensitas, softness)

---

## 🛡️ SECTION XII: ZERO-DEFECT LIGHTING AUDIT MATRIX

> [!CAUTION]
> ### 🔍 CHECKLIST AUDIT LIGHTING (WAJIB LULUS SEMUA):

| # | CHECKPOINT | PASS CRITERIA |
|:---|:---|:---|
| L01 | Sumber cahaya termotivasi? | Setiap area terang pada subjek harus bisa di-trace ke sumber logis |
| L02 | Bayangan konsisten? | Semua bayangan jatuh ke arah yang sama, sesuai posisi sumber utama |
| L03 | Color temperature selaras? | Tidak ada mixed color cast kecuali dideklarasikan eksplisit |
| L04 | Skin tone natural? | Kulit tidak plastik, tidak zombie-grey, tidak neon-orange |
| L05 | Tidak ada ring light? | Catchlight mata TIDAK menunjukkan bentuk bulat ring light |
| L06 | Tidak ada studio light? | Tidak ada softbox reflection, beauty dish glow, atau strobe shadow |
| L07 | Catchlight mata realistis? | Catchlight = bentuk jendela / langit / lampu ruangan, bukan studio gear |
| L08 | Highlight tidak blow-out? | Kulit dan objek terang masih memiliki detail tekstur, bukan putih solid |
| L09 | Shadow masih readable? | Area gelap masih memiliki detail, bukan hitam solid (kecuali silhouette) |
| L10 | Solar cycle konsisten? | Warna langit, panjang bayangan, dan intensitas sesuai fase yang dipilih |
| L11 | Lighting ratio sesuai mood? | Kontras visual selaras dengan tone narasi (ceria = low ratio, dramatis = high) |
| L12 | Inverse square law? | Objek lebih dekat ke sumber = lebih terang, lebih jauh = lebih gelap secara gradual |
| L13 | Form shadow anatomis? | Form shadow pada wajah/tubuh membentuk volume 3D, bukan flat patch gelap |
| L14 | Cast shadow grounded? | Cast shadow menyentuh contact point objek, tidak melayang/terputus |
| L15 | Penumbra konsisten? | Tepi bayangan (soft/hard) sesuai ukuran & jarak sumber cahaya |
| L16 | Specular highlight natural? | Specular pada kulit = micro-glint di T-zone/bibir, bukan seluruh wajah |
| L17 | Subsurface scattering? | Backlit ears/nostrils/thin skin menunjukkan warm translucent glow |
| L18 | Shadow direction unity? | SEMUA bayangan (wajah + tubuh + props + environment) mengarah konsisten |
| L19 | Light fall-off gradual? | Transisi terang→gelap gradual sesuai jarak, bukan cut-off tajam |
| L20 | Hair/rim glow realistis? | Rim light pada rambut = edge highlight tipis, bukan neon glow tube |

---

## 🕳️ SECTION XIII: SHADOW ANATOMY & TAXONOMY ENGINE

Bayangan bukan sekadar "area gelap" — setiap bayangan memiliki anatomi yang harus akurat secara fisika untuk menghasilkan visual yang believable.

### 13.1 Dua Kategori Utama Bayangan

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 2 FUNDAMENTAL SHADOW CATEGORIES                                        │
├──────────────────┬───────────────────────────────────────────────────────────────────────────────────────┤
│ KATEGORI         │ DEFINISI & KARAKTERISTIK                                                             │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ 1. FORM SHADOW   │ Bayangan yang terbentuk PADA permukaan subjek itu sendiri — area yang                │
│    (Self-Shadow) │ membelakangi/miring dari sumber cahaya. Membentuk persepsi VOLUME 3D.               │
│                  │ Contoh: sisi gelap hidung, pipi, dahi yang tidak terkena cahaya langsung.            │
│                  │ 🎯 FUNGSI: Mendefinisikan bentuk 3-dimensi wajah & tubuh.                           │
│                  │ ⚠️ Tanpa form shadow = wajah terlihat FLAT & 2D (seperti flash frontal).            │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ 2. CAST SHADOW   │ Bayangan yang DIPROYEKSIKAN oleh subjek ke permukaan lain (lantai, dinding,         │
│    (Projected)   │ meja, orang lain). Menunjukkan HUBUNGAN SPASIAL antar objek.                        │
│                  │ Contoh: bayangan tubuh di trotoar, bayangan tangan di meja, bayangan                 │
│                  │ hidung di pipi (dalam Rembrandt lighting).                                           │
│                  │ 🎯 FUNGSI: Grounding subjek ke environment, menunjukkan posisi matahari.             │
│                  │ ⚠️ Tanpa cast shadow = subjek tampak MELAYANG / tidak terhubung ke dunia.            │
└──────────────────┴───────────────────────────────────────────────────────────────────────────────────────┘
```

### 13.2 Anatomi Detail Bayangan (6 Komponen)

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 6-COMPONENT SHADOW ANATOMY MAP                                         │
├──────────────────┬──────────┬────────────────────────────────────────────────────────────────────────────┤
│ KOMPONEN         │ LOKASI   │ DESKRIPSI & PROMPT CUE                                                    │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 1. CORE SHADOW   │ FORM     │ Bagian TERGELAP dari form shadow, terletak di "terminator line"           │
│                  │          │ (garis transisi terang→gelap). Strip gelap sempit di batas                 │
│                  │          │ antara area terkena cahaya dan area bayangan.                              │
│                  │          │ Prompt: "visible core shadow strip along the light-to-shadow              │
│                  │          │ terminator on the nose bridge and cheekbone edge"                          │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 2. TERMINATOR    │ FORM     │ Garis batas antara area terang dan area gelap pada subjek.                │
│    LINE          │          │ Bisa TAJAM (hard light) atau GRADUAL (soft light).                        │
│                  │          │ Prompt: "soft gradual terminator line across the face" atau               │
│                  │          │ "sharp crisp terminator dividing light and shadow"                        │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 3. REFLECTED     │ FORM     │ Cahaya pantul (bounce) dari lantai/dinding/environment yang               │
│    LIGHT (BOUNCE)│          │ sedikit menerangi sisi gelap subjek. Jauh lebih lemah dari key            │
│                  │          │ light. Biasanya terlihat sebagai glow subtle di tepi jaw/leher            │
│                  │          │ pada sisi bayangan.                                                       │
│                  │          │ Prompt: "faint reflected bounce light on the shadow-side jaw              │
│                  │          │ from the light-colored floor below"                                       │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 4. CONTACT       │ CAST     │ Area PALING GELAP dari cast shadow, tepat di titik dimana objek           │
│    SHADOW        │          │ menyentuh permukaan (kaki di lantai, tangan di meja, dagu di leher).      │
│    (OCCLUSION)   │          │ Memberikan "grounding" — tanpa ini, objek tampak mengambang.              │
│                  │          │ Prompt: "deep dark contact shadow where feet meet the sidewalk,           │
│                  │          │ grounding the subject to the pavement surface"                            │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 5. UMBRA         │ CAST     │ Bagian tengah/inti dari cast shadow yang paling gelap, dimana             │
│                  │          │ sumber cahaya sepenuhnya terblokir oleh objek.                            │
│                  │          │ Prompt: "dark umbra core of the cast shadow on the wall behind"           │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 6. PENUMBRA      │ CAST     │ Tepi luar cast shadow yang lebih lembut/buram — area transisi            │
│                  │          │ dimana sumber cahaya hanya terblokir sebagian. Semakin besar              │
│                  │          │ sumber cahaya = penumbra semakin lebar & lembut.                          │
│                  │          │ Prompt: "wide soft penumbra edges on the cast shadow from the             │
│                  │          │ large overcast sky source" atau "narrow sharp penumbra from               │
│                  │          │ the small direct sun source"                                              │
└──────────────────┴──────────┴────────────────────────────────────────────────────────────────────────────┘
```

### 13.3 Shadow Anatomy pada Wajah Manusia (Face Shadow Map)

```text
                    ┌─────────────────────────┐
                    │      FOREHEAD           │
                    │   (form shadow jika     │
                    │    cahaya dari bawah)   │
                    ├────────┬────────┬───────┤
                    │ BROW   │        │  BROW │
                    │ SHADOW │  NOSE  │ SHADOW│  ◄── Alis menciptakan cast shadow
                    │(cast)  │ BRIDGE │ (cast)│      ke kelopak mata
                    ├────────┤        ├───────┤
                    │  EYE   │        │  EYE  │
                    │ SOCKET │        │ SOCKET│  ◄── Orbital shadow (form + cast)
                    ├────────┴───┬────┴───────┤
                    │            │            │
                    │  CHEEK     │ NOSE SHADOW│  ◄── Cast shadow hidung ke pipi
                    │  (form)    │ (cast)     │      = Loop / Rembrandt / Split
                    ├────────────┼────────────┤
                    │   UPPER    │   UPPER    │
                    │   LIP      │   LIP      │  ◄── Philtrum cast shadow dari hidung
                    │  SHADOW    │  SHADOW    │
                    ├────────────┴────────────┤
                    │      CHIN SHADOW        │  ◄── Cast shadow dagu ke leher
                    │   (cast ke leher/dada)  │      = WAJIB ADA untuk grounding
                    └─────────────────────────┘
```

**Aturan Wajib Face Shadow:**
1. **Nose shadow** harus SELALU ada (kecuali 100% front flat light) — bentuknya mendefinisikan lighting pattern.
2. **Chin-to-neck shadow** harus SELALU ada — tanpa ini, kepala tampak "ditempel" ke tubuh.
3. **Orbital/eye socket shadow** memberikan kedalaman mata — tanpa ini, mata terlihat datar.
4. **Brow ridge shadow** memberikan dimensi pada dahi — terutama penting pada side lighting.

---

## 🔬 SECTION XIV: SHADOW QUALITY PHYSICS ENGINE

Kualitas bayangan (tajam vs lembut) ditentukan oleh hukum fisika optik yang harus dipatuhi secara ketat.

### 14.1 Hard vs Soft Shadow Determinants

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              SHADOW QUALITY DETERMINATION MATRIX                                        │
├───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────┤
│ FAKTOR            │ HARD SHADOW                  │ SOFT SHADOW                                          │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ UKURAN SUMBER     │ Kecil relatif terhadap subjek│ Besar relatif terhadap subjek                        │
│ CAHAYA            │ (matahari langsung, spot lamp│ (langit mendung, jendela besar, softbox alam)        │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ JARAK SUMBER      │ Jauh dari subjek             │ Dekat ke subjek                                      │
│ KE SUBJEK         │ (ukuran apparent mengecil)   │ (ukuran apparent membesar)                           │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ TEPI BAYANGAN     │ Tajam, well-defined, crisp   │ Gradual, buram, feathered, smooth transition         │
│ (EDGE)            │ Penumbra sempit / tidak ada  │ Penumbra lebar                                       │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ KONTRAS           │ Tinggi — terang vs gelap     │ Rendah — transisi halus                              │
│                   │ sangat jelas terbedakan      │ terang & gelap bercampur gradual                     │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ TEKSTUR KULIT     │ Sangat teraksentuasi — pori, │ Diminimalkan — kulit tampak lebih halus              │
│                   │ kerut, bekas jerawat terlihat│ dan flawless (tanpa filter buatan)                   │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ MOOD              │ Dramatis, intens, tajam,     │ Lembut, tenang, warm, approachable,                  │
│                   │ energik, confrontational     │ intimate, comforting                                 │
├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────┤
│ SUMBER NATURAL    │ • Matahari langsung cerah    │ • Langit mendung (giant softbox)                     │
│ YANG UMUM         │ • Lampu bohlam bare/kecil    │ • Jendela besar + tirai tipis                        │
│                   │ • Layar HP (relatif kecil)   │ • Open shade (teduhan terbuka)                       │
│                   │ • Lilin (titik kecil)        │ • Golden hour (matahari rendah + atmosfer tebal)     │
└───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────┘
```

### 14.2 Shadow Edge Transition Scale (5 Tingkat)

| LEVEL | NAMA | TEPI BAYANGAN | SUMBER TYPICAL | PROMPT CUE |
|:---|:---|:---|:---|:---|
| **1** | Razor Sharp | Garis tajam tanpa gradasi | Matahari langsung, bare bulb kecil | `razor-sharp shadow edges, zero penumbra` |
| **2** | Crisp | Tajam dengan penumbra sangat tipis | Matahari pagi/sore langsung, spot | `crisp shadow edges with minimal penumbra` |
| **3** | Medium | Transisi sedang, tepi terlihat tapi tidak tajam | Jendela medium, partly cloudy | `medium shadow edge with visible gradual transition` |
| **4** | Soft | Transisi gradual, tepi bayangan buram | Jendela besar + vitrase, overcast | `soft diffused shadow edges, wide gentle penumbra` |
| **5** | Ultra-Soft | Hampir tidak terlihat, bayangan sangat tipis | Mendung tebal, multiple bounce | `nearly invisible ultra-soft shadows, ambient wrap` |

### 14.3 Shadow Density Scale (5 Tingkat)

| LEVEL | NAMA | KEGELAPAN | DETAIL DI SHADOW | PROMPT CUE |
|:---|:---|:---|:---|:---|
| **1** | Transparent | Bayangan sangat tipis, hampir tidak ada | Full detail terlihat | `transparent minimal shadows, nearly flat` |
| **2** | Light | Bayangan terlihat tapi ringan | Detail penuh terlihat | `light airy shadows, full detail in shadow areas` |
| **3** | Medium | Bayangan jelas, kontras sedang | Detail sebagian terlihat | `medium density shadows, partial detail visible` |
| **4** | Deep | Bayangan gelap, kontras tinggi | Detail samar-samar | `deep dense shadows, minimal detail in dark areas` |
| **5** | Crushed Black | Bayangan hitam pekat | Tidak ada detail (silhouette) | `crushed black shadows, zero shadow detail` |

> [!WARNING]
> ### ⚠️ HUKUM KONSISTENSI SHADOW QUALITY:
> Shadow edge dan shadow density harus **KONSISTEN** di seluruh frame:
> - Jika bayangan hidung soft → bayangan tangan, tubuh, dan props juga HARUS soft.
> - Jika bayangan cast di lantai razor-sharp → bayangan di wajah juga HARUS hard-edged.
> - **DILARANG** mencampur hard shadow di wajah dengan soft shadow di environment (kecuali ada 2+ sumber cahaya yang dideklarasikan eksplisit).

---

## ✨ SECTION XV: HIGHLIGHT & REFLECTION TAXONOMY ENGINE

Highlight adalah pasangan komplementer dari shadow — keduanya bekerja bersama membentuk persepsi volume 3D.

### 15.1 Jenis-Jenis Highlight

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 4-TYPE HIGHLIGHT TAXONOMY                                              │
├──────────────────┬──────────┬────────────────────────────────────────────────────────────────────────────┤
│ JENIS            │ INTENSITAS│ DESKRIPSI & LOKASI PADA SUBJEK                                           │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 1. SPECULAR      │ ●●●●●    │ Pantulan langsung cahaya dari permukaan licin/mengkilap.                  │
│    HIGHLIGHT     │ (max)    │ Titik paling terang pada subjek. Tajam & fokus.                           │
│                  │          │ Lokasi: ujung hidung, dahi (T-zone berminyak), bibir basah,                │
│                  │          │ mata (catchlight), layar HP, kaca, perhiasan.                             │
│                  │          │ Prompt: "sharp specular highlight on the nose tip and oily                 │
│                  │          │ T-zone forehead, tiny bright glint on wet lower lip"                      │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 2. DIFFUSE       │ ●●●○○    │ Pantulan tersebar dari permukaan matte/kasar.                             │
│    HIGHLIGHT     │ (medium) │ Area terang yang luas & gradual, tanpa titik fokus tajam.                  │
│                  │          │ Lokasi: pipi (area terluas terkena cahaya), dahi area luas,                │
│                  │          │ kain baju, kulit matte.                                                   │
│                  │          │ Prompt: "broad diffuse highlight across the sunlit cheek,                  │
│                  │          │ gentle luminous glow without sharp hot-spots"                             │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 3. CATCHLIGHT    │ ●●●●○    │ Pantulan sumber cahaya yang terlihat DI DALAM iris/pupil mata.            │
│    (EYE LIGHT)   │ (high)   │ Memberikan "kehidupan" & sparkle pada tatapan subjek.                     │
│                  │          │ Bentuk catchlight = bentuk sumber cahaya (jendela = kotak,                │
│                  │          │ langit = amorphous, ring light = bulat ← DILARANG).                       │
│                  │          │ Prompt: "rectangular window-shaped catchlight in both eyes,                │
│                  │          │ positioned at 10 o'clock, adding life and sparkle to gaze"                │
├──────────────────┼──────────┼────────────────────────────────────────────────────────────────────────────┤
│ 4. RIM /         │ ●●●○○    │ Garis cahaya tipis di tepi/kontur subjek (rambut, bahu, profil            │
│    EDGE          │ (medium) │ wajah) yang tercipta dari backlighting atau side-backlighting.             │
│    HIGHLIGHT     │          │ Memisahkan subjek dari background. BUKAN neon glow — harus                │
│                  │          │ tipis & subtle.                                                           │
│                  │          │ Prompt: "thin natural rim highlight along the hair and shoulder            │
│                  │          │ edge from the low golden-hour backlight, subtle separation glow"           │
└──────────────────┴──────────┴────────────────────────────────────────────────────────────────────────────┘
```

### 15.2 Catchlight Shape Reference (Anti-Studio Compliance)

| SUMBER CAHAYA | BENTUK CATCHLIGHT | STATUS |
|:---|:---|:---|
| Jendela persegi | Kotak/persegi panjang | ✅ ALLOWED — paling natural untuk indoor |
| Langit terbuka | Amorphous / irregular bright area | ✅ ALLOWED — outdoor look |
| Lampu meja | Titik kecil / irregular | ✅ ALLOWED — practical light |
| Layar HP/laptop | Kotak kecil biru-putih | ✅ ALLOWED — modern UGC |
| Pohon/dedaunan | Scattered irregular dots | ✅ ALLOWED — outdoor dappled |
| Ring light | ⭕ Bulat sempurna | 🚫 **DILARANG KERAS** — studio giveaway |
| Softbox | □ Kotak seragam terang | 🚫 **DILARANG** — studio equipment |
| Beauty dish | ◎ Bulat dengan titik tengah | 🚫 **DILARANG** — studio equipment |
| Octabox | ⬡ Oktagonal | 🚫 **DILARANG** — studio equipment |

### 15.3 Highlight Roll-Off Behavior

| TIPE ROLL-OFF | KARAKTERISTIK | SUMBER TYPICAL | UGC COMPLIANCE |
|:---|:---|:---|:---|
| **Harsh Clip** | Highlight langsung putih solid, tanpa gradasi | Flash, strobe, studio | 🚫 DILARANG — artificial look |
| **Abrupt** | Transisi cepat dari terang ke medium | Matahari langsung keras | ⚠️ HATI-HATI — bisa blow-out |
| **Natural CMOS** | Gradasi halus dari terang ke medium, highlight masih punya tekstur kulit | Smartphone camera sensor | ✅ TARGET — simulasikan ini |
| **Gentle Roll** | Transisi sangat halus & panjang | Soft diffused window, overcast | ✅ IDEAL — paling flattering |

---

## 🧬 SECTION XVI: SKIN-LIGHT INTERACTION & SUBSURFACE SCATTERING ENGINE

Kulit manusia BUKAN permukaan opaque solid — cahaya menembus lapisan kulit dan berinteraksi secara kompleks.

### 16.1 Subsurface Scattering (SSS) — Cahaya Menembus Kulit

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              SUBSURFACE SCATTERING ON HUMAN SKIN                                        │
├──────────────────┬───────────────────────────────────────────────────────────────────────────────────────┤
│ FENOMENA         │ DESKRIPSI & KAPAN TERLIHAT                                                           │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ EAR GLOW         │ Saat cahaya (terutama backlight/rim light) menembus daun telinga yang tipis,         │
│ (Telinga Bersinar│ telinga tampak bersinar warm-red/amber dari dalam. Sangat terlihat pada             │
│  dari Dalam)     │ golden hour backlit atau saat subjek berdiri di depan jendela terang.               │
│                  │ Prompt: "warm reddish-amber subsurface glow through the backlit ear,                │
│                  │ translucent skin revealing blood vessel warmth"                                      │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ NOSTRIL GLOW     │ Cahaya menembus cuping hidung tipis, menciptakan warm glow di sekitar               │
│ (Hidung Trans-   │ lubang hidung. Subtle tapi penting untuk realisme.                                  │
│  lucent Glow)    │ Prompt: "subtle warm translucent glow at the thin nostril edges"                    │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ FINGER GLOW      │ Saat jari menutupi senter HP atau cahaya kuat dari belakang, jari-jari              │
│ (Jari Tembus     │ bersinar merah/oranye karena cahaya menembus jaringan dan darah.                    │
│  Cahaya)         │ Prompt: "warm red-orange subsurface scatter through backlit thin fingers"           │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ SKIN EDGE GLOW   │ Di tepi wajah/leher yang backlit, terdapat garis tipis warm glow dimana             │
│ (Tepi Kulit      │ cahaya menembus lapisan kulit paling tipis.                                         │
│  Bercahaya)      │ Prompt: "thin warm subsurface edge glow along the backlit jawline contour"          │
├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ HAIR HALO        │ Rambut halus (baby hair, fine hair) yang backlit menciptakan halo bercahaya         │
│ (Lingkaran       │ di sekitar kepala. Warna = sesuai color temp sumber (golden = warm halo,            │
│  Cahaya Rambut)  │ daylight = neutral-cool halo).                                                      │
│                  │ Prompt: "delicate warm golden halo around fine flyaway hair strands                 │
│                  │ from low backlight golden hour sun"                                                 │
└──────────────────┴───────────────────────────────────────────────────────────────────────────────────────┘
```

### 16.2 Skin Surface Micro-Phenomena

| FENOMENA | KONDISI TRIGGER | EFEK VISUAL | PROMPT CUE |
|:---|:---|:---|:---|
| **T-Zone Oil Sheen** | Kulit berminyak + any light | Specular micro-highlights di dahi, hidung, dagu | `natural oily T-zone specular sheen` |
| **Peach Fuzz Glow** | Backlight / rim light | Bulu halus wajah bercahaya tipis | `fine peach fuzz catching the rim light along the cheek` |
| **Pore Texture** | Side light / hard light | Pori-pori terlihat sebagai micro-shadow dots | `visible natural pore texture in side-lit skin` |
| **Sweat Beading** | Outdoor panas / aktivitas | Butiran keringat = micro-specular highlights | `tiny sweat bead specular highlights on the temple and upper lip` |
| **Blush / Flush** | Emosi, panas, malu | Area pipi/telinga/leher lebih merah/pink | `natural emotional blush warmth on cheeks and ear tips` |
| **Under-Eye Translucency** | Kulit tipis + any light | Area bawah mata sedikit keunguan/kebiruan | `delicate bluish translucent under-eye skin` |
| **Lip Moisture** | Bibir basah + any light | Specular highlights kecil di bibir bawah | `wet lip surface catching a tiny specular highlight` |

---

## 🧭 SECTION XVII: SHADOW-SUN DIRECTIONAL CONSISTENCY ENGINE

> [!CAUTION]
> ### 🚨 HUKUM TERTINGGI KONSISTENSI BAYANGAN:
> **SEMUA bayangan dalam satu frame WAJIB mengarah ke arah yang SAMA.**
>
> Jika bayangan hidung jatuh ke kanan → bayangan tangan jatuh ke kanan → bayangan tubuh di lantai jatuh ke kanan → bayangan pohon di background jatuh ke kanan.
>
> **Bayangan yang mengarah ke arah berbeda-beda = DEFECT FATAL** yang langsung membuat visual terlihat artificial/AI-generated.

### 17.1 Shadow Direction vs Solar Altitude

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    SHADOW DIRECTION & LENGTH vs SOLAR ALTITUDE TABLE                                    │
├────────────────────┬────────────┬────────────────────┬──────────────────────────────────────────────────┤
│ SOLAR ALTITUDE     │ WAKTU      │ PANJANG BAYANGAN   │ ARAH BAYANGAN                                    │
├────────────────────┼────────────┼────────────────────┼──────────────────────────────────────────────────┤
│ 5°–15°             │ Sunrise/   │ Sangat panjang     │ Berlawanan arah matahari.                        │
│ (sangat rendah)    │ Sunset     │ (6–11x tinggi      │ Sunrise dari timur → bayangan ke BARAT.          │
│                    │            │ objek)             │ Sunset dari barat → bayangan ke TIMUR.           │
├────────────────────┼────────────┼────────────────────┼──────────────────────────────────────────────────┤
│ 15°–30°            │ Pagi awal/ │ Panjang            │ Masih berlawanan arah matahari,                  │
│ (rendah)           │ Sore akhir │ (2–4x tinggi       │ sudut mulai menurun.                             │
│                    │            │ objek)             │                                                  │
├────────────────────┼────────────┼────────────────────┼──────────────────────────────────────────────────┤
│ 30°–60°            │ Mid-       │ Sedang             │ Bayangan mulai pendek, masih mengarah            │
│ (medium)           │ morning/   │ (0.6–2x tinggi     │ berlawanan matahari tapi lebih compact.          │
│                    │ Afternoon  │ objek)             │                                                  │
├────────────────────┼────────────┼────────────────────┼──────────────────────────────────────────────────┤
│ 60°–85°            │ Mendekati  │ Pendek             │ Bayangan sangat pendek, nyaris tepat di          │
│ (tinggi)           │ tengah     │ (0.1–0.6x tinggi   │ bawah objek.                                     │
│                    │ hari       │ objek)             │                                                  │
├────────────────────┼────────────┼────────────────────┼──────────────────────────────────────────────────┤
│ 85°–90°            │ Tengah     │ Minimal / hampir   │ Bayangan tepat di bawah kaki, nyaris             │
│ (tepat di atas)    │ hari tepat │ tidak ada          │ tidak terlihat (tropis di tengah hari).          │
└────────────────────┴────────────┴────────────────────┴──────────────────────────────────────────────────┘
```

### 17.2 Multi-Object Shadow Consistency Checklist

| # | CHECK ITEM | ATURAN |
|:---|:---|:---|
| S01 | Bayangan wajah (nose shadow) | Arah sesuai posisi sumber utama |
| S02 | Bayangan tubuh di lantai | Arah & panjang konsisten dengan solar altitude |
| S03 | Bayangan tangan / lengan | Mengarah SAMA dengan bayangan tubuh utama |
| S04 | Bayangan props (HP, tas, gelas) | Mengarah SAMA dengan bayangan subjek |
| S05 | Bayangan environment (tiang, pohon, kursi) | Mengarah SAMA — SEMUA paralel |
| S06 | Bayangan orang lain di scene | Mengarah & panjang IDENTIK dengan subjek utama |
| S07 | Bayangan contact point | Ada di SETIAP titik kontak objek-permukaan |
| S08 | Bayangan indoor | Konsisten dengan arah jendela/lampu yang dideklarasikan |

---

## 📐 SECTION XVIII: LIGHT FALL-OFF & INVERSE SQUARE LAW ENGINE

### 18.1 Prinsip Inverse Square Law

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              INVERSE SQUARE LAW — LIGHT INTENSITY vs DISTANCE                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│   Intensitas cahaya berbanding terbalik dengan KUADRAT jarak dari sumber.                               │
│   Jika jarak DIGANDAKAN → intensitas turun menjadi 1/4 (25%)                                            │
│   Jika jarak DITRIPLEKAN → intensitas turun menjadi 1/9 (11%)                                           │
│                                                                                                         │
│   ┌─────┐                                                                                               │
│   │LIGHT│──1m──►[100%]──2m──►[25%]──3m──►[11%]──4m──►[6%]                                               │
│   │ SRC │                                                                                               │
│   └─────┘                                                                                               │
│                                                                                                         │
│   IMPLIKASI VISUAL:                                                                                     │
│   • Sumber DEKAT ke subjek = fall-off CEPAT (wajah terang, background gelap drastis)                    │
│   • Sumber JAUH dari subjek = fall-off LAMBAT (subjek & background hampir sama terang)                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 18.2 Light Wrap & Ambient Fill Interaction

| WRAP LEVEL | PROMPT CUE | KONDISI |
|:---|:---|:---|
| **No Wrap** | `hard terminator, no light wrap to shadow side` | Small source, hard light |
| **Minimal Wrap** | `slight light wrap just past the terminator edge` | Medium source, moderate distance |
| **Soft Wrap** | `gentle light wrap around the face, gradual transition` | Large source close (window, overcast) |
| **Full Wrap** | `full ambient wrap, light coming from nearly all directions` | Massive source (overcast sky, white room) |

---

## 🔄 SECTION XIX: SHADOW & HIGHLIGHT INTERACTION — THE COMPLETE TONAL MAP

### 19.1 The 7-Zone Tonal Map pada Wajah Manusia

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    THE 7-ZONE FACIAL TONAL MAP (Light Side → Shadow Side)                               │
├──────┬───────────────────┬───────────────────────────────────────────────────────────────────────────────┤
│ ZONE │ NAMA              │ DESKRIPSI                                                                    │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  1   │ SPECULAR          │ Titik paling terang — pantulan langsung cahaya (ujung hidung, T-zone,       │
│      │ HIGHLIGHT         │ bibir basah). Tiny, intense, sharp.                                         │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  2   │ DIFFUSE           │ Area luas yang terang tapi tanpa hotspot — pipi sisi cahaya, dahi,          │
│      │ HIGHLIGHT         │ area yang menghadap sumber. Broad, luminous, soft.                          │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  3   │ MIDTONE           │ Area transisi — tidak terang, tidak gelap. Zona baseline warna kulit         │
│      │ (HALFTONE)        │ natural. Paling representatif dari actual skin color.                       │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  4   │ TERMINATOR        │ Garis/band transisi terang→gelap. Bisa tajam (hard light) atau              │
│      │ (TRANSITION)      │ gradual/wide (soft light). Sering berisi core shadow.                       │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  5   │ CORE SHADOW       │ Strip paling gelap di batas form shadow. Lebih gelap dari area              │
│      │                   │ bayangan umum karena tidak menerima cahaya langsung NOR bounce.              │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  6   │ FORM SHADOW       │ Area umum sisi gelap wajah. Lebih terang dari core shadow karena            │
│      │ (BODY)            │ menerima sedikit ambient bounce dari environment.                           │
├──────┼───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│  7   │ REFLECTED LIGHT   │ Cahaya pantul subtle di tepi sisi gelap (jawline, leher) dari               │
│      │ (BOUNCE)          │ lantai/dinding/environment. Lebih terang dari form shadow body.              │
│      │                   │ ⚠️ WAJIB lebih lemah dari diffuse highlight — jika lebih terang,             │
│      │                   │    terlihat seperti ada 2 sumber cahaya (tidak natural).                     │
└──────┴───────────────────┴───────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 SECTION XX: EXPANDED MANDATORY LIGHTING PROMPT CHECKLIST V2

### 20.1 Full Checklist (20 Poin)

Setiap prompt yang melibatkan karakter manusia **WAJIB** mendeklarasikan:

**— LIGHT SOURCE & DIRECTION —**
- [ ] **Sumber cahaya utama** (jendela / matahari / lampu praktis / layar)
- [ ] **Arah cahaya** (front / side 45° / side 90° / back / top / rim)
- [ ] **Kualitas cahaya** (hard / soft / diffused / dappled)
- [ ] **Color temperature** (Kelvin range atau deskriptif warm/cool/neutral)

**— SHADOW CHARACTERISTICS —**
- [ ] **Shadow edge quality** (razor-sharp / crisp / medium / soft / ultra-soft)
- [ ] **Shadow density** (transparent / light / medium / deep / crushed)
- [ ] **Shadow direction** (semua bayangan mengarah ke arah yang sama)
- [ ] **Nose shadow pattern** (butterfly / loop / Rembrandt / split / none)
- [ ] **Chin-to-neck shadow** (ada / tegas / lembut)
- [ ] **Contact shadows** (ada di setiap titik kontak objek-permukaan)

**— HIGHLIGHT CHARACTERISTICS —**
- [ ] **Specular highlights** (lokasi: ujung hidung, T-zone, bibir, mata)
- [ ] **Catchlight shape** (bentuk sumber cahaya di iris — BUKAN ring/softbox)
- [ ] **Highlight roll-off** (natural CMOS / gentle / abrupt)
- [ ] **Rim/edge highlight** (ada/tidak, dari arah mana, intensitas)

**— SKIN-LIGHT INTERACTION —**
- [ ] **Subsurface scattering** (ear glow, nostril glow jika backlit)
- [ ] **Skin texture visibility** (pori-pori terlihat jika side-lit)
- [ ] **Oil sheen / sweat** (T-zone specular jika relevan)

**— PHYSICS & CONSISTENCY —**
- [ ] **Lighting ratio** (rasio atau deskriptif kontras level)
- [ ] **Fall-off behavior** (cepat/sedang/lambat sesuai jarak sumber)
- [ ] **Motivated source** (sumber terlihat/tersirat dalam frame)
