from argparse_prompt import PromptParser
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
  parser.add_argument('-n', '--name', help='name of script to run')
  args = parser.parse_args()
  if args.name:
    if args.name in commands:
      commands[args.name]()
    else:
      print('Invalid script name')
  else:
    print('No script name specified')

main()