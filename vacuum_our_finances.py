from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from cls_helper_sqlalchemy import SQLAlchemyHelper
from cls_helper_log import LogHelper
from cls_helper_log import debug_function_call
import os

l = LogHelper(__file__)
# l.set_level_debug()
l.debug(__file__)

def get_file_size(file_path):
    return os.path.getsize(file_path)

@debug_function_call
def vacuum_database(db_file_path):
    alchemy = SQLAlchemyHelper()

    vacuum_statement = text("VACUUM;")

    session = alchemy.get_session()

    try:
        # Print the size of the database file before vacuuming
        before_size = get_file_size(db_file_path)
        print(f"Database size before vacuuming: {before_size} bytes")

        # Execute VACUUM command
        session.execute(vacuum_statement)
        session.commit()

        # Print the size of the database file after vacuuming
        after_size = get_file_size(db_file_path)
        print(f"Database size after vacuuming: {after_size} bytes")
    
    except Exception as e:
        l.error(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()

    l.print("Database has been vacuumed")


if __name__ == "__main__":
    db_file_path="our_finances.sqlite"
    vacuum_database(db_file_path)
