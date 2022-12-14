import os
from time import sleep
from pyautogui import click, press, hotkey
from pyperclip import copy
from globals import INTERVAL
from helpers import new_tab, click_link, close_current_tab

first = os.getenv('FIRST_NAME')
last = os.getenv('LAST_NAME')
email = os.getenv('PORTAL_EMAIL') or os.getenv('EMAIL')
email_bidx = os.getenv('EMAIL_BIDX')
name_bidx = os.getenv('NAME_BIDX')
first_name_bidx = os.getenv('FIRST_NAME_BIDX')
last_name_bidx = os.getenv('LAST_NAME_BIDX')

def insert_user():
  new_tab(url='localhost:8083/db/xprtdb/people', wait=8)
  click_link('new document', 1)
  
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
    "cognito_uuid": "6c1db0d0-2436-4586-9fcc-eb0a9d7fb040",
    "sign_up_date": ISODate("2022-03-26T14:22:31.000Z"),
    "last_login": ISODate("2022-07-22T14:30:28.234Z"),
    "external_idp": null,
    "email_bidx": "{email_bidx}",
    "name_bidx": "{name_bidx}",
    "first_name_bidx": "{first_name_bidx}",
    "last_name_bidx": "{last_name_bidx}",
    "version": 1,
    "namespace": "xprt"
  }}
  """.format(
    first=first,
    last=last,
    email=email,
    email_bidx=email_bidx,
    name_bidx=name_bidx,
    first_name_bidx=first_name_bidx,
    last_name_bidx=last_name_bidx
  )
  
  copy(user)
  hotkey('command', 'a', interval=INTERVAL)
  hotkey('command', 'v', interval=INTERVAL)
  click_link('save', 1)
  close_current_tab()

  # Open portal
  new_tab(url='localhost:8080')
  sleep(2)
  press('enter')