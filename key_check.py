from google_helper import GoogleHelper
from log_helper import tprint


def main():
    # Define the required scopes
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    spreadsheet = GoogleHelper().get_spreadsheet(scopes)

    tprint(f"Spreadsheet name: {spreadsheet.title}")


if __name__ == "__main__":
    main()
