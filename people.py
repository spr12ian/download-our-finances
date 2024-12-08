from sqlite_helper import SQLiteQueryBuilder
from sqlite_helper import SQLiteTable


class People(SQLiteTable):
    def __init__(self, code=None):
        super().__init__("people")
        self.code = code

    def fetch_by_code(self, code):
        query = self.query_builder().where(f"Code = '{code}'").build()
        return self.sql.fetch_all(query)

    def get_first_name(self):
        tokens=self.get_value_by_code("Person").split(' ')
        return tokens[0]

    def get_date_of_birth(self):
        return self.get_value_by_code("Date of birth")

    def get_last_name(self):
        tokens=self.get_value_by_code("Person").split(' ')
        return tokens[1]

    def get_name(self):
        return self.get_value_by_code("Person")

    def get_national_insurance_number(self):
        return self.get_value_by_code("NINO")

    def get_phone_number(self):
        return self.get_value_by_code("Phone number")

    def get_spouse_code(self):
        return self.get_value_by_code("Spouse")

    def get_unique_tax_reference(self):
        return self.get_value_by_code("UTR")

    def get_utr_check_digit(self):
        return self.get_value_by_code("UTR check digit")

    def get_value_by_code(self, column_name):
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
