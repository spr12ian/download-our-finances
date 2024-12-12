from tables import *
from cls_helper_sqlite import SQLiteHelper


class OurFinances:
    def __init__(self):
        print(__class__)

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
