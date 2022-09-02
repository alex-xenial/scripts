from globals import INTERVAL
import os
import pyotp
from time import sleep
import dotenv
from helpers import new_tab, spotlight, close_current_tab, prompt_yn, run_javascript
from pyautogui import move, click, write, press, hotkey
from pyperclip import copy, paste
from environs import Env

AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
AWS_SESSION_TOKEN = 'AWS_SESSION_TOKEN'

totp = pyotp.TOTP(os.getenv('MFA_TOTP_SECRET'))
email = os.getenv('EMAIL')

def aws():
  insert_environment_vars(get_aws_creds())

def copy_totp():
  copy(totp.now())
  print('TOTP code copied to clipboard')

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
  sleep(7)
  
  if (will_ask_otp):
    copy_totp()
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
  # Example creds:
  '''
  export AWS_ACCESS_KEY_ID="xxxxxxxx"
  export AWS_SECRET_ACCESS_KEY="xxxxxxxx"
  export AWS_SESSION_TOKEN="xxxxxxxx"
  '''
  # Format into dict
  creds = creds.split('\n')
  
  return {
    AWS_ACCESS_KEY_ID: creds[0].split('=')[1].replace('"', ''),
    AWS_SECRET_ACCESS_KEY: creds[1].split('=')[1].replace('"', ''),
    AWS_SESSION_TOKEN: creds[2].split('=')[1].replace('"', '')
  }

def insert_environment_vars(creds):
  path = os.path.join(os.getenv('PROJECT_PATH'), '.env')
  dotenv.set_key(path, AWS_ACCESS_KEY_ID, creds[AWS_ACCESS_KEY_ID])
  dotenv.set_key(path, AWS_SECRET_ACCESS_KEY, creds[AWS_SECRET_ACCESS_KEY])
  dotenv.set_key(path, AWS_SESSION_TOKEN, creds[AWS_SESSION_TOKEN])