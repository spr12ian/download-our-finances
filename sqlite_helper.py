import configparser
import sqlite3


class SQLiteHelper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        database_name = config["SQLite"]["database_name"]

        self.db_path = database_name + ".db"

    def close_connection(self):
        if self.db_connection:
            self.db_connection.close()

    def drop_column(self, table_name, column_to_drop):
        temp_table_name = f"temp_{table_name}"
        self.open_connection()

        cursor = self.db_connection.cursor()

        # Get the table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        # Extract column names excluding the column to drop
        column_names = [f'"{col[1]}"' for col in columns if col[1] != column_to_drop]
        column_names_str = ", ".join(column_names)

        # Create a temporary table without the column to drop
        sql_statement = f"CREATE TABLE {temp_table_name} AS SELECT {column_names_str} FROM {table_name}"
        print(sql_statement)
        cursor.execute(sql_statement)

        # Drop the original table
        sql_statement = f"DROP TABLE {table_name}"
        cursor.execute(sql_statement)

        # Rename the temporary table to the original table name
        sql_statement = f"ALTER TABLE {temp_table_name} RENAME TO {table_name}"
        cursor.execute(sql_statement)

        # Commit the changes and close the connection
        self.db_connection.commit()

        self.close_connection()

    def executeAndCommit(self, sql_statement):
        print(sql_statement)

        self.open_connection()

        cursor = self.db_connection.cursor()
        cursor.execute(sql_statement)
        self.db_connection.commit()

        self.close_connection()

    def fetch_all(self, query):
        print(query)

        self.open_connection()

        cursor = self.db_connection.cursor()
        cursor.execute(query)
        fetch_all = cursor.fetchall()

        self.close_connection()

        return fetch_all

    def fetch_one_row(self, query):
        self.open_connection()

        cursor = self.db_connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        self.close_connection()

        return row

    def fetch_one_value(self, query):
        row = self.fetch_one_row(query)
        if row:
            value = row[0]  # Accessing the first element of the tuple
        else:
            value = None  # In case no results are returned

        return value

    def get_column_info(self, table_name, column_name):
        table_info = self.get_table_info(table_name)
        column_info = None
        for column in table_info:
            if column[1] == column_name:
                column_info = column

        return column_info

    def get_how_many(self, table_name, where=None):
        self.open_connection()
        query = f"""
SELECT COUNT(*)
FROM {table_name}

"""

        if where:
            query += where

        how_many = self.fetch_one_value(query)

        self.close_connection()

        return how_many

    def get_table_info(self, table_name):
        query = f"PRAGMA table_info('{table_name}')"
        self.open_connection()

        cursor = self.db_connection.cursor()
        cursor.execute(query)
        table_info = cursor.fetchall()

        self.close_connection()

        return table_info

    def open_connection(self):
        # Connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)

    def rename_column(self, table_name, old_column_name, new_column_name):
        temp_table_name = f"temp_{table_name}"

        self.open_connection()

        cursor = self.db_connection.cursor()

        # Get the table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        # Create a list of column names with the renamed column

        new_column_phrase = f"{old_column_name} AS {new_column_name}"

        new_columns = [
            (f'"{col[1]}"' if col[1] != old_column_name else new_column_phrase)
            for col in columns
        ]
        new_columns_str = ", ".join(new_columns)
        old_columns_str = ", ".join([col[1] for col in columns])

        # Create a new table with the renamed column
        sql_statement = f"CREATE TABLE temp_{table_name} AS SELECT {new_columns_str} FROM {table_name}"
        print(sql_statement)
        cursor.execute(sql_statement)

        # Drop the original table
        sql_statement = f"DROP TABLE {table_name}"
        cursor.execute(sql_statement)

        # Rename the new table to the original table name
        sql_statement = f"ALTER TABLE temp_{table_name} RENAME TO {table_name}"
        cursor.execute(sql_statement)

        # Commit the changes and close the connection
        self.db_connection.commit()

        self.close_connection()

    def text_to_real(self, table_name, column_name):
        table_info = self.get_table_info(table_name)

        column_type = None

        for column in table_info:
            if column[1] == column_name:
                column_type = column[2]

        if column_type == "TEXT":
            sql_statements = [
                f"ALTER TABLE {table_name} ADD COLUMN {column_name}_real REAL",
                f"UPDATE {table_name} SET {column_name}_real = CAST(REPLACE(REPLACE(REPLACE({column_name}, '£', ''), ',', ''), ' ', '') AS REAL)",
            ]
            for sql_statement in sql_statements:
                self.executeAndCommit(sql_statement)

            self.drop_column(table_name, column_name)
            self.rename_column(table_name, f"{column_name}_real", column_name)


class SQLiteTable:
    def __init__(self, table_name):
        self.sql = SQLiteHelper()
        self.table_name = table_name

    def fetch_all(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.sql.fetch_all(query)

    def get_how_many(self):
        return self.sql.get_how_many(self.table_name)
