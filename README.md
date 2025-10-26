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

Veidoja: @ruscins | 2025