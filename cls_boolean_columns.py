from cls_helper_log import LogHelper


class BooleanColumns:
    true_values = ["y", "yes", "1", "true"]
    false_values = ["n", "no", "0", "false"]

    def __init__(self):
        self.l = LogHelper("BooleanColumns")
        self.l.set_level_debug()

    def convert(self, df):
        self.l.debug("convert")
        for boolean_column in self.get_boolean_columns():
            if boolean_column in df.columns:
                try:
                    df[boolean_column] = df[boolean_column].apply(
                        self.boolean_string_to_int
                    )
                    self.l.debug(
                        f"df[boolean_column].dtype: {df[boolean_column].dtype}"
                    )
                except Exception as e:
                    self.l.error(f"Error processing column {boolean_column}: {e}")
                    raise
        return df

    def convert_column(self, df, boolean_column):
        self.l.debug("convert_column")
        self.l.debug(f"boolean_column: {boolean_column}")
        try:
            df[boolean_column] = df[boolean_column].apply(self.boolean_string_to_int)
            self.l.debug(f"df[boolean_column].dtype: {df[boolean_column].dtype}")
        except:
            self.l.error(f"boolean_column: {boolean_column}")
            raise
        return df

    def get_boolean_columns(self) -> list:
        return []

    # Function to convert boolean strings to int
    def boolean_string_to_int(self, string: str) -> int:
        if not isinstance(string, str):
            raise TypeError(f"{string} has unexpected type: {type(string)}")

        string = string.strip()

        if string == "":
            return 0  # Default to 0 --> false for empty values

        boolean_value = string.lower()
        if boolean_value in BooleanColumns.true_values:
            return 1
        elif boolean_value in BooleanColumns.false_values:
            return 0
        else:
            raise ValueError(f"Unexpected boolean value: {string}")
