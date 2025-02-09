from cls_date_columns import DateColumns
from cls_helper_config import ConfigHelper
from cls_helper_google import GoogleHelper
from cls_helper_pandas import PandasHelper
from cls_helper_sql import SQL_Helper
from cls_helper_sqlalchemy import valid_sqlalchemy_name
from cls_int_columns import IntColumns
from cls_financial_columns import FinancialColumns
from cls_real_columns import RealColumns
import time
from sqlalchemy import Column
from sqlalchemy import Integer

from cls_helper_log import LogHelper
from cls_helper_log import debug_function_call

l = LogHelper(__file__)
l.set_level_debug()
l.debug(__file__)


class SpreadsheetToSqliteDb:
    def __init__(self):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name

        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """
        self.l = LogHelper("SpreadsheetToSqliteDb")
        self.l.set_level_debug()
        config = ConfigHelper()
        if config["Google"]["convert_underscore_tables"] == "No":
            self.convert_underscore_tables = False
        else:
            self.convert_underscore_tables = True

        self.pdh = PandasHelper()

        # Define the required scopes
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]

        self.spreadsheet = GoogleHelper().get_spreadsheet(scopes)

        self.sql = SQL_Helper().select_sql_helper("SQLite")

        # List of list items which are table_name, column_name
        self.fields = []

    def convert_to_sqlite(self):
        """
        Convert all sheets in the Google Spreadsheet to SQLite tables
        """
        self.sql.open_connection()

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            if self.convert_underscore_tables or not worksheet.title.startswith("_"):
                self.convert_worksheet(worksheet)

                time.sleep(1.1)  # Prevent Google API rate limiting

                self.l.debug(self.fields)

                raise

        self.sql.close_connection()

    def get_sqlite_type(self, table_name, column_name):
        if column_name.endswith("(£)"):
            sqlite_type = "text"
        elif column_name.endswith("(%)"):
            sqlite_type = "text"
        elif column_name.endswith("(Y/N)"):
            sqlite_type = "integer"
        else:
            sqlite_type = "text"

        return sqlite_type

    @debug_function_call
    def convert_worksheet(self, worksheet):
        self.l.info(f"Converting {worksheet.title}")

        table_name = valid_sqlalchemy_name(worksheet.title)
        self.l.info(f"table_name: {table_name}")

        pdh = self.pdh

        # Get worksheet data as a DataFrame
        data = worksheet.get_all_values()

        try:
            # Split columns and rows
            df = pdh.worksheet_values_to_dataframe(data)
            [
                self.fields.append(
                    [table_name, col, self.get_sqlite_type(table_name, col)]
                )
                for col in df.columns
            ]
            df.columns = [valid_sqlalchemy_name(col) for col in df.columns]
            # df = DateColumns().convert(df)
            # df = IntColumns().convert(df)
            # df = RealColumns().convert(df)
            # df = FinancialColumns().convert(df)
            # self.l.debug("Add 'id' column and populate with values")
            df.insert(0, "id", range(1, len(df) + 1))

            # # Ensure all columns have appropriate data types
            # for col in df.columns:
            #     self.l.debug(f'df[col].dtype: {df[col].dtype}')
            #     if df[col].dtype == 'object':
            #         df[col] = df[col].astype(str)
            #     elif df[col].dtype == 'int64':
            #         df[col] = df[col].astype(int)
            #     elif df[col].dtype == 'float64':
            #         df[col] = df[col].astype(float)
            #     elif pdh.pd.api.types.is_datetime64_any_dtype(df[col]):
            #         df[col] = df[col].astype(str)  # Convert datetime to string

        except Exception as e:
            self.l.error(f"Error converting worksheet {worksheet.title}: {e}")
            raise

        # self.l.debug(f'Writing {table_name}')
        # self.l.debug(f'df: {df}')
        # Write DataFrame to SQLite table (sheet name becomes table name)
        df.to_sql(
            table_name,
            self.sql.db_connection,
            if_exists="replace",
            index=False,
            dtype={"id": "INTEGER PRIMARY KEY AUTOINCREMENT"},
        )
        # self.l.debug(f'Written {table_name}')


@debug_function_call
def main():
    l.print(f"Converting Google Sheets spreadsheet to SQLite database\n")

    converter = SpreadsheetToSqliteDb()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    l.print(f"Converted Google Sheets spreadsheet to SQLite database")


if __name__ == "__main__":
    main()
