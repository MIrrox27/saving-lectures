import subprocess, logging

def start_recording():
    ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
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