import re


class RealColumns:
    def convert(self, df):
        for real_column in RealColumns().get_real_columns():
            if real_column in df.columns:
                try:
                    df[real_column] = df[real_column].apply(self.string_to_float)
                except:
                    print(real_column)
                    raise
        return df

    def get_real_columns(self):
        return [
            "Account maximum",
            "Account minimum",
            "Amount",
            "Annual",
            "Annual interest (AER)",
            "Asset value",
            "Balance",
            "Change",
            "Change required",
            "Credit",
            "Credits due",
            "Daily",
            "Debit",
            "Debits due",
            "Dynamic amount",
            "Excess",
            "Fixed amount",
            "Four weekly",
            "Interest",
            "Interest rate",
            "Minimum today",
            "Monthly",
            "Monthly interest",
            "Nett",
            "Shortfall",
            "Sporadic",
            "Taxable interest",
            "Tolerance",
            "Total credit",
            "Total debit",
            "Weekly",
        ]

    # Function to convert currency strings to float
    def string_to_float(self, string):
        if string.strip() == "":  # Check if the string is empty or whitespace
            return 0.0

        # Remove the currency symbol (£), commas, and percent then convert to float
        return float(re.sub(r"[£,%]", "", string))
