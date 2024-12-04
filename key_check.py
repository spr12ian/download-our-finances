import configparser
from google.oauth2.service_account import Credentials
import google_helpers
import gspread
import log_it


def main():
    log_it.print_time()
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Google Cloud Service credentials
    credentials_file_name = config["Google"]["credentials_file_name"]

    spreadsheet_key = config["Google"]["source_spreadsheet_key"]

    credentials_path = google_helpers.get_credentials_path(credentials_file_name)

    # Define the required scopes
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)

    # Authorize and connect to Google Sheets
    client = gspread.authorize(credentials)

    # Access a Google Sheet
    spreadsheet = client.open_by_key(spreadsheet_key)

    log_it.print_time()
    print(spreadsheet.title)


if __name__ == "__main__":
    main()
