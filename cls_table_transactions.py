from cls_sqlite_table import SQLiteTable


class Transactions(SQLiteTable):
    def __init__(self):
        super().__init__("transactions")

    def fetch_total_by_tax_year_category(self, tax_year, category):
        query = (
            self.query_builder()
            .total("Nett")
            .where(f'"Tax year" = "{tax_year}" AND "Category" = "{category}"')
            .build()
        )
        return self.sql.fetch_one_value(query)
