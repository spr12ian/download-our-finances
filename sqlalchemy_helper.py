from config_helper import ConfigHelper
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class SQLAlchemyHelper:
    def __init__(self):
        config = ConfigHelper()

        self.db_path = config["SQLite"]["database_name"] + ".db"

        self.db_connection = None

    def get_session(self):
        url = f"sqlite:///{self.db_path}"

        engine = create_engine(url, echo=True)

        return Session(engine)
