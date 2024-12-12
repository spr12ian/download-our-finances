from cls_helper_config import ConfigHelper
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class SQLAlchemyHelper:
    def __init__(self):
        config = ConfigHelper()

        db_filename = config["SQLAlchemy"]["database_name"] + ".db"

        url = f"sqlite:///{db_filename}"

        self.engine = create_engine(url, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return Session(self.engine)

    def get_table_info(self, table_name):
        query = text(f"PRAGMA table_info('{table_name}')")

        # Open a session
        session = self.Session()
        try:
            # Execute the query
            result = session.execute(query)
            table_info = result.fetchall()
        finally:
            # Close the session
            session.close()

        return table_info

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
