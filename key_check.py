import os
from google.oauth2.service_account import Credentials
import gspread

# Path to the JSON key file
SERVICE_ACCOUNT_FILE = os.path.expanduser("~/isw-personal-scripts-314a6167bf08.json")

# Define the required scopes
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

# Authenticate using the service account
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Authorize and connect to Google Sheets
client = gspread.authorize(credentials)

# Our Finances URL
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Sj13auBheoZalYbs1KUe1ESf0Gq-3gD2DfjdFmVEPTc"

# Access a Google Sheet
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.sheet1

# Fetch data
data = worksheet.get_all_records()
print(data)
