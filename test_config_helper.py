import configparser
from cls_helper_config import ConfigHelper

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read('/home/probity/projects/download-our-finances/config.ini')

# Access nested keys
google_credentials_file_name = config['Google.Cloud']['credentials_file_name']
google_spreadsheet_source_key = config['Google.Sheets']['spreadsheet_key']
convert_underscore_tables = config['Google.Sheets'].getboolean('convert_underscore_tables')
sqlite_database_name = config['SQLite']['database_name']

# Print the values
print(f"Google Credentials File Name: {google_credentials_file_name}")
print(f"Google Spreadsheet Source Key: {google_spreadsheet_source_key}")
print(f"Convert Underscore Tables: {convert_underscore_tables}")
print(f"SQLite Database Name: {sqlite_database_name}")

coh = ConfigHelper()
print(coh['Google.Cloud']['credentials_file_name'])
print(coh['Google.Sheets']['spreadsheet_key'])
print(coh['Google.Sheets'].getboolean('convert_underscore_tables'))
print(coh['SQLite']['database_name'])

