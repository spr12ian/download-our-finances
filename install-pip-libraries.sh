#!/bin/bash

python3 -m venv venv

source venv/bin/activate

echo "Installing the django web framework"
pip install django

echo "Installing the flask web framework"
pip install flask

echo "Installing oauth2client"
pip install oauth2client

echo "Installing google-auth"
pip install google-auth

echo "Installing google-auth-oauthlib"
pip install google-auth-oauthlib

echo "Installing gspread"
pip install gspread

echo "Installing pandas"
pip install pandas

pip freeze >requirements.txt