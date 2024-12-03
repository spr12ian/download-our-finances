def get_credentials_path(file_name):
    import os

    file_path = f"~/{file_name}.json"

    return os.path.expanduser(file_path)


def get_spreadsheet_url(spreadsheet_id):
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
