from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

databases = [
    "our_finances",
    "our_finances_orm",
    "our_finances_text_only",
    "our_finances_orm_text_only",
]

for database in databases:
    # Define your database URL
    db_url = f"sqlite:///{database}.db"

    # Create an engine
    engine = create_engine(db_url, echo=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Execute VACUUM command
    session.execute("VACUUM;")
    session.commit()

    # Close the session
    session.close()
