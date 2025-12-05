import subprocess, logging
#from config import readDataConfigs, readWindowsConfigs
from pathlib import Path



def start_recording(ffmpeg_path: Path):

    cmd = [
        ffmpeg_path,
        "ffmpeg",
        "-f", "gdigrab",
        "-framerate", "30",
        "-i", "desktop",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "23",
        "lecture.mp4"
    ]
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)

def stop_recording(proc: subprocess.Popen):
    proc.terminate()          # посылает SIGTERM (Windows -> TerminateProcess)
    proc.wait()               # ждём, пока процесс полностью завершится
    print("Запись остановлена")