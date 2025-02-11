import pandas as pd
from cls_helper_log import LogHelper


class PandasHelper:
    def __init__(self):
        self.l = LogHelper("PandasHelper")
        #self.l.set_level_debug()

    def pd(self):
        return pd

    def header_to_dataframe(self, values):
        self.l.debug("values_to_dataframe")
        # Create a DataFrame
        columns = values
        return pd.DataFrame(columns=columns)

    def infer_dtype(self, series):        
        return pd.api.types.infer_dtype(series)

    def worksheet_values_to_dataframe(self, worksheet_values):
        self.l.debug("worksheet_values_to_dataframe")
        # Create a DataFrame
        columns = worksheet_values[0]  # Assume the first row contains headers
        rows = worksheet_values[1:]  # Remaining rows are the data
        return pd.DataFrame(rows, columns=columns)
