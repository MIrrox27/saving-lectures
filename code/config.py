from configparser import ConfigParser
from pathlib import Path



def readDataConfigs(path: str):
    configs = ConfigParser()
    configs.read(f'{path}', encoding='utf-8')


    url = configs.get('data', 'url')
    timer = 60 * (configs.getint('data', 'timer')) # получаем в минутах

    print(f"{url}\n{timer} sec")
    return url, timer


def readWindowsConfigs(path: str):
    configs = ConfigParser()
    configs.read(f'{path}', encoding='utf-8')

    ffmpeg_exe = Path(configs.get('windows', 'ffmpeg_exe'))
    folder_with_lectures = Path(configs.get('windows', 'folder_with_lectures'))

    print(f"{str(ffmpeg_exe)}\n{str(folder_with_lectures)}")
    return ffmpeg_exe, folder_with_lectures



if __name__ == "__main__":
    url,  timer = readDataConfigs('config.config')
    print(url)
    print(timer)