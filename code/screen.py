import subprocess, uuid
from pathlib import Path
import os



AUDIO_DEVICE = "Line 1 (Virtual Audio Cable)"


def start_recording(ffmpeg_path: Path, timer: int, folder_with_lectures: Path, filename: str):

    out_path = f'{folder_with_lectures}\\{filename}'  # путь из конфига
    outfile = os.path.join(folder_with_lectures, f"lecture_{uuid.uuid4().hex[:8]}.mp4")

    print(f'ffmpeg_path={ffmpeg_path}\nAUDIO_DEVICE={AUDIO_DEVICE}\ntimer={timer}\nfolder_with_lectures={folder_with_lectures}\n')

    cmd = [
        ffmpeg_path,
        "-y",
        "-f", "gdigrab",
        "-framerate", "30",
        "-i", "desktop",
        "-f", "dshow",
        "-i", f"audio={AUDIO_DEVICE}",
        "-t", str(timer),
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-c:a", "aac",
        "-b:a", "128k",
        outfile
    ]
    # Запуск с выводом ошибок, чтобы увидеть причину падения
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = proc.communicate()

    if proc.returncode != 0:
        print("------FFmpeg завершился с ошибкой:")
        print(err.strip())
    else:
        print(f"------Запись завершена, файл сохранён в: {out_path}")

def stop_recording(proc: subprocess.Popen):
    proc.terminate()          # посылает SIGTERM (Windows -> TerminateProcess)
    proc.wait()               # ждём, пока процесс полностью завершится
    print("Запись остановлена")