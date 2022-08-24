from time import sleep
from pyautogui import position

def mouse_pos():
  while True:
    print(position())
    sleep(.05)