from time import sleep
import sys
from globals import INTERVAL
from pyautogui import write, press, hotkey

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
  write(query)
  press('enter')

def new_tab(url, wait=2):
  spotlight('chrome')
  hotkey('command', 't', interval=INTERVAL)
  write(url)
  press('enter')
  sleep(wait)

def click_link(text, wait=0, index=0):
  hotkey('command', 'f', interval=INTERVAL)
  write(text)
  for i in range(index):
    press('enter')
  press('escape')
  press('enter')
  sleep(wait)