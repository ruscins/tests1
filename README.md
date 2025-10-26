# 🎬 AutoSkola Video Reklāmas Ģenerators

Automātisks reklāmas video ģenerators autoskolai ar Python un MoviePy.

## 📋 Prasības

- Python 3.8 vai jaunāks
- FFmpeg instalēts sistēmā

## 🚀 Instalācija

### 1. Klonē repozitoriju
```bash
git clone https://github.com/ruscins/tests1.git
cd tests1
```

### 2. Instalē Python bibliotēkas
```bash
pip install -r requirements.txt
```

### 3. Instalē FFmpeg

**Windows:**
- Lejupielādē no https://ffmpeg.org/download.html
- Pievieno FFmpeg pie PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## 🎥 Lietošana

### Pamata komanda:
```bash
python generate_ad.py
```

### Ar pielāgotiem parametriem:
```bash
python generate_ad.py --duration 15 --style modern
```

### Parametri:
- `--duration` - Video garums sekundēs (default: 20)
- `--style` - Stils: classic, modern, minimal (default: modern)
- `--output` - Izvades faila nosaukums (default: output/autoskola_ad.mp4)

## 📁 Projekta struktūra

```
tests1/
├── generate_ad.py          # Galvenais skripts
├── config.yaml             # Konfigurācija
├── requirements.txt        # Python bibliotēkas
├── README.md              # Šis fails
├── PIEMERI.md             # Lietošanas piemēri
├── assets/                # Resursi
│   ├── images/            # Bildes (lietus, auto, u.c.)
│   ├── fonts/             # Fonti
│   └── audio/             # Fona mūzika
└── output/                # Gatavie video
```

## 🎨 Pielāgošana

Rediģē `config.yaml` failu, lai mainītu:
- Tekstus
- Krāsas
- Timing
- Animāciju stilus

## 📝 Ātrā lietošana

### 1. Instalē visu:
```bash
git clone https://github.com/ruscins/tests1.git
cd tests1
pip install -r requirements.txt
```

### 2. Ģenerē video:
```bash
python generate_ad.py
```

### 3. Video būs pieejams mapē:
```
output/autoskola_ad.mp4
```

## 💡 Video saturs

Video automātiski izveidos 4 scēnas:
1. **Scēna 1** (5 sek) - Lietus efekts + "Ārā līst lietus? 🌧️"
2. **Scēna 2** (5 sek) - "Mēs zinām risinājumu!"
3. **Scēna 3** (7 sek) - "🚗 B kategorija - Tavs ceļš uz brīvību"
4. **Scēna 4** (3 sek) - "📞 Sāc šodien ar autoSkaila"

## 🎬 Piemēri

Vairāk piemēru skatīt failā: [PIEMERI.md](PIEMERI.md)

### Īss 15 sekunžu video:
```bash
python generate_ad.py --duration 15
```

### Instagram Story formāts:
Rediģē `config.yaml`:
```yaml
video:
  width: 1080
  height: 1920
```

## 🆘 Problēmu risināšana

### FFmpeg kļūda
```
ModuleNotFoundError: No module named 'imageio_ffmpeg'
```
**Risinājums:**
```bash
pip install imageio-ffmpeg
```

### Fonts nav atrasts
Pārbaudi, vai `assets/fonts/` mapē ir fonti. Ja nav, skripts izmantos sistēmas defaulto.

## 📞 Kontakti

Repozitorijs: https://github.com/ruscins/tests1

Vairāk piemēru: [PIEMERI.md](PIEMERI.md)

---

**Veidoja:** @ruscins | 2025

**Tehnoloģijas:** Python | MoviePy | FFmpeg | YAML