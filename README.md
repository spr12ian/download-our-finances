# download-our-finances
Python repository

SQLAlchemy tutorial
https://docs.sqlalchemy.org/en/20/tutorial/metadata.html

VS Code extensions:
Black Formatter by Microsoft

pwl is my own script to run Python With Logging

Test the Python connection to the Google spreadsheet
pwl key_check

All database fields are text to start with, except primary key id fields which are int
pwl spreadsheet_to_database

pwl vacuum our_finances.sqlite

sqlitebrowser our_finances.sqlite >sqlitebrowser.log 2>sqlitebrowser_error.log &

Prefer Numeric(10,2) over Float for financial data, map to Python as Decimal type
