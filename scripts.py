from pyautogui import move, click, write, press, hotkey
from time import sleep
from pyperclip import copy
import argparse

INTERVAL = 0.1

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--name', help='name of script to run')
  args = parser.parse_args()
  if args.name:
    if args.name == 'aws_credentials':
      aws_credentials()
    elif args.name == 'insert_user':
      insert_user()
    elif args.name == 'mouse_pos':
      mouse_pos()
    else:
      print('Invalid script name')
  else:
    print('No script name specified')

def spotlight(query):
  hotkey('command', 'space', interval=INTERVAL)
  write(query)
  press('enter')

def new_tab(url):
  hotkey('command', 't', interval=INTERVAL)
  write(url)
  press('enter')
  sleep(2)

def aws_credentials():
  spotlight('chrome')
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

def insert_user():
  spotlight('chrome')
  new_tab(url='localhost:8083')
  sleep(4)
  
  # Open xprt databse
  for i in range(7):
    press('tab')
  press('enter')
  sleep(3)
  
  # Open people collection
  hotkey('command', 'f', interval=INTERVAL)
  write('people')
  press('enter')
  press('escape')
  press('enter')
  sleep(2)
  
  # Insert new document
  for i in range(8):
    press('tab')
  press('enter')
  sleep(1)
  hotkey('command', 'a', interval=INTERVAL)
  user = '{"_id": ObjectID("62dab1fec5123b0009a8d310"),"is_active": true,"created_at": ISODate("2022-03-25T14:22:31.134Z"),"created_by": ObjectID("5c86483fa3b5a00ce28c56dc"),"updated_at": ISODate("2022-03-25T14:22:31.626Z"),"updated_by": ObjectID("5c86483fa3b5a00ce28c56dc"),"name": "Alex Wohlbruck","first_name": "Alex","last_name": "Wohlbruck","email": "alex.wohlbruck+dev@xenial.com","roles": [{"role_name": "admin","role_id": ObjectID("5881ffa30d242c000609858d")}],"preferred_language": "en-US","cognito_uuid": "unknown","sign_up_date": ISODate("2022-03-26T14:22:31.000Z"),"last_login": ISODate("2022-07-22T14:30:28.234Z"),"external_idp": null,"email_bidx": "maVa+mNoefnR6TqR45gBB4o2t9aE2cguTlrq79KQ1kM=","name_bidx": "BID54HZoCgLsQ4BvPEKMe4oCsx48P0aFJo8/Beyu/5A=","first_name_bidx": "svSI8HecvHidCPMHGgQqtPxHIZqaAGAIYYqCBhFVfpY=","last_name_bidx": "WSnfIJoRcGvoQ62qcp4edo0ggIpEBsNs5Mc4E62Hv4U=","version": 1}'
  copy(user)
  hotkey('command', 'v', interval=INTERVAL)
  click(x=1206, y=628)
  sleep(1)
  hotkey('command', 'w', interval=INTERVAL)

  # Open portal
  new_tab(url='localhost:8080')
  sleep(2)
  press('enter')

def mouse_pos():
  from pyautogui import position
  while True:
    print(position())
    sleep(.05)

main()