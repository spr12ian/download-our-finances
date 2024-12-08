from hmrc_category import HMRC_Category
from tables import *
from sqlite_helper import SQLiteHelper


class HMRC:
    def __init__(self, person_code, tax_year):
        print(person_code)
        print(tax_year)
        questions = [
            ["TR 1", "1", "Your date of birth"],
            ["TR 1", "3", "Your phone number"],
            ["TR 3", "2", "Total"],
            ["SES 1", "9", "Total"],
            ["UKP 2", "20", "Total"],
        ]

        self.person = People(person_code)
        categories = Categories()
        transactions = Transactions()

        for hmrc_page, box, question_type in questions:
            print(hmrc_page)
            print(box)
            print(question_type)
            match question_type:
                case "Your date of birth":
                    question = question_type
                    answer = self.person.get_date_of_birth()
                    self.hmrc_print(hmrc_page, box, question, answer)
                case "Your phone number":
                    question = question_type
                    answer = self.person.get_phone_number()
                    self.hmrc_print(hmrc_page, box, question, answer)
                case "Total":
                    category = categories.fetch_by_hmrc_page_id(
                        hmrc_page, box, person_code
                    )
                    print(category)
                    if category:
                        hmrc_category = HMRC_Category(category, person_code)
                        question = hmrc_category.get_description()

                        amount = transactions.fetch_total_by_tax_year_category(
                            tax_year, category
                        )

                        self.hmrc_print(hmrc_page, box, question, amount, "£")
                    else:
                        self.hmrc_print(
                            hmrc_page, box, person_code, "Category not found"
                        )

        query = (
            transactions.query_builder()
            .select_raw("DISTINCT Category")
            .where(
                f'"Tax year" = "{tax_year}" AND "Category" LIKE "HMRC {person_code}%"'
            )
            .build()
        )
        print(query)
        sql = SQLiteHelper()
        hmrc_transactions = sql.fetch_all(query)
        print(hmrc_transactions)

    def get_spouse_code(self):
        return self.person.get_spouse_code()

    def hmrc_print(self, hmrc_page, box, question, answer, answer_type=None):
        if answer_type == "£":
            answer = f"£{answer:,.2f}"
        print(f"Page {hmrc_page} box {box} {question}: {answer}")


class OurFinances:
    def __init__(self):
        """
        Initialize the report with the database_name name

        Args:
            database_name (str): Name of the SQLite database
        """

        # Local database connection
        self.db_connection = None
        self.sql = SQLiteHelper()

    def account_balances(self):
        query = """
            SELECT Key, Balance 
            FROM account_balances
            WHERE Balance NOT BETWEEN -1 AND 1
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def get_hmrc_data(self, person_code, tax_year):
        print(person_code)
        print(tax_year)
        return HMRC(person_code, tax_year)

    def get_year_category_total(self, tax_year, category):
        query = f"""
            SELECT SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category = '{category}'
        """

        return self.sql.fetch_one_value(query)

    def print_hmrc_report(self, person_code, tax_year):
        hmrc_data = self.get_hmrc_data(person_code, tax_year)
        spouse_code = hmrc_data.get_spouse_code()
        print(spouse_code)
        print(tax_year)
        hmrc_spouse_data = self.get_hmrc_data(spouse_code, tax_year)

        query = f"""
            SELECT "Person", "Date of birth", "Phone number", "NINO", "UTR", "UTR check digit"
            FROM people
            WHERE "Code" = '{person_code}'
        """

        row = self.sql.fetch_one_row(query)
        person_name = row[0]
        date_of_birth = row[1]
        phone_number = row[2]
        national_insurance_number = row[3]
        unique_tax_reference = row[4]
        utr_check_digit = row[5]

        print(
            f"HMRC {tax_year} tax return for {person_name} - {unique_tax_reference}{utr_check_digit}"
        )

        print("\nPage TR 1\n")

        print(f"1 Your date of birth: {date_of_birth}")
        print(f"3 Your phone number: {phone_number}")
        print(f"4 Your National Insurance number: {national_insurance_number}")

        print("\nPage TR 2\n")

        query = f"""
            SELECT COUNT(DISTINCT Category)
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category LIKE 'HMRC {person_code} EMP%income'
        """

        how_many = self.sql.fetch_one_value(query)

        question_number = 1
        question = "Employment"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
            answer += f", Number: {how_many}"
        else:
            answer += f" - No: X"
            answer += f", Number: 0"

        print(answer)

        query = f"""
            SELECT COUNT(DISTINCT Category)
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category LIKE 'HMRC {person_code} SE%income'
        """

        how_many = self.sql.fetch_one_value(query)

        question_number += 1
        question = "Self-employment"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
            answer += f", Number: {how_many}"
        else:
            answer += f" - No: X"
            answer += f", Number: 0"

        print(answer)

        how_many = 0
        question_number += 1
        question = "Partnership"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
            answer += f", Number: {how_many}"
        else:
            answer += f" - No: X"
            answer += f", Number: 0"

        print(answer)

        query = f"""
            SELECT COUNT(DISTINCT Category)
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category LIKE 'HMRC {person_code} property income%'
        """

        how_many = self.sql.fetch_one_value(query)

        question_number += 1
        question = "UK property"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "Foreign"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "Trusts etc"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "Capital Gains Tax summary"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
            answer += f", Computation(s) provided: "
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "Residence remittance basis etc"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "Additional information"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

        how_many = 0

        question_number += 1
        question = "If you need more pages"
        answer = f"{question_number} {question}"
        if how_many:
            answer += f" - Yes: X"
        else:
            answer += f" - No: X"

        print(answer)

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
    # our_finances.print_HMRC("B", "2023 to 2024")
    our_finances.print_hmrc_report("B", "2023 to 2024")


if __name__ == "__main__":
    main()
