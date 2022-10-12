import sys
import os
from time import sleep
from globals import INTERVAL, WRITE_INTERVAL
from pyautogui import typewrite, press, hotkey
from pyperclip import copy

def prompt_yn(question, default='y'):
  valid = {'y': True, 'n': False}
  if default is None:
    prompt = ' [y/n] '
  elif default == 'y':
    prompt = ' [Y/n] '
  elif default == 'n':
    prompt = ' [y/N] '
  else:
    raise ValueError('Invalid default answer: {}'.format(default))

  while True:
    sys.stdout.write(question + prompt)
    choice = input().lower()
    if default is not None and choice == '':
      return valid[default]
    elif choice in valid:
      return valid[choice]
    else:
      sys.stdout.write('Please respond with \'y\' or \'n\'.\n')
    
def spotlight(query):
  hotkey('command', 'space', interval=INTERVAL)
  sleep(1)
  typewrite(query, interval=WRITE_INTERVAL)
  press('enter')
  sleep(1)

def new_tab(url, wait=2):
  sleep(.5)
  spotlight('chrome')
  hotkey('command', 't', interval=INTERVAL)
  typewrite(url, interval=WRITE_INTERVAL)
  press('enter')
  sleep(wait)

def click_link(text, wait=0, index=0):
  hotkey('command', 'f', interval=INTERVAL)
  typewrite(text, interval=WRITE_INTERVAL)
  for i in range(index):
    press('enter')
  press('escape')
  press('enter')
  sleep(wait)
  
def run_javascript(filename, wait=0):
  path = os.path.join(os.path.dirname(__file__), 'js-snippets', filename + '.js')
  f = open(path, 'r')
  script = f.read()
  f.close()
  
  hotkey('command', 'option', 'j', interval=INTERVAL)
  hotkey('ctrl', '`', interval=INTERVAL)
  sleep(2)
  copy(script)
  hotkey('command', 'v', interval=INTERVAL)
  press('enter')
  sleep(wait)

def close_current_tab():
  hotkey('command', 'w', interval=INTERVAL)