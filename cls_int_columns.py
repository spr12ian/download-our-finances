import re


class IntColumns:
    def convert(self, df):
        for int_column in self.get_int_columns():
            if int_column in df.columns:
                try:
                    df[int_column] = df[int_column].apply(self.string_to_int)
                except:
                    print(int_column)
                    raise
        return df

    def get_int_columns(self):
        return [
            "Order by",
        ]

    # Function to convert number strings to int
    def string_to_int(self, string):
        if string.strip() == "":  # Check if the string is empty or whitespace
            return 0

        # Remove any currency symbol (£), commas, and percent then convert to int
        return int(re.sub(r"[£,%]", "", string))
