from time import sleep
from helpers import new_tab, spotlight
from pyautogui import move, click, write, press, hotkey
from globals import INTERVAL

def aws():
  new_tab(url='mfa.')
  sleep(5)
  write('aws')
  press('enter')
  sleep(5)
  click(x=607, y=323)
  sleep(1.5)
  click(x=964, y=495)
  sleep(2)
  click(x=1211, y=547)
  sleep(2)
  click(x=935, y=542)
  for i in range(2):
    hotkey('command', 'w', interval=INTERVAL)
  spotlight('visual studio code')
  hotkey('command', 'p', interval=INTERVAL)
  write('.env')
  press('enter')
  hotkey('command', 'f', interval=INTERVAL)
  write('aws_')
  press('escape')
  hotkey('command', 'left', interval=INTERVAL)
  for i in range(2):
    hotkey('command', 'option', 'down', interval=INTERVAL)
  hotkey('command', 'shift', 'right', interval=INTERVAL)
  hotkey('command', 'v', interval=INTERVAL)
  hotkey('command', 'shift', 'left', interval=INTERVAL)
  press('left')
  hotkey('option', 'delete', interval=INTERVAL)
  press('delete')
  hotkey('command', 's', interval=INTERVAL)
