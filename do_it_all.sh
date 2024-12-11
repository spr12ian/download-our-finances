#!/bin/bash
trap 'echo "Executing: $BASH_COMMAND"' DEBUG

pwl key_check

# List of databases 
databases=("our_finances" "our_finances_orm")

# Loop through each database 
for db in "${databases[@]}"
do
    db_filename="${db}.db"
    if [ -f "${db_filename}" ]; then
        rm "${db_filename}"
    fi

    pwl "spreadsheet_to_${db}"

    if [ -f "${db_filename}" ]; then
        text_only_db_filename="${db}_text_only.db"

        cp "${db_filename}" "${text_only_db_filename}"
        
        sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_text_only_tables.py"

        pwl "text_to_real_${db}"

        sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_tables.py"

        pwl vacuum_databases

        pwl "generate_reports_${db}"
    fi
done

trap - DEBUG
