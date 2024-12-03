import configparser
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import sqlite3
import time
import google_helpers


class SpreadsheetDatabaseConverter:
    def __init__(self, credentials_path, spreadsheet_key, database_name):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """
        # Setup Google Sheets authentication
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        # Define the required scopes
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)

        # Open the spreadsheet
        self.spreadsheet = client.open_by_key(spreadsheet_key)

        # Local database connection
        self.db_connection = None
        self.db_path = database_name + ".db"

    def convert_to_sqlite(self):
        """
        Convert all sheets in the Google Spreadsheet to SQLite tables
        """
        # Create or connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            # Get worksheet data as a DataFrame
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)

            # Write DataFrame to SQLite table (sheet name becomes table name)
            table_name = worksheet.title.replace(" ", "_")
            print(table_name)
            df.to_sql(table_name, self.db_connection, if_exists="replace", index=False)

            time.sleep(1)

        print(f"Spreadsheet converted to SQLite database at {self.db_path}")

    def close_connection(self):
        """
        Close database connection
        """
        if self.db_connection:
            self.db_connection.close()


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Google Cloud Service credentials
    credentials_file_name = config["Google"]["credentials_file_name"]

    spreadsheet_key = config["Google"]["source_spreadsheet_key"]

    database_name = config["SQLite"]["database_name"]
    credentials_path = google_helpers.get_credentials_path(credentials_file_name)

    converter = SpreadsheetDatabaseConverter(
        credentials_path, spreadsheet_key, database_name
    )

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    # Always close the database connection
    converter.close_connection()


if __name__ == "__main__":
    main()
