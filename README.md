# fvso
A fact-checking platform using NLP

## Installation Instructions:

### React
Install all dependencies: `yarn` or `yarn install`

### Flask
Create a config.cfg file at the root level (will need PORT, DEBUG, and SECRET_KEY values at minimum) and then run the below commands.

pip3 install virtualenv (skip if already installed)
virtualenv venv 
. venv/bin/activate (Mac) | . venv/scripts/activate (Windows)
pip3 install -r requirements.txt
python3 run.py

## Run Instructions:
### React
Start app: `yarn start`

### Flask

. venv/bin/activate (Mac) | . venv/scripts/activate (Windows)
python3 run.py
