from time import sleep
from pyautogui import press, hotkey
from pyperclip import copy
from helpers import new_tab, click_link, prompt_yn, close_current_tab, run_javascript
from globals import INTERVAL

def timesheet():
  
  submit_timesheet = prompt_yn(question='Do you want to submit the timesheet after saving?')
  
  new_tab('kinetix-globalpay', 10)
  click_link('add timesheet', 3)
  click_link('select', 1, index=1)
  
  press('tab')
  press('space')
  press('enter')
  press('tab')
  press('enter')
  
  sleep(5)
  
  
  js = """
  const days = ['mon','tue','wed','thu','fri']
  days.forEach(day => {
    document.querySelector(`#start_time_${day}`).value = '09:00'
    document.querySelector(`#end_time_${day}`).value = '17:00'
  })
  document.querySelector('input[name=saveSheet]').click()
  """
  
  # Paste javascript into the console
  run_javascript(js)
  close_current_tab()
  
  sleep(5)
  
  if (submit_timesheet):
    click_link('save timesheet', 5)
  
  close_current_tab()
  