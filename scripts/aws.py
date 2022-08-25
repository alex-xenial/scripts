from globals import INTERVAL
import os
import pyotp
from time import sleep
from helpers import new_tab, spotlight, close_current_tab, prompt_yn, run_javascript
from pyautogui import move, click, write, press, hotkey
from pyperclip import copy, paste
from environs import Env

totp = pyotp.TOTP(os.getenv('MFA_TOTP_SECRET'))
email = os.getenv('EMAIL')

def aws():
  creds = get_aws_creds()
  functions = {
    'vscode': insert_env_vscode
  }
  functions[os.getenv('CODE_EDITOR')](creds)

def get_aws_creds():
  
  will_ask_otp = not prompt_yn(question='Have you entered your 2FA code in the last 24 hours?', default='n')

  # Open SSO  
  new_tab(url='mfa.', wait=3)
  
  # Login
  hotkey('command', 'a', interval=INTERVAL)
  write(email)
  press('space')
  press('tab')
  press('enter')
  sleep(7)
  
  # Open AWS
  write('aws')
  press('enter')
  sleep(5)
  
  if (will_ask_otp):
    copy(totp.now())
    hotkey('command', 'v', interval=INTERVAL)
    press('tab')
    press('space')
    press('tab')
    press('enter')
    sleep(5)
  
  run_javascript('copy-aws-credentials', wait=7)
  
  # Close tab
  for i in range(2):
    close_current_tab()
    
  creds = paste()
  return creds
  
def insert_env_vscode(creds):
  copy(creds)
    
  # Open .env file
  spotlight('visual studio code')
  hotkey('command', 'p', interval=INTERVAL)
  write('pos-onboarding/.env', interval=INTERVAL/2)
  sleep(1)
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
  close_current_tab()

