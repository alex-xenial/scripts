from globals import INTERVAL
import os
import pyotp
from time import sleep
from helpers import new_tab, spotlight
from pyautogui import move, click, write, press, hotkey
from pyperclip import copy

totp = pyotp.TOTP(os.getenv('TOTP_SECRET'))
print(totp.now())

def aws():

  # Open SSO  
  new_tab(url='mfa.', wait=3)
  
  # Login
  press('tab')
  press('enter')
  sleep(7)
  
  # Open AWS
  write('aws')
  press('enter')
  sleep(5)
  
  copy(totp.now())
  hotkey('ctrl', 'v', interval=INTERVAL)
  return
  
  # Copy env variables
  # TODO: Do this without using the mouse
  click(x=607, y=323)
  sleep(1.5)
  click(x=964, y=495)
  sleep(2)
  click(x=1211, y=547)
  sleep(2)
  click(x=935, y=542)
  
  # Close tab
  for i in range(2):
    hotkey('command', 'w', interval=INTERVAL)
    
  # Open .env file
  spotlight('visual studio code')
  hotkey('command', 'p', interval=INTERVAL)
  write('.env')
  press('enter')
  
  # Place cursor at beginning of file
  hotkey('command', 'a', interval=INTERVAL)
  press('left')
  
  # Find existing env variables
  hotkey('command', 'f', interval=INTERVAL)
  write('aws_')
  press('escape')
  hotkey('command', 'left', interval=INTERVAL)
  
  # Place multiple cursors and paste
  for i in range(2):
    hotkey('command', 'option', 'down', interval=INTERVAL)
  hotkey('command', 'shift', 'right', interval=INTERVAL)
  hotkey('command', 'v', interval=INTERVAL)
  hotkey('command', 'shift', 'left', interval=INTERVAL)
  press('left')
  hotkey('option', 'delete', interval=INTERVAL)
  press('delete')
  
  # Save file and close
  hotkey('command', 's', interval=INTERVAL)
  hotkey('command', 'w', interval=INTERVAL)
