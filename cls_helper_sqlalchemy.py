from cls_helper_config import ConfigHelper
from cls_helper_log import LogHelper
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import utility_functions as uf
import re

l = LogHelper(__file__)
#l.set_level_debug()
l.debug(__file__)


class SQLAlchemyHelper:
    def __init__(self):
        self.l = LogHelper("SQLAlchemyHelper")
        # self.l.set_level_debug()
        self.l.debug(__class__)

        config = ConfigHelper()

        db_filename = config.get("SQLite.database_name")
        file_path = Path(f"{db_filename}")
        if file_path.exists():
            self.l.debug(f"File '{file_path}' exists.")
        else:
            self.l.warning(f"File '{file_path}' does not exist.")

        url = f"sqlite:///{db_filename}"

        if self.l.is_debug_enabled():
            is_echo_enabled = True
        else:
            is_echo_enabled = False

        self.engine = create_engine(url, echo=is_echo_enabled)
        self.Session = sessionmaker(bind=self.engine)

    def fetch_one_value(self, query):
        query = text(query)

        # Open a session
        session = self.Session()
        try:
            # Execute the query
            result = session.execute(query)
            value = result.scalar()
        finally:
            # Close the session
            session.close()

        return value
    
    def get_db_filename(self):
        return self.engine.url.database

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


def valid_sqlalchemy_name(name):
    l.debug(f"valid_sqlalchemy_name")
    l.debug(f"name: {name}")
    valid_method_name = uf.to_valid_method_name(name)
    l.debug(f"valid_method_name: {valid_method_name}")
    return valid_method_name


def validate_sqlalchemy_name(name):
    if name != valid_sqlalchemy_name(name):
        raise ValueError(f"Invalid SQLAlchemy name: {name}")


def clean_column_names(df):

    df.columns = [valid_sqlalchemy_name(col) for col in df.columns]
    return df


# print(len(metadata.tables))
# for table in metadata.tables.values():
#     print(table.name)

#     if not table.primary_key.columns:
#         table.append_column(Column('id', Integer, primary_key=True))  # Add a primary key manually

#     for column in table.columns.values():
#         print(f'    {column.name}')


# def examine_model(model):
#     result = session.query(model).all()

#     # Print the actual data contained in the objects
#     for row in result:
#         print({column.name: getattr(row, column.name) for column in model.__table__.columns})


# model = Base.classes["account_balances"]
# examine_model(model)
