from cls_hmrc import HMRC
from cls_table_hmrc_questions_by_year import HMRC_QuestionsByYear
from cls_helper_log import LogHelper
from datetime import datetime

l = LogHelper(__file__)
l.set_level_debug()
l.debug(__file__)


def check_questions(tax_year):
    questions = HMRC_QuestionsByYear(tax_year)
    questions.check_questions()


def print_reports(hmrc_people, tax_year):
    for person in hmrc_people:        
        l.debug(f"Getting HMRC instance for person: {person}, tax year: {tax_year}")
        hmrc = HMRC(person, tax_year)
        hmrc.print_reports()
        #exit()


def main():
    # List of people to generate reports for
    hmrc_people = ["S", "B"]
    hmrc_people = ["B"]

    earliest_year = 2023

    tax_years = get_tax_years_from(earliest_year)

    for tax_year in tax_years:
        # Tax year to generate reports for

        check_questions(tax_year)

        print_reports(hmrc_people, tax_year)


def get_tax_years_from(earliest_year) -> list[str]:
    current_year = datetime.now().year
    years_to_report = list(range(earliest_year, current_year))

    tax_years = [f"{year} to {year + 1}" for year in years_to_report]
    return tax_years


if __name__ == "__main__":
    main()
