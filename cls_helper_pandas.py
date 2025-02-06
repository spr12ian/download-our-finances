import pandas as pd
from sqlalchemy import Integer


class PandasHelper:
    def worksheet_values_to_dataframe(self, worksheet_values):
        # Create a DataFrame
        columns = worksheet_values[0]  # Assume the first row contains headers
        rows = worksheet_values[1:]  # Remaining rows are the data
        return pd.DataFrame(rows, columns=columns)
