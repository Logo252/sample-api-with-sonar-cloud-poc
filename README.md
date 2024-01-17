## Setup up project

### Virtual environment
- Create venv: `python3 -m venv ./venv`
- Activate venv: `source venv/bin/activate`
- Deactivate venv: `deactivate`

### Add new dependencies to requirements.txt
- Run command: `pipreqs --force` (use --force to overwrite file)

### Install dependencies
- Run command: `pip install -r requirements.txt`

## Run project
- Run command: `python main.py`
- Or run command: `gunicorn -w 1 --bind "0.0.0.0:6000" --log-level debug main:app`

## REST API examples
- Call endpoint to do...: `curl -X GET http://localhost:5000/action?param1=value1&param2=value2`
- etc.

### API docs

- ??


## Test

## Deployment

### TO DO
- 