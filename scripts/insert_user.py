import os
from time import sleep
from pyautogui import click, press, hotkey
from pyperclip import copy
from globals import INTERVAL
from helpers import new_tab, click_link, close_current_tab

first = os.getenv('FIRST_NAME')
last = os.getenv('LAST_NAME')
email = os.getenv('EMAIL')

def insert_user():
  new_tab(url='localhost:8083', wait=10)
  
  # Open xprt databse
  for i in range(7):
    press('tab')
  press('enter')
  sleep(3)
  
  click_link('people', 4, index=1)
  
  # Insert new document
  for i in range(8):
    press('tab')
  press('enter')
  sleep(1)
  hotkey('command', 'a', interval=INTERVAL)
  
  user = """
  {{
    "_id": ObjectID("62dab1fec5123b0009a8d310"),
    "is_active": true,
    "created_at": ISODate("2022-03-25T14:22:31.134Z"),
    "created_by": ObjectID("5c86483fa3b5a00ce28c56dc"),
    "updated_at": ISODate("2022-03-25T14:22:31.626Z"),
    "updated_by": ObjectID("5c86483fa3b5a00ce28c56dc"),
    "name": "{first} {last}",
    "first_name": "{first}",
    "last_name": "{last}",
    "email": "{email}",
    "roles": [
      {{
        "role_name": "admin",
        "role_id": ObjectID("5881ffa30d242c000609858d")
      }}
    ],
    "preferred_language": "en-US",
    "cognito_uuid": "unknown",
    "sign_up_date": ISODate("2022-03-26T14:22:31.000Z"),
    "last_login": ISODate("2022-07-22T14:30:28.234Z"),
    "external_idp": null,
    "email_bidx": "maVa+mNoefnR6TqR45gBB4o2t9aE2cguTlrq79KQ1kM=",
    "name_bidx": "BID54HZoCgLsQ4BvPEKMe4oCsx48P0aFJo8/Beyu/5A=",
    "first_name_bidx": "svSI8HecvHidCPMHGgQqtPxHIZqaAGAIYYqCBhFVfpY=",
    "last_name_bidx": "WSnfIJoRcGvoQ62qcp4edo0ggIpEBsNs5Mc4E62Hv4U=",
    "version": 1
  }}
  """.format(first=first, last=last, email=email)
  
  copy(user)
  hotkey('command', 'v', interval=INTERVAL)
  click(x=1206, y=628)
  sleep(1)
  close_current_tab()

  # Open portal
  new_tab(url='localhost:8080')
  sleep(2)
  press('enter')