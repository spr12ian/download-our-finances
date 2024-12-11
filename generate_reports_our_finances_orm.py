from hmrc_category import HMRC_Category
from sqlalchemy_helper import SQLAlchemyHelper
import sys
from our_finances_tables import *
from tables import *

class HMRC:
    def __init__(self, person_code, tax_year):
        self.person_code = person_code
        self.tax_year = tax_year
        self.person = People(person_code)
        self.spouse = People(self.person.get_spouse_code())
        self.categories = Categories()
        self.transactions = Transactions()
        self.sql = SQLAlchemyHelper()

        # self.list_categories()

    def append_header(self, answers, header):
        header = f"\n{header.upper()}"
        this_return = f"{self.person.get_name()} {self.tax_year}\n"

        answers.append([header, "", "", this_return])

        answers.append(["Section", "Box", "Question", "Answer"])

        return answers

    def call_method(self, method_name):
        try:
            method = getattr(self, method_name)
            return method()
        except AttributeError:
            print(f"Method {method_name} not found")

    def format_answer(self, string_list):
        if len(string_list[2]) > 0:
            widths = [8, 5, 55]  # Define column widths

            # Use zip to pair strings with widths and format them in one step
            formatted_parts = [
                f"{string:<{width}}" for string, width in zip(string_list[:3], widths)
            ]
        else:
            widths = [69]  # Define column widths

            # Use zip to pair strings with widths and format them in one step
            formatted_parts = [
                f"{string:<{width}}" for string, width in zip(string_list[:1], widths)
            ]

        # Join the formatted parts and append the fourth string without formatting
        return "".join(formatted_parts) + string_list[3]

    def get_additional_information__yes_no_(self):
        return False

    def get_answers(self):
        answers = []
        for question, section, box, method_name, header in self.get_questions():
            if header:
                answers = self.append_header(answers, header)

            answer = self.call_method(method_name)

            answers.append([section, box, question, answer])
            # match question:
            #     case "Declaration":
            #         answer = "Sign & date"
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Collect by PAYE":
            #         answer = "NO"
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Collect small amounts by PAYE":
            #         answer = "NO"
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Date of marriage":
            #         answer = "10/04/2018"
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your spouse's first name":
            #         answer = self.spouse.get_first_name()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your spouse's last name":
            #         answer = self.spouse.get_last_name()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your date of birth":
            #         answer = self.person.get_date_of_birth()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your spouse's date of birth":
            #         answer = self.spouse.get_date_of_birth()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your phone number":
            #         answer = self.person.get_phone_number()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your National Insurance number":
            #         answer = self.person.get_national_insurance_number()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Your spouse's National Insurance number":
            #         answer = self.spouse.get_national_insurance_number()
            #         answers[question] = f"{section} {box} {question}: {answer}"
            #     case "Total":
            #         category = self.categories.fetch_by_section_box(
            #             section, box, self.person_code
            #         )
            #         if category:
            #             hmrc_category = HMRC_Category(category, self.person_code)
            #             question = hmrc_category.get_description()

            #             amount = self.transactions.fetch_total_by_tax_year_category(
            #                 self.tax_year, category
            #             )

            #             answers[question] = (
            #                 f"{section} {box} {question}: £{amount:,.2f}"
            #             )
            #         else:
            #             sys.stderr.write(
            #                 f'{section}, {box}, {self.person_code}, "Category not found"\n'
            #             )
            #     case _:
            #         sys.stderr.write(f"Unhandled question: {question}\n")

        return answers

    def get_any_tax_taken_off_box_17(self):
        return 0

    def get_benefit_from_pre_owned_assets(self):
        return 0

    def get_capital_gains_tax_summary__yes_no_(self):
        return False

    def get_computations_provided__yes_no_(self):
        return False

    def get_description_of_income_in_boxes_17_and_20(self):
        return ""

    def get_dividends_from_uk_companies(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Dividends from UK companies"
        )

    def get_foreign_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Foreign dividends"
        )

    def get_foreign__yes_no_(self):
        return False

    def get_full_utr(self):
        utr = self.person.get_unique_tax_reference()
        utr_check_digit = self.person.get_utr_check_digit()
        return utr + utr_check_digit

    def get_how_many_businesses(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_how_many_employments(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_how_many_partnerships(self):
        return 0

    def get_jobseeker_s_allowance(self):
        return 0

    def get_more_pages__yes_no_(self):
        return False

    def get_other_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Other dividends"
        )

    def get_other_taxable_income(self):
        return 0

    def get_pensions__other_than_state_pension_(self):
        return 0

    def get_residence__remittance_basis_etc__yes_no_(self):
        return False

    def get_questions(self):
        return HMRC_QuestionsByYear(self.tax_year).get_questions()

    def get_spouse_code(self):
        return self.person.get_spouse_code()

    def get_state_pension(self):
        return 0

    def get_state_pension_lump_sum(self):
        return 0

    def get_tax_taken_off_box_9(self):
        return 0

    def get_tax_taken_off_box_11(self):
        return 0

    def get_tax_taken_off_foreign_dividends(self):
        return 0

    def get_tax_taken_off_incapacity_benefit_in_box_13(self):
        return 0

    def get_taxable_incapacity_benefit(self):
        return 0

    def get_taxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Taxed UK interest"
        )

    def get_title(self):
        full_utr = self.get_full_utr()
        person_name = self.person.get_name()
        tax_year = self.tax_year

        return f"HMRC {tax_year} tax return for {person_name} - {full_utr}\n"

    def get_total_amount_of_allowable_expenses(self):
        return 0

    def get_total_of_any_other_taxable_state_pensions_and_benefits(self):
        return 0

    def get_trusts_etc__yes_no_(self):
        return False

    def get_untaxed_foreign_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Untaxed foreign interest"
        )

    def get_untaxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Untaxed UK interest"
        )

    def get_uk_property__yes_no_(self):
        # search the transactions table for any records in this tax year
        # which have a UKP income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} UKP income%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def get_year_category_total(self, tax_year, category):
        return self.transactions.fetch_total_by_tax_year_category(tax_year, category)

    def get_your_date_of_birth(self):
        return self.person.get_date_of_birth()

    def get_your_name_and_address(self):
        return self.person.get_name()

    def get_your_national_insurance_number(self):
        return self.person.get_national_insurance_number()

    def get_your_phone_number(self):
        return self.person.get_phone_number()

    def get_were_you_employed_in_this_tax_year(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def get_were_you_in_partnership_s__this_tax_year(self):
        return False

    def get_were_you_self_employed_in_this_tax_year(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def list_categories(self):
        query = (
            self.transactions.query_builder()
            .select_raw("DISTINCT Category")
            .where(
                f'"Tax year" = "{self.tax_year}" AND "Category" LIKE "HMRC {self.person_code}%" ORDER BY Category'
            )
            .build()
        )
        print(query)

        categories = SQLAlchemyHelper().fetch_all(query)
        for row in categories:
            print(row[0])

    def print_answer(self, section, box, question, answer):
        if isinstance(answer, bool):
            answer = "Yes" if answer else "No"
        elif isinstance(answer, float):
            answer = f"£{answer:,.2f}"
        elif isinstance(answer, int):
            answer = f"{answer:,}"
        elif isinstance(answer, str):
            pass  # No change needed for strings
        else:
            answer = str(answer)

        formatted_answer = self.format_answer([section, box, question, answer])

        print(formatted_answer)

    def print_report(self):

        print(self.get_title())

        answers = self.get_answers()

        for section, box, question, answer in answers:
            self.print_answer(section, box, question, answer)

        print(
            "\n=========================================================================================\n"
        )

    def print_hmrc_report(self):
        tax_year = self.tax_year
        person_code = self.person_code

        print("\nPage TR 3\n")

        question_number = 1
        question = "Taxed UK interest: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Untaxed UK interest: "
        answer = f"{question_number} {question}"

        amount = self.get_year_category_total(
            tax_year, f"HMRC {person_code} Untaxed UK interest"
        )

        if amount:
            answer += f"£{amount:,.2f}"

        print(answer)

        question_number += 1
        question = "Untaxed foreign interest: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Dividends from UK companies: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Foreign dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off foreign dividends: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "State pension: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "State pension lump sum: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 9: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other pensions: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 11: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Taxable incapacity benefit: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Tax taken off box 13: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Jobseeker's Allowance: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any other taxable State Pensions and benefits: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Other taxable income: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total amount of allowable expenses: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Any tax taken off box 17: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Benefit from pre-owned assets: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Description of income in boxes 17 and 20: "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 4\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)
        print(answer)

        print("\nPage TR 5\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number = 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number = 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 6\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)
        print(answer)

        print("\nPage TR 7\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TR 8\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 3\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage Ai 4\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage SES 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage SES 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage UKP 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage UKP 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TC 1\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        print("\nPage TC 2\n")

        question_number = 1
        question = "Gross pension payments (relief at source): "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Total of any 'one off' payments in box 1: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = ": "
        answer = f"{question_number} {question}"
        print(answer)

        query = f"""
            SELECT Category, SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category LIKE 'HMRC {person_code}%'
            GROUP BY Category
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


class OurFinances:
    def __init__(self):
        """
        Initialize the report with the database_name name
        """

        self.sql = SQLAlchemyHelper()

    def account_balances(self):
        query = """
            SELECT Key, Balance 
            FROM account_balances
            WHERE Balance NOT BETWEEN -1 AND 1
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def people(self):
        query = """
            SELECT * 
            FROM people
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def transactions(self):
        query = """
            SELECT Category, SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '2023 to 2024'
            AND Category LIKE 'HMRC%'
            GROUP BY Category
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def main():
    our_finances = OurFinances()

    # our_finances.print_account_balances()
    # our_finances.print_people()
    # our_finances.print_transactions()

    hmrc = HMRC("B", "2023 to 2024")
    hmrc.print_report()

    hmrc = HMRC("S", "2023 to 2024")
    hmrc.print_report()


if __name__ == "__main__":
    main()
