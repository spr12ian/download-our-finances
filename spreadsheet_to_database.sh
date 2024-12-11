#!/bin/bash

if [ -f our_finances.db ]; then
    rm our_finances.db
fi

pwl spreadsheet_to_database

cp our_finances.db our_finances_text.db

pwl text_to_real

pwl generate_db_reports

sqlacodegen "sqlite:///our_finances_text.db" --outfile our_finances_text.py

sqlacodegen "sqlite:///our_finances.db" --outfile our_finances.py

diff our_finances.py alchemy_models.py >our_finances_text.log
