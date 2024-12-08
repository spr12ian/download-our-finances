from google_helper import GoogleHelper
import log_helper
import pandas as pd
from sqlite_helper import SQLiteHelper
import time


class SpreadsheetDatabaseConverter:
    def __init__(self):
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

        self.spreadsheet = GoogleHelper().get_spreadsheet(scopes)

        self.sql = SQLiteHelper()

    def convert_to_sqlite(self):
        """
        Convert all sheets in the Google Spreadsheet to SQLite tables
        """

        db_connection = self.sql.open_connection()

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            log_helper.tprint(f"Converting {worksheet.title}")

            # Get worksheet data as a DataFrame
            data = worksheet.get_all_records()

            df = pd.DataFrame(data)

            # Write DataFrame to SQLite table (sheet name becomes table name)
            table_name = worksheet.title.replace(" ", "_").lower()

            df.to_sql(
                table_name, self.sql.db_connection, if_exists="replace", index=False
            )

            log_helper.tprint(f"Converted {table_name}\n")

            time.sleep(1)

        self.sql.close_connection()

        log_helper.tprint(f"Spreadsheet imported to SQLite database")

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
    converter = SpreadsheetDatabaseConverter()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    # Convert TEXT to REAL for selected columns
    converter.text_to_real()

if __name__ == "__main__":
    main()
