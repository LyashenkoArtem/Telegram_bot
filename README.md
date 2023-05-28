# Telegram_bot

1. Install Dependencies
Install dependencies via script `scripts/install_packages.<arch>.sh`
2. make Project
```commandline
make
```
3. Create env file with secrets
```commandline
touch secrets.env
```
and fill
```commandline
DABOT_TOKEN=sometoken
```
Them you can run and test
```commandline
 docker run --env-file=secrets.env -it dabot:latest
```
