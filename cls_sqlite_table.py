from cls_helper_sqlite import SQLiteHelper
from cls_query_builder import QueryBuilder


class SQLiteTable:
    def __init__(self, table_name):
        self.sql = SQLiteHelper()
        self.table_name = table_name

    def fetch_all(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.sql.fetch_all(query)

    def get_how_many(self):
        return self.sql.get_how_many(self.table_name)

    def query_builder(self):
        return QueryBuilder(self.table_name)
