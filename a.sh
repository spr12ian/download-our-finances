#!/bin/bash


db_filename="our_finances.sqlite"
if [ -f "${db_filename}" ]; then
    echo rm "${db_filename}"
    rm "${db_filename}"
fi


rm -fv ./*.log

./do_it_all.sh >do_it_all.log 2>do_it_all_error.log

# Check if the file exists and its size is zero
if [ -f "do_it_all_error.log" ] && [ ! -s "do_it_all_error.log" ]; then
    rm "do_it_all_error.log"
fi
