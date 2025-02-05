from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Connect to your SQLite database
sqlite_file = 'our_finances.sqlite'
engine = create_engine(f'sqlite:///{sqlite_file}')

# Reflect the tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Automap base
Base = automap_base(metadata=metadata)
Base.prepare(autoload_with=engine)

# Create a session
session = Session(engine)

# Generate models
for table_name in metadata.tables.keys():
    try:
        print(table_name)
        model_class = getattr(Base.classes, table_name)
        print(f"Model for table '{table_name}':")
        for column in model_class.__table__.columns:
            print(f" - {column.name} ({column.type})")
    except KeyError:
        print(f"Table '{table_name}' not found in Base.classes")



