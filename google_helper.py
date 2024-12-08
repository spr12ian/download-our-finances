from config_helper import ConfigHelper
from google.oauth2.service_account import Credentials
import gspread
from os_helper import OsHelper

class GoogleHelper:
    def __init__(self):        
        config = ConfigHelper()

        # Google Cloud Service credentials
        self.credentials_file_name = config["Google"]["credentials_file_name"]

        self.spreadsheet_key = config["Google"]["source_spreadsheet_key"]
    
    def get_authorized_client(self, scopes):
        # from_service_account_file requires scopes to be passed as a keyword arguement

        credentials_path = self.get_credentials_path()

        creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
        client = gspread.authorize(creds)

        return client


    def get_credentials_path(self):
        home_directory=OsHelper().get_home_directory()

        return f"{home_directory}/{self.credentials_file_name}.json"


    def get_spreadsheet_url(self, spreadsheet_id):
        return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
    
    def get_spreadsheet(self, scopes):
        client = self.get_authorized_client(scopes)

        return client.open_by_key(self.spreadsheet_key)
