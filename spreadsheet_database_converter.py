import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import sqlite3

class SpreadsheetDatabaseConverter:
    def __init__(self, credentials_path, spreadsheet_name):
        """
        Initialize the converter with Google Sheets credentials and spreadsheet name
        
        Args:
            credentials_path (str): Path to your Google Cloud service account JSON
            spreadsheet_name (str): Name of the Google Spreadsheet
        """
        # Setup Google Sheets authentication
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        # Define the required scopes
        SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive.readonly'
        ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)
        

        # Python Our Finances URL
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1zss8pMXIT3REAbs7-CtlFm7GWSsmzK6Xt7F00hQseDw"

        # Open the spreadsheet
        self.spreadsheet = client.open_by_url(spreadsheet_url)
        
        # Local database connection
        self.db_connection = None
        self.db_path = 'converted_spreadsheet.db'
    
    def convert_to_sqlite(self):
        """
        Convert all sheets in the Google Spreadsheet to SQLite tables
        """
        # Create or connect to SQLite database
        self.db_connection = sqlite3.connect(self.db_path)
        
        # Iterate through all worksheets
        for worksheet in self.spreadsheet.worksheets():
            # Get worksheet data as a DataFrame
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            
            # Write DataFrame to SQLite table (sheet name becomes table name)
            table_name = worksheet.title.replace(' ', '_')
            df.to_sql(table_name, self.db_connection, if_exists='replace', index=False)
        
        print(f"Spreadsheet converted to SQLite database at {self.db_path}")
    
    def process_data(self):
        """
        Example data processing method. 
        Replace this with your specific data processing logic.
        """
        # Create a database cursor
        cursor = self.db_connection.cursor()
        
        # Example: Run a complex query
        cursor.execute("""
            SELECT * FROM your_sheet_name 
            WHERE some_column > 100 
            ORDER BY another_column
        """)
        
        # Convert results back to DataFrame for further processing
        processed_data = pd.DataFrame(cursor.fetchall())
        return processed_data
    
    def convert_to_spreadsheet(self, processed_data, new_sheet_name):
        """
        Convert processed data back to a Google Spreadsheet
        
        Args:
            processed_data (pd.DataFrame): Processed DataFrame to upload
            new_sheet_name (str): Name for the new Google Sheet
        """
        # Create a new worksheet in the existing spreadsheet
        new_worksheet = self.spreadsheet.add_worksheet(
            title=new_sheet_name, 
            rows=processed_data.shape[0], 
            cols=processed_data.shape[1]
        )
        
        # Update the worksheet with processed data
        new_worksheet.update([processed_data.columns.values.tolist()] + 
                              processed_data.values.tolist())
        
        print(f"Processed data uploaded to new sheet: {new_sheet_name}")
    
    def close_connection(self):
        """
        Close database connection
        """
        if self.db_connection:
            self.db_connection.close()

# Example usage
def main():
    # Replace with your actual paths and names
    converter = SpreadsheetDatabaseConverter(
        credentials_path=os.path.expanduser("~/isw-personal-scripts-314a6167bf08.json"), 
        spreadsheet_name='Python Our Finances'
    )
    
    # Convert spreadsheet to SQLite
    converter.convert_to_sqlite()
    
    try:
        # Process data (customize this method for your needs)
        processed_data = converter.process_data()
        
        # Convert processed data back to spreadsheet
        converter.convert_to_spreadsheet(processed_data, 'Processed Data')
    
    finally:
        # Always close the database connection
        converter.close_connection()

if __name__ == '__main__':
    main()