from utility_functions import to_valid_method_name
from cls_sqlite_table import SQLiteTable


class HMRC_QuestionsByYear(SQLiteTable):
    def __init__(self, tax_year):
        super().__init__("hmrc_questions_by_year")
        self.tax_year = tax_year

    def get_questions(self):
        query = (
            self.query_builder()
            .select("Question", f"{self.tax_year}")
            .where(f'"{self.tax_year}"<> ""')
            .order("Order by")
            .build()
        )
        print(query)
        questions = [
            [
                row[0],  # question
                (split := row[1].split(","))[0],  # page
                (split[1] if len(split) > 1 else None),  # header
                (split[2] if len(split) > 2 else None),  # box
                "get_" + to_valid_method_name(row[0]),  # method
            ]
            for row in self.sql.fetch_all(query)
        ]

        return questions
