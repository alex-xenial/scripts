import os
import subprocess
from time import sleep
import json
from helpers import spotlight

def cd_project():
  os.chdir(os.getenv('PROJECT_PATH'))

def start_docker():
  ensure_docker_running()
  cd_project()
  create_container('dev')
  # TODO: Start thread and poll these statuses while docker-compose up is running
  restart_seed()
  check_express()
  check_backend()
  
def ensure_docker_running():
  docker_process = subprocess.Popen('docker ps', shell=True, stdout=subprocess.PIPE)
  docker_output = docker_process.stdout.read()
  if (docker_output == b''):
    spotlight('docker')
    sleep(20)
  
def stop_docker():
  cd_project()
  os.system('docker-compose down')

def prune_docker():
  cd_project()
  os.system('docker system prune --all --force')

def create_container(name):
  os.system('docker-compose up --build -d {name}'.format(name=name))

def start_container(name):
  os.system('docker start {name}'.format(name=name))
  print('Started {name}'.format(name=name))

def restart_container(name):
  os.system('docker restart {name}'.format(name=name))
  print('Restarted {name}'.format(name=name))
  
def check_container(name):
  try:
    log = subprocess.check_output('docker container inspect {name}'.format(name=name), shell=True)
    data = json.loads(log)
    process = data[0]
    
    state = process['State']
    status = state['Status']
    running = state['Running']
    paused = state['Paused']
    restarting = state['Restarting']
    dead = state['Dead']
    
    return status, (running, paused, restarting, dead)
  except Exception as e:
    return False, (False, False, False, False)
  
def restart_seed():
  restart_container('mongodb-seed')

def check_express():
    # Check seed container, if bad then restart it
  status, states = check_container('mongo-express')
  if (status == 'exited'):
    start_container('mongo-express')

def check_backend():
  status, (running, paused, restarting, dead) = check_container('xprt-backend-dev')
  
  if (not status):
    create_container('xprt-backend-dev')
  elif (not running):
    restart_container('xprt-backend-dev')