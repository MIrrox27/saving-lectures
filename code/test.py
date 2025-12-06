from configparser import ConfigParser
from pathlib import Path
import os

config = ConfigParser()
config.read('config.config', encoding='utf-8')

folder_with_lectures = Path(config.get('windows', 'folder_with_lectures'))
print(folder_with_lectures)
