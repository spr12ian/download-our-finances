from cls_helper_config import ConfigHelper

config = ConfigHelper()

# Accessing values
print("Credentials:", config.get("Google.Cloud.credentials_file_name"))
print("Spreadsheet Key:", config.get("Google.Sheets.spreadsheet_key"))
print("Convert Tables:", config.get("Google.Sheets.convert_underscore_tables"))
print("SQLite DB:", config.get("SQLite.database_name"))
