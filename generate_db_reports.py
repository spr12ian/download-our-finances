import configparser
import sqlite_helper


class Generate_DB_Reports:
    def __init__(self, database_name):
        """
        Initialize the reporter with the database_name name

        Args:
            database_name (str): Name of the SQLite database
        """

        # Local database connection
        self.db_connection = None
        self.db_path = database_name + ".db"
        self.sql = sqlite_helper.SQLiteHelper(self.db_path)

    def account_balances(self):
        query = """
            SELECT Key, Balance 
            FROM account_balances
            WHERE Balance NOT BETWEEN -1 AND 1
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def get_year_category_total(self, tax_year, category):
        query = f"""
            SELECT SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category = '{category}'
        """

        return self.sql.fetch_one_value(query)

    def HMRC(self, owner_code, tax_year):
        query = f"""
            SELECT "Person", "Date of birth", "Phone number", "NINO", "UTR", "UTR check digit"
            FROM people
            WHERE "Code" = '{owner_code}'
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
            AND Category LIKE 'HMRC {owner_code} EMP%income'
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
            AND Category LIKE 'HMRC {owner_code} SE%income'
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
            AND Category LIKE 'HMRC {owner_code} property income%'
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
            tax_year, f"HMRC {owner_code} Untaxed UK interest"
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
            AND Category LIKE 'HMRC {owner_code}%'
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
    config = configparser.ConfigParser()
    config.read("config.ini")

    database_name = config["SQLite"]["database_name"]

    reporter = Generate_DB_Reports(database_name)

    # reporter.account_balances()
    # reporter.people()
    # reporter.transactions()
    reporter.HMRC("B", "2023 to 2024")
    reporter.HMRC("S", "2023 to 2024")


if __name__ == "__main__":
    main()
