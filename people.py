from sqlite_helper import SQLiteTable


class People(SQLiteTable):
    def __init__(self, code=None):
        super().__init__("people")
        self.code = code

    def fetch_by_code(self, code):
        print(code)
        query = f"SELECT * FROM {self.table_name} WHERE Code = '{code}'"
        print(query)
        return self.sql.fetch_all(query)

    def get_date_of_birth(self):
        if self.code:
            print(self.code)
            query = f'SELECT "Date of birth" FROM {self.table_name} WHERE Code = "{self.code}"'
            print(query)
            date_of_birth = self.sql.fetch_one_value(query)
        else:
            date_of_birth = None
        return date_of_birth

    def get_name(self):
        if self.code:
            print(self.code)
            query = f"SELECT Person FROM {self.table_name} WHERE Code = '{self.code}'"
            print(query)
            name = self.sql.fetch_one_value(query)
        else:
            name = None
        return name

    def get_spouse_code(self):
        if self.code:
            print(self.code)
            query = f"SELECT Spouse FROM {self.table_name} WHERE Code = '{self.code}'"
            print(query)
            spouse_code = self.sql.fetch_one_value(query)
        else:
            spouse_code = None

        return spouse_code
