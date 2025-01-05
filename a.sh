#!/bin/bash

# List of databases
databases=("our_finances" "our_finances_orm")

# Loop through each database
for db in "${databases[@]}"; do
    db_filename="${db}.db"
    if [ -f "${db_filename}" ]; then
        echo rm "${db_filename}"
        rm "${db_filename}"
    fi

    text_only_db_filename="${db}_text_only.db"
    if [ -f "${text_only_db_filename}" ]; then
        echo rm "${text_only_db_filename}"
        rm "${text_only_db_filename}"
    fi
done

rm -fv ./*.log

./do_it_all.sh >do_it_all.log 2>do_it_all_error.log

# Check if the file exists and its size is zero
if [ -f "do_it_all_error.log" ] && [ ! -s "do_it_all_error.log" ]; then
    rm "do_it_all_error.log"
fi
