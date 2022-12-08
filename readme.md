# Xenial Portal scripts

## Table of contents
- [Xenial Portal scripts](#xenial-portal-scripts)
  - [Table of contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Environment variables](#environment-variables)
      - [Retrieving TOTP secret key](#retrieving-totp-secret-key)
      - [Retrieving BIDX hashes](#retrieving-bidx-hashes)
  - [Usage](#usage)
    - [Scripts](#scripts)

## Requirements
- MacOS with [Spotlight](https://support.apple.com/guide/mac-help/search-with-spotlight-mchlp1008/mac) enabled
- [Cloned repository for Portal (pos-onboarding)](https://bit.xenial.com/projects/HC/repos/pos-onboarding/browse)
- [Cloned repository for Permissions Provisioning Tool (xenial-permission-provisioning-tool)](https://bit.xenial.com/projects/HC/repos/xenial-permission-provisioning-tool/browse)
- [Python 3](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en)
- [NVM](https://github.com/nvm-sh/nvm)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

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
echo "PORTAL_PATH=/path/to/project" >> .env
echo "EMAIL=myemail@example.com" >> .env
echo "FIRST_NAME=Bob" >> .env
...
(See table below for all required variables)
```

### Environment variables
| Name              | Description                                                         | Required |
|-------------------|---------------------------------------------------------------------|----------|
| `PORTAL_PATH`     | Absolute path to your xenial-onboarding project                     | Yes      |
| `PPT_PATH`        | Absolute path to your xenial permissions provisioning tool project  | Yes      |
| `FIRST_NAME`      | Your first name                                                     | Yes      |
| `LAST_NAME`       | Your last name                                                      | Yes      |
| `EMAIL`           | Your email address                                                  | Yes      |
| `PORTAL_EMAIL`    | Email address of the portal account (not needed if same as `EMAIL`) | No       |
| `MFA_TOTP_SECRET` | One-time-password secret key for Global Payments single sign on     | Yes      |
| `EMAIL_BIDX`      | Your Xenial `email_bidx` hash                                       | Yes      |
| `NAME_BIDX`       | Your Xenial `name_bidx` hash                                        | Yes      |
| `FIRST_NAME_BIDX` | Your Xenial `first_name_bidx` hash                                  | Yes      |
| `LAST_NAME_BIDX`  | Your Xenial `last_name_bidx` hash                                   | Yes      |

#### Retrieving TOTP secret key
1. Log in to the [Global Payments MFA portal](https://mfa.sso.globalpay.com/)
2. In the upper right click your user name
3. Navigate to `Settings`
4. Click `Edit Profile`
5. Enter your 2FA code from your authenticator app
6. In the `Extra Verification` section, remove your `Google Authenticator` configuration
7. Reconfigure Google Authenticator by clicking `Set up`
8. Step through the setup wizard until you see the QR code
9. Click `Can't scan` under the QR code
10. Copy the key that is displayed into your .env file as `MFA_TOTP_SECRET` 
11. Click `Scan barcode`
12. In your authenticator app, delete your old MFA account, then add the new one by scanning the QR code

#### Retrieving BIDX hashes
`bidx` hash values can be found by logging in to portal on an AWS-hosted upper stack and inspecting the "/v1/me" endpoint upon logging in. Ex:

```
Request URL: https://dev-xprtbackend.xenial.com/v1/me
Request Method: GET
Status Code: 200 
Remote Address: 23.20.157.89:443
Referrer Policy: strict-origin-when-cross-origin
```
```json
{
    "is_active": true,
    "created_at": "2022-07-20T15:14:36.738Z",
    ...
    "email_bidx": "************************************",
    "name_bidx": "************************************",
    "first_name_bidx": "************************************",
    "last_name_bidx": "************************************",
    ...
}
```



## Usage

1. Ensure the python virtual environment is activated
```bash
source env/bin/activate
```

2. With the python environment activated, run your script:
```bash
% python3 main.py               
name: name of script to run [dev, aws, docker, docker-stop, docker-prune, docker-reseed, insert_user, timesheet]
> dev
```
or:
```bash
% python3 main.py -n dev
```

### Scripts
| Name              | Description                                                                              |
|-------------------|------------------------------------------------------------------------------------------|
| `dev`             | Start development environment (runs `aws`, `docker`, `insert-user`)                      |
| `aws`             | Copy AWS access credentials to your `.env` file                                          |
| `docker`          | Start docker containers                                                                  |
| `docker-stop`     | Stop docker containers                                                                   |
| `docker-prune`    | Clean docker storage                                                                     |
| `docker-reseed`   | Re-seed the database                                                                     |
| `ppt`             | Run the permissions provisioning tool migration script                                   |
| `insert-user`     | Insert your user account into the database                                               |
| `timesheet`       | Fill 40 hours for the week in Kinetix time sheets                                        |
| `sandbox`         | Executes any code you write in `sandbox.py`                                              |
| `totp`            | Retrieves your current TOTP code for Global Payments mfa and copies it to your clipboard |