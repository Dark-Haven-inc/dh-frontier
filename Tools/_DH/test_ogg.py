import os
import sys
import soundfile as sf

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Resources"))

broken_files = []

for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.lower().endswith(".ogg"):
            path = os.path.join(dirpath, f)
            try:
                with sf.SoundFile(path) as audio:
                    audio.frames
            except Exception as e:
                broken_files.append((path, str(e)))

if broken_files:
    print("⚠️ Найдены битые OGG файлы:")
    for path, err in broken_files:
        print(f"{path} -> {err}")
    sys.exit(1)
else:
    print("✅ Все OGG файлы валидные")
