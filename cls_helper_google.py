from cls_helper_config import ConfigHelper
from cls_helper_log import LogHelper
from google.oauth2.service_account import Credentials
import gspread
from cls_helper_os import OsHelper


class GoogleHelper:
    def __init__(self):
        # LogHelper.debug_enabled = True
        self.l = LogHelper(__name__)
        config = ConfigHelper()

        # Google Cloud Service credentials
        self.credentials_file_name = config["Google"]["credentials_file_name"]

        self.spreadsheet_key = config["Google"]["source_spreadsheet_key"]

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
        self.l.debug(f"credentials.default_scopes: {credentials.default_scopes}")
        self.l.debug(f"credentials.expired: {credentials.expired}")
        self.l.debug(f"credentials.project_id: {credentials.project_id}")
        self.l.debug(f"credentials.quota_project_id: {credentials.quota_project_id}")
        self.l.debug(
            f"credentials.service_account_email: {credentials.service_account_email}"
        )
        self.l.debug(f"credentials.valid: {credentials.valid}")
        return credentials

    def get_credentials_path(self):
        home_directory = OsHelper().get_home_directory()

        credentials_path = f"{home_directory}/{self.credentials_file_name}.json"
        self.l.debug(f"credentials_path: {credentials_path}")
        return credentials_path

    def get_spreadsheet_url(self, spreadsheet_id):
        return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"

    def get_spreadsheet(self, scopes):
        self.l.debug(f"scopes: {scopes}")
        client = self.get_authorized_client(scopes)
        spreadsheet = client.open_by_key(self.spreadsheet_key)
        self.l.debug(f"spreadsheet.title: {spreadsheet.title}")

        return spreadsheet
