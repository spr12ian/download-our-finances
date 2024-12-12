from cls_sqlite_table import SQLiteTable


class Categories(SQLiteTable):
    def __init__(self, category=None):
        super().__init__("categories")
        self.category = category

    def fetch_by_category(self, category):
        query = self.query_builder().where(f"Category = '{category}'").build()
        return self.sql.fetch_all(query)

    def fetch_by_hmrc_page_id(self, hmrc_page, hmrc_question_id, person_code):
        query = (
            self.query_builder()
            .select("Category")
            .where(
                f'"HMRC page"="{hmrc_page}" AND "HMRC question id"="{hmrc_question_id}" AND "Category" LIKE "HMRC {person_code}%"'
            )
            .build()
        )
        return self.sql.fetch_one_value(query)

    def get_description(self):
        return self.get_value_by_category("Description")

    def get_category_group(self):
        return self.get_value_by_category("Category group")

    def get_value_by_category(self, column_name):
        if self.category:
            query = (
                self.query_builder()
                .select(column_name)
                .where(f'"Category" = "{self.category}"')
                .build()
            )
            result = self.sql.fetch_one_value(query)
        else:
            result = None

        return result
