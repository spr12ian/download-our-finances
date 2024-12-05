import configparser
import pandas as pd
import sqlite_helpers


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

    def account_owners(self):
        query = """
            SELECT * 
            FROM 'Account_owners'
        """

        dataframe = self.report(query)

        return dataframe

    def account_balances(self):
        query = """
            UPDATE 'Account_balances'
            SET Balance = printf('%.2f', CAST(Balance AS REAL))
        """
        self.executeQuery(query)

        query = """
            SELECT Key, Balance 
            FROM 'Account_balances'
        """

        dataframe = self.report(query)

        return dataframe

    def executeQuery(self, query):
        """
        Data reporting method.
        """
        print(query)

        db_connection = sqlite_helpers.open_connection(self.db_path)

        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()

        sqlite_helpers.close_connection(db_connection)

    def report(self, query):
        """
        Data reporting method.
        """
        print(query)

        db_connection = sqlite_helpers.open_connection(self.db_path)

        dataframe = pd.read_sql(query, db_connection)

        sqlite_helpers.close_connection(db_connection)

        print(dataframe.describe())

        print(dataframe.info())

        print(dataframe)

        return dataframe


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    database_name = config["SQLite"]["database_name"]

    reporter = Generate_DB_Reports(database_name)

    dataframe = reporter.account_owners()
    dataframe = reporter.account_balances()


if __name__ == "__main__":
    main()
