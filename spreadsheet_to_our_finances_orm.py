from google_helper import GoogleHelper
import log_helper
import pandas as pd
import re
from sqlalchemy import create_engine, Table
from sqlalchemy_helper import SQLAlchemyHelper
import time
from our_finances_text_only_tables import *


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

        self.sql=SQLAlchemyHelper()

    def convert_to_sqlite(self):
        tables = {}
        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            print(worksheet.title)
            # table_name = worksheet.title.replace("-", "_").replace(" ", "_").lower()
            table_name = re.sub(r"[- ]", "_", worksheet.title).lower()
            print(table_name)
            tables = {f"{table_name}": eval(f"t_{table_name}")}

            log_helper.tprint(f"Converting {worksheet.title}")

            # Get worksheet data as a DataFrame
            data = worksheet.get_all_records()

            df = pd.DataFrame(data)

            # Write DataFrame to SQLite table (sheet name becomes table name)

            self.to_sql(df, tables.get(table_name))

            log_helper.tprint(f"Converted {table_name}\n")

            time.sleep(1)

        log_helper.tprint(f"Spreadsheet imported to SQLite database")

    def to_sql(self, df, table: Table):
        session = self.sql.get_session()
        try:
            with session.begin():
                # Create the table if it does not exist
                table.create(session.bind, checkfirst=True)

                # Convert the DataFrame to a list of dictionaries
                data_dicts = df.to_dict(orient="records")

                # Insert data into the table using the session
                session.execute(table.insert(), data_dicts)
        except Exception as e:
            # Rollback in case of an error
            session.rollback()
            print(f"Transaction failed: {e}")
        finally:
            session.close()


def main():
    converter = SpreadsheetDatabaseConverter()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()


if __name__ == "__main__":
    main()
