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

TYPE_MAPPING = {
    " (£)": {"to_db": "to_numeric_str", "sqlite_type": "TEXT", "from_db": "from_decimal_2", "python_type": "Decimal"},
    " (%)": {"to_db": "to_numeric_str", "sqlite_type": "TEXT", "from_db": "from_decimal", "python_type": "Decimal"},
    "?": {"to_db": "to_boolean_integer", "sqlite_type": "INTEGER", "from_db": "from_boolean_integer", "python_type": "bool"},
    "Date ": {"to_db": "to_date", "sqlite_type": "TEXT", "from_db": "from_str", "python_type": "str"},
}

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

        self.l.debug(self.fields)

    @debug_function_call
    def analyze_worksheet(self, worksheet):
        self.l.info(f"Analyzing {worksheet.title}")

        table_name = valid_sqlalchemy_name(worksheet.title)
        self.l.info(f"table_name: {table_name}")

        pdh = self.pdh
        try:
            first_row = worksheet.row_values(1)
            self.l.debug(f'first_row: {first_row}')
            
            # Split columns and rows
            df = pdh.header_to_dataframe(first_row)
            [
                self.fields.append(
                    self.get_column_types(table_name, col)
                )
                for col in df.columns
            ]

        except Exception as e:
            self.l.error(f"Error analyzing worksheet {worksheet.title}: {e}")
            raise

    def get_column_types(self, table_name, spreadsheet_column_name):
        self.l.debug("get_column_types")
        self.l.debug(f'spreadsheet_column_name: {spreadsheet_column_name}')

        # sqlite_type is used to write the spreadsheet column value to the database
        # The sqlite_type may cause the spreadsheet string to be transformed

        # python_type is used when reading the database column value from the database
        # i.e. read the sqlite value and format as python type 
        
        sqlite_column_name = valid_sqlalchemy_name(spreadsheet_column_name)
        for type_map_key, type_info in TYPE_MAPPING.items():
            if spreadsheet_column_name.endswith(type_map_key):
                if type_map_key == "?":  # Only for boolean columns
                    sqlite_column_name = sqlite_column_name.strip('_')
                elif type_map_key != "?":  # For the other special cases
                    sqlite_column_name = uf.crop(sqlite_column_name, '____')

                self.l.debug(f'type_info["sqlite_type"]:{type_info["sqlite_type"]}')
                return [
                    table_name,
                    spreadsheet_column_name,
                    sqlite_column_name,
                    type_info["to_db"],
                    type_info["sqlite_type"],
                    type_info["from_db"],
                    type_info["python_type"],
                ]
        
            if spreadsheet_column_name.startswith(type_map_key):
                return [
                    table_name,
                    spreadsheet_column_name,
                    sqlite_column_name,
                    type_info["to_db"],
                    type_info["sqlite_type"],
                    type_info["from_db"],
                    type_info["python_type"],
                ]

        sqlite_type = "TEXT"
        python_type = "str"
        to_db = "to_str"
        from_db = "from_str"

        return [
            table_name,
            spreadsheet_column_name,
            sqlite_column_name,
            to_db,
            sqlite_type,
            from_db,
            python_type,
        ]


    def write_output(self):
        file_path = Path("spreadsheet_fields.py")
        with file_path.open("w") as output:
            prefix=self.get_prefix()
            fields_output=self.get_fields_output()
            output.write(prefix + fields_output)

    def get_fields_output(self):
        for field in self.fields:
            self.l.debug(f'field: {field}')
        return str(self.fields)

    def get_prefix(self):
        prefix='''# spreadsheet_fields.py
def get_field_by_spreadsheet_column_name(table_name, spreadsheet_column_name):
    for field in fields:
        if field[1] == spreadsheet_column_name and field[0] == table_name:
            return field
    return None

def get_field_by_sqlite_column_name(table_name, sqlite_column_name):
    for field in fields:
        if field[2] == sqlite_column_name and field[0] == table_name:
            return field
    return None

def get_from_db(table_name, column_name):
    field = get_field_by_sqlite_column_name(
        table_name, column_name
    )
    return field[5] # from_db

def get_python_type(table_name, column_name):
    field = get_field_by_sqlite_column_name(
        table_name, column_name
    )
    return field[6] # python_type

def get_sqlite_type(table_name, column_name):
    field = get_field_by_sqlite_column_name(
        table_name, column_name
    )
    return field[4] # sqlite_type

def get_to_db(table_name, column_name):
    field = get_field_by_sqlite_column_name(
        table_name, column_name
    )
    return field[3] # to_db

# table_name, spreadsheet_column_name, sqlite_column_name, to_db, sqlite_type, from_db, python_type
fields = '''
        return prefix


@debug_function_call
def main():
    l.print(f"Analyzing Google Sheets spreadsheet\n")

    analyzer = SpreadsheetAnalyzer()

    # Analyze spreadsheet
    analyzer.analyze_spreadsheet()

    analyzer.write_output()


if __name__ == "__main__":
    main()
