from utility_functions import string_to_financial
from cls_helper_log import LogHelper


class FinancialColumns:
    def __init__(self):
        self.l = LogHelper("FinancialColumns")
        self.l.set_level_debug()

    def convert(self, df):
        self.l.debug("convert")
        for financial_column in self.get_financial_columns():
            if financial_column in df.columns:
                try:
                    df[financial_column] = df[financial_column].apply(string_to_financial)                    
                    self.l.debug(f'df[financial_column].dtype: {df[financial_column].dtype}')                    
                    self.l.debug(f'df[financial_column].head: {df[financial_column].head}')                    
                    self.l.debug(f'df[financial_column].describe: {df[financial_column].describe}')
                except:
                    print(financial_column)
                    raise
        return df

    def get_financial_columns(self):
        return [
            "account_maximum",
            "account_minimum",
            "amount",
            "annual",
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
