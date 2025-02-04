import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Connect to your SQLite database
sqlite_file = 'our_finances.sqlite'
engine = create_engine(f'sqlite:///{sqlite_file}')

# Reflect the tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Rename columns with spaces
for table in metadata.tables.values():
    for column in table.columns.values():
        if ' ' in column.name:
            column.name = column.name.replace(' ', '_')

# Automap base
Base = automap_base(metadata=metadata)
Base.prepare()

# Create a session
session = Session(engine)

for table_name in metadata.tables.keys():
    try:
        model_class = getattr(Base.classes, table_name)
        print(f"Model for table '{table_name}':")
        for column in model_class.__table__.columns:
            print(f" - {column.name} ({column.type})")
    except KeyError:
        print(f"Table '{table_name}' not found in Base.classes")

# Print all available table names in Base.classes
print("Available tables in Base.classes:")
for table_name in Base.classes.keys():
    print(f" - {table_name}")

# Example usage
# Your models are now accessible via Base.classes.<table_name>
example_model = Base.classes.example_table
result = session.query(example_model).all()
print(result)

# Generate models
for table_name in metadata.tables.keys():
    model_class = getattr(Base.classes, table_name)
    print(f"Model for table '{table_name}':")
    for column in model_class.__table__.columns:
        print(f" - {column.name} ({column.type})")

# Example usage
# Your models are now accessible via Base.classes.<table_name>
example_model = Base.classes.example_table
result = session.query(example_model).all()
print(result)
