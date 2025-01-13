from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from cls_helper_sqlalchemy import SQLAlchemyHelper
from cls_helper_log import LogHelper
from cls_helper_log import debug_function_call


l = LogHelper(__file__)
# l.set_level_debug()
l.debug(__file__)


@debug_function_call
def main():
    alchemy = SQLAlchemyHelper()

    vacuum_statement = text("VACUUM;")

    session = alchemy.get_session()

    try:
        # Execute VACUUM command
        session.execute(vacuum_statement)
        session.commit()
    except Exception as e:
        l.error(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()

    l.print("Database has been vacuumed")


if __name__ == "__main__":
    main()
