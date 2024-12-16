from datetime import datetime


class DateColumns:
    def convert(self, df):
        for date_column in DateColumns().get_date_columns():
            if date_column in df.columns:
                try:
                    df[date_column] = df[date_column].apply(self.reverse_date_string)
                except:
                    print(date_column)
                    raise
        return df

    def get_date_columns(self):
        return [
            "As at",
            "CPTY date",
            "CPTY date 2",
            "Date",
            "Date 2",
            "Date of birth",
            "End date",
            "Fixed until",
            "Last updated",
            "Marriage date",
            "Start date",
        ]

    # Function to convert Google sheets date strings (DD-MM-YYYY) to Sqlite date strings YYYY-MM-DD
    def reverse_date_string(self, g_date_str):
        if g_date_str.strip() == "":  # Check if the string is empty or whitespace
            return ""

        # Convert the string to a datetime object
        date_obj = datetime.strptime(g_date_str, "%d/%m/%Y")

        # Convert the datetime object back to a string in the desired format
        return date_obj.strftime("%Y-%m-%d")
