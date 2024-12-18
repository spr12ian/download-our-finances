#!/bin/bash

# Check if DEBUG is set to true
if [ "$DEBUG" = "true" ]; then
    set -x # Enable debugging
else
    set +x # Disable debugging
fi

stop_if_module_has_errors() {
    module=$1
    echo "pwl ${module}"
    pwl "${module}"
    log_file="${module}.log"
    if [ -f "${log_file}" ]; then
        cat "${log_file}"
    fi
    error_file="${module}_error.log"
    if [ -f "${error_file}" ]; then
        echo "Check ${error_file}"
        exit 1
    fi
}

stop_if_module_has_errors key_check

# List of databases
databases=("our_finances")

# Loop through each database
for db in "${databases[@]}"; do
    db_filename="${db}.db"

    stop_if_module_has_errors "spreadsheet_to_${db}"

    if [ -f "${db_filename}" ]; then
        echo sqlacodegen_v2 "sqlite:///${db_filename}" --outfile "tables_sqlalchemy.py"
        sqlacodegen_v2 "sqlite:///${db_filename}" --outfile "tables_sqlalchemy.py"

        stop_if_module_has_errors "vacuum_${db}"

        stop_if_module_has_errors "hmrc_reports_${db}"
    fi
done
