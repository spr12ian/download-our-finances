import database_to_spreadsheet
import key_check
import pytest
import spreadsheet_to_database


def f():
    raise SystemExit(1)

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_database_to_spreadsheet():
    database_to_spreadsheet.main()

def test_key_check():
    key_check.main()

def test_mytest():
    with pytest.raises(SystemExit):
        f()

def test_one():
    x = "this"
    assert "h" in x

def test_spreadsheet_to_database():
    spreadsheet_to_database.main()

def test_two():
    x = "hello"
    assert hasattr(x, "check")
