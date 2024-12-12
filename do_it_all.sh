#!/bin/bash
trap 'echo "Executing: $BASH_COMMAND"' DEBUG

stop_if_module_has_errors() {
    module=$1
    echo "pwl ${module}"
    pwl "${module}"
    error_file="${module}_error.log"
    if [ -f "${error_file}" ]; then
        echo "Check ${error_file}"
        exit 1
    fi
}

stop_if_module_has_errors key_check

# List of databases
databases=("our_finances" "our_finances_orm")

# Loop through each database
for db in "${databases[@]}"; do
    db_filename="${db}.db"

    stop_if_module_has_errors "spreadsheet_to_${db}"

    if [ -f "${db_filename}" ]; then
        text_only_db_filename="${db}_text_only.db"

        echo cp "${db_filename}" "${text_only_db_filename}"
        cp "${db_filename}" "${text_only_db_filename}"

        echo sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_text_only_tables.py"
        sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_text_only_tables.py"

        stop_if_module_has_errors "text_to_real_${db}"

        echo sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_tables.py"
        sqlacodegen "sqlite:///${db_filename}" --outfile "${db}_tables.py"

        stop_if_module_has_errors vacuum_databases

        stop_if_module_has_errors "hmrc_reports_${db}"
    fi
done

trap - DEBUG
