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
            "account_maximum",
            "account_minimum",
            "amount",
            "annual",
            "annual_interest__aer_",
            "asset_value",
            "balance",
            "change",
            "change_required",
            "credit",
            "credits_due",
            "daily",
            "debit",
            "debits_due",
            "dynamic_amount",
            "excess",
            "fixed_amount",
            "four_weekly",
            "interest",
            "interest_rate",
            "minimum_today",
            "monthly",
            "monthly_interest",
            "nett",
            "shortfall",
            "sporadic",
            "taxable_interest",
            "tolerance",
            "total_credit",
            "total_debit",
            "total_nett",
            "weekly",
            "weekly_state_pension_forecast",
        ]
