from cls_boolean_columns import BooleanColumns
from cls_date_columns import DateColumns
from cls_decimal_columns import DecimalColumns
from cls_helper_config import ConfigHelper
from cls_helper_google import GoogleHelper
from cls_helper_pandas import PandasHelper
from cls_helper_sql import SQL_Helper
from cls_helper_sqlalchemy import valid_sqlalchemy_name
from cls_int_columns import IntColumns
from cls_financial_columns import FinancialColumns
from cls_real_columns import RealColumns
import time
import spreadsheet_fields
import utility_functions as uf

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

    def convert_column_name(self, spreadsheet_column_name):
        sqlite_column_name = valid_sqlalchemy_name(spreadsheet_column_name)

        if spreadsheet_column_name.endswith(" (£)"):
            sqlite_column_name=uf.crop(sqlite_column_name, '____')
        elif spreadsheet_column_name.endswith(" (%)"):
            sqlite_column_name=uf.crop(sqlite_column_name, '____')
        elif spreadsheet_column_name.endswith("?"):
            sqlite_column_name=sqlite_column_name.strip('_')

        return sqlite_column_name

    def convert_df_col(self, df, table_name, column_name):
        self.l.debug("convert_df_col")
        sqlite_type = self.get_sqlite_type(table_name, column_name)
        self.l.debug(f"sqlite_type: {sqlite_type}")
        to_db = self.get_to_db(table_name, column_name)
        self.l.debug(f"to_db: {to_db}")
        match to_db:
            case 'to_boolean_integer':
                df = BooleanColumns().convert_column(df, column_name)
            case 'to_date':
                df = DateColumns().convert_column(df, column_name)
            case 'to_str':
                pass
            case _:
                raise ValueError(f'Unexpected to_db value: {to_db}')
            
        return df

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

        self.sql.close_connection()

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

            df.columns = [self.convert_column_name(col) for col in df.columns]
            
            self.l.debug("Before convert_df_col")
            for col in df.columns:
                df = self.convert_df_col(df, table_name, col)

            self.l.debug("After convert_df_col")

            # self.l.debug("Add 'id' column and populate with values")
            df.insert(0, "id", range(1, len(df) + 1))

        except Exception as e:
            self.l.error(f"Error converting worksheet {worksheet.title}: {e}")
            raise

        self.l.debug(f'Writing {table_name}')
        self.l.debug(f'df: {df}')
        # Write DataFrame to SQLite table (sheet name becomes table name)
        df.to_sql(
            table_name,
            self.sql.db_connection,
            if_exists="replace",
            index=False,
            dtype={"id": "INTEGER PRIMARY KEY AUTOINCREMENT"},
        )
        # self.l.debug(f'Written {table_name}')

    def get_sqlite_type(self, table_name, column_name):
        self.l.debug("get_sqlite_type")
        self.l.debug(f"table_name: {table_name}")
        self.l.debug(f"column_name: {column_name}")
        field = spreadsheet_fields.get_field_by_sqlite_column_name(
            table_name, column_name
        )
        self.l.debug(f"field: {field}")
        return field[4] # sqlite_type

    def get_to_db(self, table_name, column_name):
        field = spreadsheet_fields.get_field_by_sqlite_column_name(
            table_name, column_name
        )
        return field[3] # to_db


@debug_function_call
def main():
    l.print(f"Converting Google Sheets spreadsheet to SQLite database\n")

    converter = SpreadsheetToSqliteDb()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    l.print(f"Converted Google Sheets spreadsheet to SQLite database")


if __name__ == "__main__":
    main()
