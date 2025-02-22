from cls_helper_config import ConfigHelper
from cls_helper_google import GoogleHelper
from cls_helper_pandas import PandasHelper
from cls_helper_sql import SQL_Helper
from cls_helper_sqlalchemy import valid_sqlalchemy_name
from database_keys import get_primary_key_columns, has_primary_key
import spreadsheet_fields
import time
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

        self.convert_underscore_tables = config["Google.Sheets"].getboolean(
            "convert_underscore_tables"
        )

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
            sqlite_column_name = uf.crop(sqlite_column_name, "____")
        elif spreadsheet_column_name.endswith(" (%)"):
            sqlite_column_name = uf.crop(sqlite_column_name, "____")
        elif spreadsheet_column_name.endswith("?"):
            sqlite_column_name = sqlite_column_name.strip("_")

        return sqlite_column_name

    def convert_df_col(self, df, table_name, column_name):
        self.l.debug("convert_df_col")
        sqlite_type = self.get_sqlite_type(table_name, column_name)
        self.l.debug(f"sqlite_type: {sqlite_type}")
        to_db = self.get_to_db(table_name, column_name)
        self.l.debug(f"to_db: {to_db}")
        match to_db:
            case "to_boolean_integer":
                df[column_name] = df[column_name].apply(uf.boolean_string_to_int)
            case "to_date":
                df[column_name] = df[column_name].apply(uf.UK_to_ISO)
            case "to_numeric_str":
                df[column_name] = df[column_name].apply(uf.remove_non_numeric)
            case "to_str":
                pass
            case _:
                raise ValueError(f"Unexpected to_db value: {to_db}")

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

            if has_primary_key(table_name):
                primary_key_columns = get_primary_key_columns(table_name)
                self.l.debug(f"primary_key_columns: {primary_key_columns}")
                key_column = primary_key_columns[0]
                self.l.debug(f"key_column: {key_column}")
                if key_column not in df.columns:
                    raise ValueError(
                        f"Primary key column '{key_column}' not found in worksheet '{worksheet.title}'"
                    )
                sqlite_type = self.get_sqlite_type(table_name, key_column)
                self.l.debug(f"sqlite_type: {sqlite_type}")
                dtype = {key_column: f"{sqlite_type} PRIMARY KEY"}
            else:
                # Add 'id' column and populate with values
                df.insert(0, "id", range(1, len(df) + 1))
                dtype = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT"}

        except Exception as e:
            self.l.error(f"Error converting worksheet {worksheet.title}: {e}")
            raise

        self.l.debug(f"Writing {table_name}")
        self.l.debug(f"df: {df}")
        # Write DataFrame to SQLite table (sheet name becomes table name)
        df.to_sql(
            table_name,
            self.sql.db_connection,
            if_exists="replace",
            index=False,
            dtype=dtype,
        )
        # self.l.debug(f'Written {table_name}')

    def get_sqlite_type(self, table_name, column_name):
        return spreadsheet_fields.get_sqlite_type(table_name, column_name)

    def get_to_db(self, table_name, column_name):
        return spreadsheet_fields.get_to_db(table_name, column_name)


@debug_function_call
def main():
    l.print(f"Converting Google Sheets spreadsheet to SQLite database\n")

    converter = SpreadsheetToSqliteDb()

    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()

    l.print(f"Converted Google Sheets spreadsheet to SQLite database")


if __name__ == "__main__":
    main()
