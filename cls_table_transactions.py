from cls_sqlite_table import SQLiteTable


class Transactions(SQLiteTable):
    def __init__(self):
        super().__init__("transactions")

    def fetch_total_where(self, where_clause):
        query = self.query_builder().total("Nett").where(f"{where_clause}").build()
        return self.sql.fetch_one_value_float(query)

    def fetch_total_by_tax_year_category(self, tax_year, category):
        where_clause = f'"Tax year" = "{tax_year}" AND "Category" = "{category}"'
        return self.fetch_total_where(where_clause)

    def fetch_total_by_tax_year_category_like(self, tax_year, category_like):
        where_clause = (
            f'"Tax year" = "{tax_year}" AND "Category" LIKE "{category_like}%"'
        )
        return self.fetch_total_where(where_clause)
