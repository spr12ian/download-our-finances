from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper
from cls_helper_log import debug_function_call
from cls_helper_pandas import PandasHelper
from cls_helper_sqlalchemy import valid_sqlalchemy_name
from pathlib import Path
import time
import utility_functions as uf

l = LogHelper(__file__)
l.set_level_debug()
l.debug(__file__)


class SpreadsheetAnalyzer:
    def __init__(self):
        """
        Initialize the analyzer
        """
        self.l = LogHelper("SpreadsheetAnalyzer")
        self.l.set_level_debug()

        # Define the required scopes
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]

        self.spreadsheet = GoogleHelper().get_spreadsheet(scopes)

        self.pdh = PandasHelper()

        # List of list items which are table_name, column_name
        self.fields = []

    def analyze_spreadsheet(self):
        """
        Analyze all sheets in the Google Spreadsheet
        """

        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            self.analyze_worksheet(worksheet)

            time.sleep(1.1)  # Prevent Google API rate limiting

            return

        self.l.debug(self.fields)

    @debug_function_call
    def analyze_worksheet(self, worksheet):
        self.l.info(f"Analyzing {worksheet.title}")

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
                    [table_name, col, self.get_column_types(table_name, col)]
                )
                for col in df.columns
            ]

        except Exception as e:
            self.l.error(f"Error analyzing worksheet {worksheet.title}: {e}")
            raise

    def get_column_types(self, table_name, spreadsheet_column_name):
        
        sqlite_column_name=valid_sqlalchemy_name(spreadsheet_column_name)
        # sqlite_type is used to write the spreadsheet column value to the database
        # The sqlite_type may cause the spreadsheet string to be transformed
        # python_type is used when reading the database column value from the database
        # i.e. read the sqlite value and format as python type 
        if spreadsheet_column_name.endswith(" (£)"):
            sqlite_column_name=uf.crop(sqlite_column_name, '____')
            sqlite_type = "text"
            python_type = "Decimal"
        elif spreadsheet_column_name.endswith(" (%)"):
            sqlite_column_name=uf.crop(sqlite_column_name, '____')
            sqlite_type = "text"
            python_type = "Decimal"
        elif spreadsheet_column_name.endswith(" (Y/N)"):
            sqlite_column_name=uf.crop(sqlite_column_name, '__y_n_')
            sqlite_type = "integer"
            python_type = "boolean"
        elif spreadsheet_column_name.startswith("Date"):
            sqlite_type = "integer"
            python_type = "Decimal"
        else:
            sqlite_type = "text"
            python_type = "Decimal"

        return {
            "sqlite_column_name": sqlite_column_name,
            "sqlite_type": sqlite_type,
            "python_type": python_type,
        }

    def write_output(self):
        file_path = Path("spreadsheet_fields.py")
        with file_path.open("w") as output:
            output.write("fields = " + str(self.fields))


@debug_function_call
def main():
    l.print(f"Analyzing Google Sheets spreadsheet\n")

    analyzer = SpreadsheetAnalyzer()

    # Analyze spreadsheet
    analyzer.analyze_spreadsheet()

    analyzer.write_output()


if __name__ == "__main__":
    main()
