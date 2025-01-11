from cls_hmrc import HMRC
from cls_table_hmrc_questions_by_year import HMRC_QuestionsByYear
from cls_helper_log import LogHelper

l = LogHelper(__file__)
# l.set_level_debug()
l.debug(__file__)


def check_questions(tax_year):
    questions = HMRC_QuestionsByYear(tax_year)
    questions.check_questions()


def print_reports(hmrc_people, tax_year):
    for person in hmrc_people:
        hmrc = HMRC(person, tax_year)
        hmrc.print_reports()


def main():
    # List of people to generate reports for
    hmrc_people = ["S", "B", "C"]

    # Tax year to generate reports for
    tax_year = "2023 to 2024"

    check_questions(tax_year)

    print_reports(hmrc_people, tax_year)


if __name__ == "__main__":
    main()
