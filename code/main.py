import webbrowser, time
from screen import start_recording, stop_recording #
from config import readDataConfigs, readWindowsConfigs

# ---- переменные
configPath = 'config.config'
url, timer = readDataConfigs(configPath)
ffmpeg_path, folder_with_lectures = readWindowsConfigs(configPath)

# ---- основная функция
def main():
    webbrowser.open(url)


#r = start_recording()
#time.sleep(5)
#stop_recording(r)


if __name__ == "__main__":
    main()