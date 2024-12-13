from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper
import pandas as pd
import re
from cls_helper_sqlite import SQLiteHelper
import time


class SpreadsheetToSqliteDb:
    def __init__(self):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """

        self.log = LogHelper()

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

        real_columns = [
            "Account maximum",
            "Account minimum",
            "Amount",
            "Annual",
            "Annual interest (AER)",
            "Asset value",
            "Balance",
            "Change",
            "Change required",
            "Credit",
            "Credits due",
            "Daily",
            "Debit",
            "Debits due",
            "Dynamic amount",
            "Excess",
            "Fixed amount",
            "Four weekly",
            "Interest",
            "Interest rate",
            "Minimum today",
            "Monthly",
            "Monthly interest",
            "Nett",
            "Shortfall",
            "Sporadic",
            "Taxable interest",
            "Tolerance",
            "Total credit",
            "Total debit",
            "Weekly",
        ]

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            self.log.tprint(f"Converting {worksheet.title}")

            table_name = worksheet.title.replace(" ", "_").lower()

            # Get worksheet data as a DataFrame
            data = worksheet.get_all_values()

            # Create a DataFrame
            columns = data[0]  # Assume the first row contains headers
            rows = data[1:]  # Remaining rows are the data
            df = pd.DataFrame(rows, columns=columns)
            for real_column in real_columns:
                if real_column in df.columns:
                    try:
                        df[real_column] = df[real_column].apply(self.string_to_float)
                    except:
                        print(table_name)
                        print(real_column)
                        raise

            # Write DataFrame to SQLite table (sheet name becomes table name)

            df.to_sql(
                table_name, self.sql.db_connection, if_exists="replace", index=False
            )

            self.log.tprint(f"Converted {table_name}\n")

            time.sleep(1)

        self.sql.close_connection()

    # Function to convert currency strings to float
    def string_to_float(self, string):
        if string.strip() == "":  # Check if the string is empty or whitespace
            return 0.0
        else:
            # Remove the currency symbol (£), commas, and percent then convert to float
            return float(re.sub(r"[£,%]", "", string))


def main():
    log = LogHelper()
    log.print_date_today()
    log.tprint(f"Converting Google Sheets spreadsheet to SQLite database")

    converter = SpreadsheetToSqliteDb()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    log.tprint(f"Converted Google Sheets spreadsheet to SQLite database")


if __name__ == "__main__":
    main()
