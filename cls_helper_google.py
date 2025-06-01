from cls_config import Config
from google.oauth2.service_account import Credentials  # type: ignore
import gspread
from cls_helper_os import OsHelper


class GoogleHelper:
    def __init__(self):
        self.read_config()

    def get_authorized_client(self, scopes):
        # from_service_account_file requires scopes to be passed as a keyword arguement

        # creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
        credentials = self.get_credentials(scopes)

        client = gspread.authorize(credentials)

        return client

    def get_credentials(self, scopes):
        service_account_file = self.get_credentials_path()
        credentials = Credentials.from_service_account_file(
            service_account_file, scopes=scopes
        )
        return credentials

    def get_credentials_path(self):
        home_directory = OsHelper().get_home_directory()

        credentials_path = f"{self.service_account_key_file}"

        return credentials_path

    def get_spreadsheet(self, scopes):
        client = self.get_authorized_client(scopes)
        spreadsheet = client.open_by_key(self.spreadsheet_key)

        return spreadsheet

    def get_spreadsheet_url(self, spreadsheet_id):
        return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"

    def read_config(self):
        config = Config()

        # Google Cloud Service credentials
        service_account_key_file = config.get("Google.service_account_key_file")
        if not service_account_key_file:
            raise ValueError(
                "Google.service_account_key_file is not set in the configuration."
            )
        if not service_account_key_file.endswith(".json"):
            raise ValueError("Google.Credentials must be a JSON file.")
        if not OsHelper().file_exists(service_account_key_file):
            raise FileNotFoundError(
                f"Credentials file '{service_account_key_file}' does not exist."
            )
        spreadsheet_key = config.get("Google.Sheets.spreadsheet_key")
        if not spreadsheet_key:
            raise ValueError(
                "Google.Sheets.spreadsheet_key is not set in the configuration."
            )

        self.service_account_key_file = service_account_key_file
        self.spreadsheet_key = spreadsheet_key
