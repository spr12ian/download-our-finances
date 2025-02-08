import re
from cls_helper_log import LogHelper

class IntColumns:
    def __init__(self):
        self.l = LogHelper("IntColumns")
        self.l.set_level_debug()

    def convert(self, df):
        self.l.debug("convert")
        for int_column in self.get_int_columns():
            if int_column in df.columns:
                try:
                    df[int_column] = df[int_column].apply(self.string_to_int)
                    self.l.debug(f'df[int_column].dtype: {df[int_column].dtype}')
                except:
                    print(int_column)
                    raise
        return df

    def get_int_columns(self):
        return [
            "online_order",
            "order_by",
            "printed_order",
        ]

    # Function to convert number strings to int
    def string_to_int(self, string):
        if string.strip() == "":  # Check if the string is empty or whitespace
            return 0

        # Remove any currency symbol (£), commas, and percent then convert to int
        return int(re.sub(r"[£,%]", "", string))
