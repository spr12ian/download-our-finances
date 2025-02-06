from cls_helper_log import LogHelper
from cls_sqlite_table import SQLiteTable


class Transactions(SQLiteTable):
    def __init__(self):
        self.l = LogHelper("Transactions")
        # self.l.set_level_debug()
        self.l.debug(__file__)

        super().__init__("transactions")

    def fetch_total_where(self, where_clause):
        query = self.query_builder().total("nett").where(f"{where_clause}").build()
        self.l.debug(f"query: {query}")
        total = self.sql.fetch_one_value_float(query)
        self.l.debug(f"total: {total}")
        total = round(total, 2)
        self.l.debug(f"rounded total: {total}")
        return total

    def fetch_total_by_tax_year_category(self, tax_year, category):
        where_clause = f'"tax_year" = "{tax_year}" AND "category" = "{category}"'
        return self.fetch_total_where(where_clause)

    def fetch_total_by_tax_year_category_like(self, tax_year, category_like):
        where_clause = (
            f'"tax_year" = "{tax_year}" AND "category" LIKE "{category_like}%"'
        )
        return self.fetch_total_where(where_clause)
