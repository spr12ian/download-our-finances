from cls_sqlite_table import SQLiteTable


class BankAccounts(SQLiteTable):
    def __init__(self, key=None):
        super().__init__("bank_accounts")
        self.key = key

    def fetch_by_key(self, key):
        query = self.query_builder().where(f"Code = '{key}'").build()
        return self.sql.fetch_all(query)

    def get_account_number(self):
        return self.get_value_by_key_column("Account number")

    def get_bank_name(self):
        return self.get_value_by_key_column("Institution")

    def get_sort_code(self):
        return self.get_value_by_key_column("Sort code")

    def get_value_by_key_column(self, column_name):
        if self.key:
            query = (
                self.query_builder()
                .select(column_name)
                .where(f'"Key" = "{self.key}"')
                .build()
            )
            result = self.sql.fetch_one_value(query)
        else:
            result = None

        return result
