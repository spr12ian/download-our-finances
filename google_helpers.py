from google.oauth2.service_account import Credentials
import gspread


def get_authorized_client(credentials_path, scopes):
    """
    Get client using credentials

    Args:
        credentials_path (str): Path to your Google Cloud service account JSON
        scopes (array): Google auth scopes
    """

    # from_service_account_file requires scopes to be passed as a keyword arguement
    creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
    client = gspread.authorize(creds)

    return client


def get_credentials_path(file_name):
    import os

    file_path = f"~/{file_name}.json"

    return os.path.expanduser(file_path)


def get_spreadsheet_url(spreadsheet_id):
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
