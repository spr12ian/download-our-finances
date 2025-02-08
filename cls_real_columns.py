from utility_functions import string_to_float


class RealColumns:
    def convert(self, df):
        for real_column in self.get_real_columns():
            if real_column in df.columns:
                try:
                    df[real_column] = df[real_column].apply(string_to_float)
                except:
                    print(real_column)
                    raise
        return df

    def get_real_columns(self):
        return [
            "annual_interest__aer_",
            "interest_rate",
        ]
