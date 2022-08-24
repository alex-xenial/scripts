import os
from dotenv import load_dotenv
from argparse_prompt import PromptParser

load_dotenv()

from scripts.aws import aws
from scripts.insert_user import insert_user
from scripts.timesheet import timesheet
from scripts.mouse_pos import mouse_pos

commands = {
  'aws': aws,
  'insert_user': insert_user,
  'timesheet': timesheet,
  'mouse_pos': mouse_pos
}

def main():
  parser = PromptParser()
  scripts_list = ', '.join(list(commands.keys()))
  parser.add_argument('-n', '--name', help='name of script to run [' + scripts_list + ']')
  args = parser.parse_args()
  if args.name:
    if args.name in commands:
      commands[args.name]()
      os.system('say "{name} script completed"'.format(name=args.name))
    else:
      print('Invalid script name')
  else:
    print('No script name specified')

main()