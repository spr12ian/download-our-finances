from cls_helper_log import LogHelper

class BooleanColumns:
    def __init__(self):
        self.l = LogHelper("BooleanColumns")
        self.l.set_level_debug()

    def convert(self, df):
        self.l.debug("convert")
        for boolean_column in BooleanColumns().get_boolean_columns():
            if boolean_column in df.columns:
                try:
                    df[boolean_column] = df[boolean_column].apply(self.reverse_date_string)
                    self.l.debug(f'df[boolean_column].dtype: {df[boolean_column].dtype}')
                except:
                    print(boolean_column)
                    raise
        return df

    def convert_column(self, df, boolean_column):
        self.l.debug("convert_column")
        self.l.debug(f'boolean_column: {boolean_column}')
        try:
            df[boolean_column] = df[boolean_column].apply(self.boolean_string_to_int)
            self.l.debug(f'df[boolean_column].dtype: {df[boolean_column].dtype}')
        except:
            self.l.error(f'boolean_column: {boolean_column}')
            raise
        return df

    def get_boolean_columns(self):
        return []

    # Function to convert boolean strings to int
    def boolean_string_to_int(self, string)->int:
        if string.strip() == "":  # Check if the string is empty or whitespace
            return 0

        if string[:1].lower() in ['y','1']:
            return 1
        else:
            return 0
