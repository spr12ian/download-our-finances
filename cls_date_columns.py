from cls_helper_date_time import DateTimeHelper


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

    # Function to convert Google sheets date strings (DD/MM/YYYY) to Sqlite date strings YYYY-MM-DD
    def reverse_date_string(self, g_date_str):
        return DateTimeHelper().UK_to_ISO(g_date_str)
