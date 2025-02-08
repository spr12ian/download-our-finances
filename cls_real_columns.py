from utility_functions import string_to_float
from cls_helper_log import LogHelper


class RealColumns:
    def __init__(self):
        self.l = LogHelper("RealColumns")
        self.l.set_level_debug()

    def convert(self, df):
        self.l.debug("convert")
        for real_column in self.get_real_columns():
            if real_column in df.columns:
                try:
                    df[real_column] = df[real_column].apply(string_to_float)
                    self.l.debug(f'df[real_column].dtype: {df[real_column].dtype}')
                except:
                    print(real_column)
                    raise
        return df

    def get_real_columns(self):
        return [
            "annual_interest__aer_",
            "interest_rate",
        ]
