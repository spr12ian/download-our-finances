import re
from cls_helper_log import LogHelper
from cls_helper_decimal import DecimalHelper
import utility_functions as uf


class DecimalColumns:
    def __init__(self, decimal_places=None):
        self.l = LogHelper("DecimalColumns")
        self.l.set_level_debug()
        self.l.debug(f'decimal_places: {decimal_places}')
        self.decimal_places = decimal_places

    def convert(self, df):
        self.l.debug("convert")
        for decimal_column in self.get_decimal_columns():
            if decimal_column in df.columns:
                try:
                    df[decimal_column] = df[decimal_column].apply(
                        self.string_to_decimal
                    )
                    self.l.debug(
                        f"df[decimal_column].dtype: {df[decimal_column].dtype}"
                    )
                except:
                    print(decimal_column)
                    raise
        return df

    def convert_column(self, df, decimal_column):
        self.l.debug("convert_column")
        self.l.debug(f'decimal_column: {decimal_column}')
        try:
            df[decimal_column] = df[decimal_column].apply(self.string_to_decimal)
            self.l.debug(f'df[decimal_column].dtype: {df[decimal_column].dtype}')
        except:
            self.l.error(f'decimal_column: {decimal_column}')
            raise
        return df
    
    def get_decimal_columns(self):
        return [
            "online_order",
            "order_by",
            "printed_order",
        ]

    # Function to convert number strings to decimal
    def string_to_decimal(self, string):
        self.l.debug("string_to_decimal")
        self.l.debug(f'string: {string}')
        string=uf.remove_non_numeric(string)
        if string.strip() == "":  # Check if the string is empty or whitespace
            return DecimalHelper(2).get_decimal("0")

        
        decimal = DecimalHelper(2).get_decimal(string)
        self.l.debug(f'decimal: {decimal}')
        
        return decimal
