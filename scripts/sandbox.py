from time import sleep
from pyautogui import press, hotkey, typewrite

def sandbox():
  sleep(2.5)
  for i in range(1000):
    n = i
    typewrite(str(n))
    hotkey('command', 'enter', interval=0.1)
    sleep(.3)
    for i in range(len(str(n))):
      press('backspace')
    i += 1