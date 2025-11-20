# Dilly Daily backend server

## Server deployed adress :

https://fastapi-example-da0l.onrender.com/

## Run server locally

((\*) = run only the first time)

- **[run all following commands in a terminal open in dilly_daily_server folder]**
- (on Linux : ) source .venv/bin/activate
- (on Windows PowerShell) .venv\Scripts\Activate.ps1
- (on Windows Bash) source .venv/Scripts/activate
- (\*) python -m pip install --upgrade pip
- (\*) echo "\*" > .venv/.gitignore
- (\*) pip install "fastapi[standard]"
- (\*) pip install -r requirements.txt
- fastapi run main.py

The server is now accessible at http://0.0.0.0:8000
