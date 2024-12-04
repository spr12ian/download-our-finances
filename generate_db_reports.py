import configparser
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import sqlite3
import time
import google_helpers


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

    def first_report(self):
        """
        Example data reporting method.
        """
        self.open_db_connection()

        query = """
            SELECT * FROM 'Account_owners'
        """
        # Create a database cursor
        cursor = self.db_connection.cursor()

        # Example: Run a complex query
        cursor.execute(query)

        # Convert results back to DataFrame for further processing
        dataframe = pd.DataFrame(cursor.fetchall())

        self.close_db_connection()
        return dataframe

    def open_db_connection(self):
        # Connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)

    def close_db_connection(self):
        """
        Close database connection
        """
        if self.db_connection:
            self.db_connection.close()


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    database_name = config["SQLite"]["database_name"]

    reporter = Generate_DB_Reports(database_name)

    try:
        dataframe = reporter.first_report()
        print(dataframe)

    finally:
        # Always close the database connection
        reporter.close_db_connection()


if __name__ == "__main__":
    main()
