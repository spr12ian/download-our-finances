import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import sqlite3
import time


class SpreadsheetDatabaseConverter:
    def __init__(self, credentials_path, spreadsheet_url):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """

        # Define the required scopes
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)

        # Open the spreadsheet
        self.spreadsheet = client.open_by_url(spreadsheet_url)

        # Local database connection
        self.db_connection = None
        self.db_path = self.spreadsheet.title.replace(" ", "_") + ".db"

    def list_tables(self):
        self.db_connection = sqlite3.connect(self.db_path)
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        self.close_connection()
        return [table[0] for table in tables]

    def convert_to_spreadsheet(self):
        """
        Convert all SQLite tables to sheets in the Google Spreadsheet
        """

        tables = self.list_tables()
        print(tables)

        for table in tables:
            data = self.fetch_data_from_table(table)
            self.create_and_populate_sheet(data, table, api_credentials)
            time.sleep(1)

        print(f"SQLite database at {self.db_path} converted to spreadsheet")

    def close_connection(self):
        """
        Close database connection
        """
        if self.db_connection:
            self.db_connection.close()

    def fetch_data_from_table(self, table_name):
        # Create or connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)
        cursor = self.db_connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        self.close_connection()
        return data

def authorize_google_sheets(api_credentials):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        api_credentials, scope
    )
    client = gspread.authorize(credentials)
    return client


def create_and_populate_sheet(data, table_name, api_credentials):
    client = authorize_google_sheets(api_credentials)
    spreadsheet = client.create(f"SQLite Database Copy - {table_name}")
    worksheet = spreadsheet.get_worksheet(0)  # Get the first worksheet
    worksheet.update("A1", data)  # Update starting from cell A1


def main():
    # Python Our Finances URL
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1zss8pMXIT3REAbs7-CtlFm7GWSsmzK6Xt7F00hQseDw"

    converter = SpreadsheetDatabaseConverter(
        credentials_path=os.path.expanduser("~/isw-personal-scripts-314a6167bf08.json"),
        spreadsheet_url=spreadsheet_url,
    )

    try:
        # Convert database to spreadsheet
        converter.convert_to_spreadsheet()

    finally:
        # Always close the database connection
        converter.close_connection()


if __name__ == "__main__":
    main()
