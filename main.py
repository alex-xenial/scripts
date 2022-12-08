import os
from dotenv import load_dotenv
from argparse_prompt import PromptParser

load_dotenv()

from scripts.aws import aws, copy_totp
from scripts.insert_user import insert_user
from scripts.timesheet import timesheet
from scripts.ppt import run_ppt
from scripts.docker import start_docker, stop_docker, prune_docker, restart_seed
from scripts.sandbox import sandbox

def start_dev_env():
  stop_docker()
  aws()
  start_docker()
  run_ppt()
  insert_user()

commands = {
  'dev': start_dev_env,
  'aws': aws,
  'totp': copy_totp,
  'docker': start_docker,
  'docker-stop': stop_docker,
  'docker-prune': prune_docker,
  'docker-reseed': restart_seed,
  'ppt': run_ppt,
  'insert-user': insert_user,
  'timesheet': timesheet,
  'sandbox': sandbox
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