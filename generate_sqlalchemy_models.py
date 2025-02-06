from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Float
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from utility_functions import to_camel_case

def add_comment(string):
    output_list.append(f"# {string}")

def add_line(string):
    output_list.append(f"{string}")

output_list=[
    "from sqlalchemy import Integer, String, Float",
    "from sqlalchemy.orm import DeclarativeBase, mapped_column",
    "",
    "class Base(DeclarativeBase):",
    "    pass",
    "",
]
# Connect to your SQLite database
sqlite_file = 'our_finances.sqlite'
engine = create_engine(f'sqlite:///{sqlite_file}')

# Reflect the tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Automap base
Base = automap_base(metadata=metadata)
Base.prepare(autoload_with=engine)

# Generate models
for table_name in metadata.tables.keys():
    try:
        add_comment(f"Model for table '{table_name}':")
        model_class = getattr(Base.classes, table_name)
        class_name=to_camel_case(table_name)
        add_line(f"class {class_name}(Base):")
        add_line(f"    __tablename__ = '{table_name}'")
        
        for column in model_class.__table__.columns:
            col_type = column.type
            if isinstance(col_type, Integer):
                col_type_str = "Integer"
            elif isinstance(col_type, String):
                col_type_str = "String"
            elif isinstance(col_type, Float):
                col_type_str = "Float"
            elif isinstance(col_type, Date):
                col_type_str = "Date"
            else:
                col_type_str = "String"  # Default to String for unknown types
            
            column_parts=[col_type_str]

            # Check if the column is a primary key
            if column.primary_key:
                column_parts.append("primary_key=True")

            if column.name=="id":
                column_parts.append("autoincrement=True")
            
            column_args=", ".join(column_parts)
            add_line(f"    {column.name} = mapped_column({column_args})")
        

        add_line("")
    except KeyError:
        print(f"Table '{table_name}' not found in Base.classes")

output="\n".join(output_list)
output_file="models.py"
with open(output_file, "w") as source:
    source.write(output)
            

