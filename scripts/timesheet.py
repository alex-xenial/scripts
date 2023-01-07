from time import sleep
from pyautogui import press, hotkey
from pyperclip import copy, paste
from helpers import new_tab, alt_tab, spotlight, click_link, find_link, prompt_yn, close_current_tab, run_javascript
from globals import INTERVAL
import json
import os

def timesheet():
  
  submit_timesheet = prompt_yn(question='Do you want to submit the timesheet after saving?')
  
  hours = {}
  
  # Ask about hours for each day
  weekdays = ['mon', 'tue', 'wed', 'thu', 'fri']
  worked_entire_week = prompt_yn(question='Did you work 40 hours this week?')
  if worked_entire_week:
    hours = {}
    for day in weekdays:
      hours[day] = {
        'start': '9:00AM',
        'end': '5:00PM'
      }
  else:
    for day in weekdays:
      worked_entire_day = prompt_yn(question='Did you work the entire 8 hours on ' + day + '?')
      if not worked_entire_day:
        hours_worked = input('When did you work on ' + day + '? (Use format "9-5", "8:30-6", "12-3", etc). Press enter if you did not work at all.\n')
        if hours_worked == '':
          continue
        hours_worked = [int(hour) for hour in hours_worked.split('-')]
        # Get clock in and out time in format "9:00AM", "5:00PM".
        # Assume any time between 7 and 11:59 is AM, and 12 and 6:59 is PM
        # Support HH:MM format
        time_in = hours_worked[0]
        time_out = hours_worked[1]
        
        hour_in, minute_in = time_in.split(':') if ':' in str(time_in) else (time_in, '00')
        hour_out, minute_out = time_out.split(':') if ':' in str(time_out) else (time_out, '00')
        hour_in, minute_in, hour_out, minute_out = int(hour_in), int(minute_in), int(hour_out), int(minute_out)
        
        if hour_in >= 7 and hour_in <= 11:
          clock_in = str(hour_in).zfill(2) + ':' + str(minute_in).zfill(2) + 'AM'
          
        else:
          clock_in = str(hour_in).zfill(2) + ':' + str(minute_in).zfill(2) + 'PM'
          
        if hour_out >= 7 and hour_out <= 11:
          clock_out = str(hour_out).zfill(2) + ':' + str(minute_out).zfill(2) + 'AM'
        else:
          clock_out = str(hour_out).zfill(2) + ':' + str(minute_out).zfill(2) + 'PM'
        
      else:
        clock_in = '9:00AM'
        clock_out = '5:00PM'
      
      hours[day] = {
        'start': clock_in,
        'end': clock_out
      }
    
  new_tab('kinetix-globalpay', 3)
  click_link('login', wait=2, index=1)
  click_link('add timesheet', 3)
  find_link('select', index=1)
  sleep(1)
  press('tab')
  press('enter')
  
  run_javascript('get-timesheets', wait=3)
  timesheets = json.loads(paste())
  
  if (len(timesheets) == 0):
    alt_tab()
    print('No timesheets found, exiting...')
    return
  if (len(timesheets) > 1):
    alt_tab()
    os.system('Say "More than one timesheet found"')
    print('More than one timesheet found, which one do you want to fill out? Please enter the index number')
    for i in range(len(timesheets)):
      print(str(i) + ': ' + timesheets[i]['start'] + ' - ' + timesheets[i]['end'])
    choice = int(input())
    sleep(.5)
    spotlight('chrome')
  else:
    choice = 0
  
  find_link('select', index=1)
  sleep(1)
  press('tab')
  press('enter')
  for i in range(choice + 1):
    press('down')
    sleep(.1)
  press('tab')
  sleep(.1)
  press('enter')
  
  sleep(2)
  
  run_javascript('fill-timesheet', wait=7, data=hours)
  close_current_tab()
  
  sleep(5)
  
  if (submit_timesheet):
    click_link('submit timesheet', 5)
  
  sleep(5)
  
  close_current_tab()
  