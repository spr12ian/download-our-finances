from cls_helper_log import LogHelper
from cls_sqlite_table import SQLiteTable
import utility_functions as uf


class HMRC_QuestionsByYear(SQLiteTable):
    yes_no_questions = [
        "Are ",
        "Did ",
        "Do ",
        "Does ",
        "Has ",
        "Have ",
        "Is ",
        "Should ",
        "Was ",
        "Were ",
    ]

    def __init__(self, tax_year):
        self.l = LogHelper("HMRC_QuestionsByYear")
        self.l.set_level_debug()
        self.l.debug(__file__)
        self.l.debug(__class__)
        self.l.debug(__name__)

        table_name = f"hmrc_questions_{tax_year.replace(' ', '_')}"
        super().__init__(table_name)

        self.l.debug(f"table_name: {table_name}")

    def __get_questions(self, columns, order_column):
        self.l.debug(f"columns: {columns}")
        self.l.debug(f"order_column: {order_column}")

        columns_as_string = self.convert_columns_to_string(columns)

        query = (
            f'SELECT {columns_as_string}, q2."Additional information"'
            + " FROM hmrc_questions_2023_to_2024 q1 JOIN hmrc_questions q2"
            + " ON q1.Question = q2.Question"
            + f' WHERE q1."{order_column}" > 0'
            + f' ORDER BY q1."{order_column}" ASC'
        )

        self.l.debug(f"query: {query}")

        # SELECT q1."Question", q1."Online section", q1."Online header", q1."Online box", q2."Additional information"
        # FROM hmrc_questions_2023_to_2024 q1 JOIN hmrc_questions q2
        # ON q1.Question = q2.Question
        # WHERE q1."Online order" > 0
        # ORDER BY q1."Online order" ASC

        questions = [
            [
                row[0],  # question
                row[1],  # section
                row[2],  # header
                row[3],  # box
                self.to_method_name(row[0]),  # method
                row[4],  # additional information
            ]
            for row in self.sql.fetch_all(query)
        ]

        return questions

    def convert_columns_to_string(self, columns):
        return ", ".join([f'q1."{column}"' for column in columns])

    def check_questions(self):
        self.l.debug("check_questions")
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
            self.l.info(f"{how_many_rows} unused questions")
            self.l.debug(query)
            for row in rows:
                self.l.info(row)

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
            self.l.debug(how_many_rows)
            self.l.debug(query)
            for row in rows:
                self.l.debug(row)

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

    def is_it_a_yes_no_question(self, question):
        return any(question.startswith(q) for q in self.yes_no_questions)

    def to_method_name(self, question):
        self.l.debug("\n\nto_method_name")
        self.l.debug(f"question: {question}")
        reformatted_question = uf.to_valid_method_name(question)
        self.l.debug(f"reformatted_question: {reformatted_question}")

        if self.is_it_a_yes_no_question(question):
            self.l.debug(f"Yes/No question: {question}")
            method_name = reformatted_question
        elif question[-6:] == " (GBP)":
            self.l.debug(" (GBP) matched")
            method_name = "get_" + uf.crop(reformatted_question, "__gbp_") + "_gbp"
        else:
            method_name = "get_" + reformatted_question

        self.l.debug(f"method_name: {method_name}")

        return method_name
