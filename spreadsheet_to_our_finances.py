from cls_date_columns import DateColumns
from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper
from cls_helper_pandas import PandasHelper
from cls_helper_sql import SQL_Helper
from cls_int_columns import IntColumns
from cls_real_columns import RealColumns
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

        self.sql = SQL_Helper().select_sql_helper("SQLite")

    def convert_to_sqlite(self):
        """
        Convert all sheets in the Google Spreadsheet to SQLite tables
        """
        self.sql.open_connection()

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():

            self.convert_worksheet(worksheet)

            time.sleep(1)

        self.sql.close_connection()

    @LogHelper.log_execution_time
    def convert_worksheet(self, worksheet):
        self.log.debug(f"Converting {worksheet.title}")

        table_name = worksheet.title.replace(" ", "_").lower()

        # Get worksheet data as a DataFrame
        data = worksheet.get_all_values()

        try:
            df = PandasHelper().worksheet_values_to_dataframe(data)
            df = DateColumns().convert(df)
            df = IntColumns().convert(df)
            df = RealColumns().convert(df)
        except:
            print(table_name)
            raise

        # Write DataFrame to SQLite table (sheet name becomes table name)
        df.to_sql(table_name, self.sql.db_connection, if_exists="replace", index=False)


def main():
    LogHelper.debug_enabled = True
    log = LogHelper()
    log.debug_date_today()
    log.tdebug(f"Converting Google Sheets spreadsheet to SQLite database\n")

    converter = SpreadsheetToSqliteDb()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    log.tdebug(f"Converted Google Sheets spreadsheet to SQLite database")


if __name__ == "__main__":
    main()
