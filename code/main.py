import webbrowser, time
from screen import start_recording, stop_recording #

#webbrowser.open("https://telemost.yandex.ru/j/82808439554691")

r = start_recording()
time.sleep(5)
stop_recording(r)