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

    def HMRC(self, owner_code, tax_year):
        query = f"""
            SELECT "Name", "Date of birth", "Phone number", "National insurance number"
            FROM people
            WHERE "Code" = '{owner_code}'
        """

        row = self.sql.fetch_one_row(query)
        person_name = row[0]
        date_of_birth = row[1]
        phone_number = row[2]
        national_insurance_number = row[3]

        print(f"HMRC {tax_year} tax return for {person_name}")
        print("Page TR 1")
        print(f"1 Your date of birth: {date_of_birth}")
        print(f"3 Your phone number: {phone_number}")
        print(f"4 Your National Insurance number: {national_insurance_number}")
        print("Page TR 2")

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
        print(query)

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
        print(query)

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

        print("Page TR 3")
        question_number = 1
        question = "Taxed UK interest: "
        answer = f"{question_number} {question}"
        print(answer)

        question_number += 1
        question = "Untaxed UK interest: "
        answer = f"{question_number} {question}"

        query = f"""
            SELECT SUM(Nett) 
            FROM transactions
            WHERE Key <> ''
            AND "Tax year" = '{tax_year}'
            AND Category = 'HMRC {owner_code} interest'
        """
        print(query)
        amount = self.sql.fetch_one_value(query)
        print(amount)
        # answer += f"£{amount:,.2f}"
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
