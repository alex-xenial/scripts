# Xenial Portal scripts

## Table of contents
- [Xenial Portal scripts](#xenial-portal-scripts)
  - [Table of contents](#table-of-contents)
  - [Setup](#setup)
    - [Environment variables](#environment-variables)
  - [Usage](#usage)
    - [Scripts](#scripts)

## Setup

1. Create virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
```bash
touch .env
echo "PROJECT_PATH=/path/to/project" >> .env
echo "CODE_EDITOR=vscode" >> .env
echo "EMAIL=myemail@example.com" >> .env
echo "FIRST_NAME=Bob" >> .env
echo "LAST_NAME=Smith" >> .env
echo "MFA_TOTP_SECRET=XXXXXXXXXX" >> .env
```

### Environment variables
| Name            | Description                                                     | Possible values |
|-----------------|-----------------------------------------------------------------|-----------------|
| PROJECT_PATH    | Absolute path to your xenial-onboarding project                 |                 |
| CODE_EDITOR     | Code editor to use for editing files                            | vscode          |
| FIRST_NAME      | Your first name                                                 |                 |
| LAST_NAME       | Your last name                                                  |                 |
| EMAIL           | Your email address                                              |                 |
| PORTAL_EMAIL ?  | Email address of the portal account                             |                 |
| MFA_TOTP_SECRET | One-time-password secret key for Global Payments single sign on |                 |

## Usage

1. With the python environment activated, run the following script:
```bash
% python3 main.py               
name: name of script to run [start_dev, aws, docker, docker-stop, docker-prune, docker-reseed, insert_user, timesheet]
> start_dev
```
or:
```bash
% python3 main.py -n start_dev
```

### Scripts
| Name              | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| `start_dev`       | Start development environment (runs `aws`, `docker`, `insert_user`) |
| `aws`             | Copy AWS access credentials to your `.env` file                 |
| `docker`          | Start docker containers                                       |
| `docker-stop`     | Stop docker containers                                        |
| `docker-prune`    | Clean docker storage                                          |
| `docker-reseed`   | Re-seed the databse                                           |
| `insert_user`     | Insert your user account into the database                    |
| `timesheet`       | Fill 80 hours for the week in Kinetix time sheets             |