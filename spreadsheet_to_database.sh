#!/bin/bash

pwl spreadsheet_to_database

if [ -f initial_models.py ]; then
    rm initial_models.py
fi

sqlacodegen "sqlite:///our_finances.db" --outfile initial_models.py

pwl text_to_real

pwl generate_db_reports
