import configparser
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import sqlite3
import time
import google_helper


class DatabaseSpreadsheetConverter:
    def __init__(self, credentials_path, spreadsheet_key, database_name):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet URL

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_url (str): URL of the Google Spreadsheet
        """

        client = self.get_authorized_client(credentials_path)

        # Open the spreadsheet
        self.spreadsheet = client.open_by_key(spreadsheet_key)
        print(self.spreadsheet.title)

        # Local database connection
        self.db_connection = None
        self.db_path = database_name + ".db"

    def get_authorized_client(self, credentials_path):
        """
        Get client using credentials

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
        """

        # Define the required scopes
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.readonly",
        ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)

        return client

    def list_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.open_db_connection()
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()
        self.close_db_connection()
        return [table[0] for table in tables]

    def convert_to_spreadsheet(self):
        """
        Convert all SQLite tables to sheets in the Google Spreadsheet
        """

        tables = self.list_tables()

        for table in tables:
            print(table)
            dataframe = self.get_table_as_dataframe(table)
            self.upload_to_google_sheet(table, dataframe)
            time.sleep(1)

        print(f"SQLite database at {self.db_path} converted to spreadsheet")

    def close_db_connection(self):
        """
        Close database connection
        """
        if self.db_connection:
            self.db_connection.close()

    def get_table_as_dataframe(self, table_name):
        self.open_db_connection()
        query = f'SELECT * FROM "{table_name}"'
        dataframe = pd.read_sql_query(query, self.db_connection)
        self.close_db_connection()
        return dataframe

    def open_db_connection(self):
        # Connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)

    def upload_to_google_sheet(self, table_name, dataframe):
        if table_name[0] != "_":
            sheet_name = table_name.replace("_", " ")
        else:
            sheet_name = table_name

        print(f"Trying to upload {sheet_name}.")
        try:
            # Check if sheet exists and clear it
            worksheet = self.spreadsheet.worksheet(sheet_name)
            print(f"Sheet {sheet_name} exists.")
            worksheet.clear()
        except gspread.exceptions.WorksheetNotFound:
            print(f"{sheet_name} not found. Trying to add it.")
            # If sheet doesn't exist, create it
            worksheet = self.spreadsheet.add_worksheet(
                title=sheet_name, rows=100, cols=20
            )
            print(f"Added sheet {sheet_name}")

        print(f"Trying to update {sheet_name}.")
        # Update the sheet with DataFrame content
        worksheet.update(
            [dataframe.columns.values.tolist()] + dataframe.values.tolist()
        )

        print(f"Uploaded {sheet_name}")


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Google Cloud Service credentials
    credentials_file_name = config["Google"]["credentials_file_name"]

    spreadsheet_key = config["Google"]["target_spreadsheet_key"]

    database_name = config["SQLite"]["database_name"]

    credentials_path = google_helper.get_credentials_path(credentials_file_name)

    converter = DatabaseSpreadsheetConverter(
        credentials_path, spreadsheet_key, database_name
    )

    try:
        # Convert database to spreadsheet
        converter.convert_to_spreadsheet()

    finally:
        # Always close the database connection
        converter.close_db_connection()


if __name__ == "__main__":
    main()
