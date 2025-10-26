# 📚 Lietošanas Piemēri

## Pamata lietošana

### 1. Vienkāršākais variants
```bash
python generate_ad.py
```
Izveido 20 sekunžu video ar default iestatījumiem.

### 2. Īss 15 sekunžu video
```bash
python generate_ad.py --duration 15
```

### 3. Ar citu stilu
```bash
python generate_ad.py --style minimal
```

## Pielāgota konfigurācija

### 4. Mainīt tekstus
Rediģē `config.yaml`:
```yaml
scenes:
  scene1:
    text: "Tavs pielāgotais teksts"
```

### 5. Mainīt krāsas
```yaml
scenes:
  scene1:
    background_color: [100, 150, 200]  # RGB
    text_color: [255, 255, 0]  # Dzeltens
```

### 6. Pievienot fona mūziku
1. Ieliec MP3 failu mapē `assets/audio/background.mp3`
2. Pārliecinies, ka `config.yaml` ir:
```yaml
audio:
  background_music: "assets/audio/background.mp3"
  volume: 0.3
```

## Dažādi formāti

### 7. Instagram Story (1080x1920)
Rediģē `config.yaml`:
```yaml
video:
  width: 1080
  height: 1920
```

### 8. TikTok formāts (1080x1920)
```yaml
video:
  width: 1080
  height: 1920
  duration: 15
```

### 9. YouTube Shorts (1080x1920)
```yaml
video:
  width: 1080
  height: 1920
  duration: 60
```

## Progresīvi piemēri

### 10. Batch ģenerēšana (vairāki video)
```bash
# Izveido skriptu batch_generate.sh
for i in {1..5}
do
   python generate_ad.py --output "output/ad_$i.mp4" --style modern
done
```

### 11. Cron job (katru dienu jauns video)
```bash
# Pievieno pie crontab
0 9 * * * cd /path/to/tests1 && python generate_ad.py --output "output/daily_$(date +\%Y\%m\%d).mp4"
```

### 12. Python skripts vairākiem variantiem
```python
styles = ['modern', 'classic', 'minimal']
for style in styles:
    os.system(f'python generate_ad.py --style {style} --output output/ad_{style}.mp4')
```

## Troubleshooting

### Ja video ir par lielu
Samazini kvalitāti `generate_ad.py`:
```python
final_video.write_videofile(
    output_file,
    preset='ultrafast',  # Ātrāk, bet lielāks fails
    # VAI
    preset='veryslow',   # Lēnāk, bet mazāks fails
)
```

### Ja rendering ir par lēnu
```yaml
# Samazini izšķirtspēju testēšanai
video:
  width: 1280
  height: 720
```

## Eksportēšana

### 13. Optimizēts Facebook
```bash
python generate_ad.py --output output/facebook_ad.mp4
# Tad saspiež:
ffmpeg -i output/facebook_ad.mp4 -c:v libx264 -preset slow -crf 22 -c:a aac -b:a 128k output/facebook_optimized.mp4
```

### 14. GIF izveidošana
```bash
ffmpeg -i output/autoskola_ad.mp4 -vf "fps=10,scale=640:-1:flags=lanczos" output/preview.gif
```

---

💡 **Padomi:**
- Vienmēr testē ar īsāku duration pirms full render
- Saglabā vairākas config.yaml versijas (config_variant1.yaml)
- Izmanto version control (git) konfigurāciju izmaiņām

🆘 **Palīdzība:** https://github.com/ruscins/tests1/issues