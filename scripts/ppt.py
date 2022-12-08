import os

def cd_project():
  os.chdir(os.getenv('PPT_PATH'))
  
def run_ppt():
  cd_project()
  os.system('nvm use 16')
  os.system('npm run migrate')
