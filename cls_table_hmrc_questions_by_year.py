from utility_functions import to_valid_method_name
from cls_sqlite_table import SQLiteTable


class HMRC_QuestionsByYear(SQLiteTable):
    def __init__(self, tax_year):
        table_name = f"hmrc_questions_{tax_year.replace(' ', '_')}"
        super().__init__(table_name)

    def __get_questions(self, columns, order_column):
        query = (
            self.query_builder()
            .select(*columns)
            .where(f'"{order_column}"<> ""')
            .order(order_column)
            .build()
        )

        questions = [
            [
                row[0],  # question
                row[1],  # section
                row[2],  # header
                row[3],  # box
                "get_" + to_valid_method_name(row[0]),  # method
            ]
            for row in self.sql.fetch_all(query)
        ]

        return questions

    def get_online_questions(self):
        columns = [
            "Question",
            "Online section",
            "Online header",
            "Online box",
        ]
        order_column = "Online order"
        return self.__get_questions(columns, order_column)

    def get_printed_form_questions(self):
        columns = ["Question", "Printed section", "Printed header", "Printed box"]
        order_column = "Printed order"
        return self.__get_questions(columns, order_column)
