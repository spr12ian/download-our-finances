from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

databases = [
    "our_finances_orm",
]

for database in databases:
    db_filename = f"{database}.sqlite"
    file_path = Path(f"{db_filename}")
    if file_path.exists():
        print(f"File '{file_path}' exists.")
    else:
        print(f"File '{file_path}' does not exist.")
        continue

    # Define your database URL
    db_url = f"sqlite:///{database}.db"

    # Create an engine
    engine = create_engine(db_url, echo=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    vacuum_statement = text("VACUUM;")

    # Execute VACUUM command
    session.execute(vacuum_statement)
    session.commit()

    # Close the session
    session.close()
