
from screen import start_recording, stop_recording #
from config import readDataConfigs, readWindowsConfigs

# ---- переменные
configPath = 'config.config'
url, timer = readDataConfigs(configPath)
ffmpeg_path, folder_with_lectures = readWindowsConfigs(configPath)

# Убедимся, что каталог существует (создадим, если нет)
folder_with_lectures.mkdir(parents=True, exist_ok=True)

# ---- основная функция
def main():
    #webbrowser.open(url)
    r = start_recording(ffmpeg_path, timer, folder_with_lectures, 'l1.mp4')

if __name__ == "__main__":
    main()