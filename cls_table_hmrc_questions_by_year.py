from cls_sqlite_table import SQLiteTable
from utility_functions import to_valid_method_name

from cls_helper_log import LogHelper

l = LogHelper(__name__)
# l.setLevelDebug()
l.debug(__file__)


class HMRC_QuestionsByYear(SQLiteTable):
    def __init__(self, tax_year):
        l.debug(__class__)
        l.debug(__name__)
        table_name = f"hmrc_questions_{tax_year.replace(' ', '_')}"
        super().__init__(table_name)
        l.debug(table_name)

    def __get_questions(self, columns, order_column):
        query = (
            self.query_builder()
            .select(*columns)
            .where(f'"{order_column}" > 0')
            .order(order_column)
            .build()
        )

        questions = [
            [
                row[0],  # question
                row[1],  # section
                row[2],  # header
                row[3],  # box
                self.to_method_name(row[0]),  # method
            ]
            for row in self.sql.fetch_all(query)
        ]

        return questions

    def check_questions(self):
        l.debug("check_questions")
        core_questions = "hmrc_questions"
        query = (
            "SELECT q1.Question"
            + f" FROM {core_questions} q1 LEFT JOIN {self.table_name} q2"
            + " ON q1.Question=q2.Question"
            + " WHERE q2.Question IS NULL"
        )
        rows = self.sql.fetch_all(query)
        how_many_rows = len(rows)
        if how_many_rows > 0:
            l.info(f"{how_many_rows} unused questions")
            l.debug(query)
            for row in rows:
                l.info(row)

        query = (
            'SELECT q1.Question, q1."Online order", q2."Printed order"'
            + f" FROM {self.table_name} q1 JOIN {self.table_name} q2"
            + " WHERE q1.Question=q2.Question"
            + ' AND q1."Online order" > 0'
            + ' AND q2."Online order" = 0'
        )
        rows = self.sql.fetch_all(query)
        how_many_rows = len(rows)
        if how_many_rows > 0:
            l.debug(how_many_rows)
            l.debug(query)
            for row in rows:
                l.debug(row)

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

    def to_method_name(self, question):
        l.debug("\nto_method_name")
        l.debug(f"question: {question}")
        reformatted_question = to_valid_method_name(question)
        l.debug(f"reformatted_question: {reformatted_question}")

        if question[:3] == "If ":
            l.debug("If matched")
            method_name = reformatted_question
        elif question[-6:] == " (GBP)":
            l.debug(" (GBP) matched")
            method_name = "get_" + reformatted_question[:-6] + "_gbp"
        else:
            method_name = "get_" + to_valid_method_name(question)

        l.debug(f"method_name: {method_name}")

        return method_name
