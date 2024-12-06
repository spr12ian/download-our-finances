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
        self.sql=sqlite_helper.SQLiteHelper(self.db_path)

    def account_balances(self):
        query = """
            SELECT Key, Balance 
            FROM account_balances
            WHERE Balance NOT BETWEEN -1 AND 1
        """

        for row in self.sql.fetch_all(query):
            print(row)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def account_owners(self):
        query = """
            SELECT * 
            FROM account_owners
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

    reporter.account_balances()
    reporter.account_owners()
    reporter.transactions()


if __name__ == "__main__":
    main()
