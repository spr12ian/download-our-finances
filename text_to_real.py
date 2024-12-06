import configparser
import google_helpers
import log_helper
import pandas as pd
import sqlite_helper
import time


class TextToReal:
    def __init__(self, credentials_path, spreadsheet_key, database_name):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """

        # Define the required scopes
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]

        client = google_helpers.get_authorized_client(credentials_path, scopes)

        # Open the spreadsheet
        self.spreadsheet = client.open_by_key(spreadsheet_key)

        # Local database connection
        self.db_connection = None
        self.db_path = database_name + ".db"
        self.sql = sqlite_helper.SQLiteHelper(self.db_path)

    def text_to_real(self):
        real_columns = [
            ["account_balances", "Credit"],
            ["account_balances", "Debit"],
            ["account_balances", "Balance"],
            ["transactions", "Credit"],
            ["transactions", "Debit"],
            ["transactions", "Nett"],
        ]

        for table_name, column_name in real_columns:
            self.sql.text_to_real(table_name, column_name)


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Google Cloud Service credentials
    credentials_file_name = config["Google"]["credentials_file_name"]
    credentials_path = google_helpers.get_credentials_path(credentials_file_name)

    spreadsheet_key = config["Google"]["source_spreadsheet_key"]

    database_name = config["SQLite"]["database_name"]

    converter = TextToReal(credentials_path, spreadsheet_key, database_name)

    # Convert TEXT to REAL for selected columns
    converter.text_to_real()


if __name__ == "__main__":
    main()
