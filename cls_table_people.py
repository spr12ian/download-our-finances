from cls_helper_date_time import DateTimeHelper
from cls_sqlite_table import SQLiteTable


class People(SQLiteTable):
    def __init__(self, code=None):
        super().__init__("people")
        self.code = code

    def fetch_by_code(self, code):
        query = self.query_builder().where(f"Code = '{code}'").build()
        return self.sql.fetch_all(query)

    def get_address(self):
        return self.get_value_by_code_column("Address")

    def get_date_of_birth(self):
        return self.get_value_by_code_column("Date of birth")

    def get_first_name(self):
        return self.get_value_by_code_column("First name")

    def get_last_name(self):
        return self.get_value_by_code_column("Last nname")

    def get_middle_name(self):
        return self.get_value_by_code_column("Middle name")

    def get_name(self):
        return self.get_value_by_code_column("Person")

    def get_phone_number(self):
        return self.get_value_by_code_column("Phone number")

    def get_uk_date_of_birth(self):
        return DateTimeHelper().ISO_to_UK(self.get_date_of_birth())

    def get_value_by_code_column(self, column_name):
        if self.code:
            query = (
                self.query_builder()
                .select(column_name)
                .where(f'"Code" = "{self.code}"')
                .build()
            )
            result = self.sql.fetch_one_value(query)
        else:
            result = None

        return result
