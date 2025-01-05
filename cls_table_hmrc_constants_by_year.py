from cls_sqlite_table import SQLiteTable
from utility_functions import string_to_float


class HMRC_ConstantsByYear(SQLiteTable):
    def __init__(self, tax_year):
        super().__init__("hmrc_constants_by_year")
        self.tax_year = tax_year

    def get_property_income_allowance(self):
        property_income_allowance = string_to_float(
            self.get_value_by_hmrc_constant("Property income allowance")
        )
        return property_income_allowance

    def get_trading_income_allowance(self):
        trading_income_allowance = string_to_float(
            self.get_value_by_hmrc_constant("Trading income allowance")
        )
        return trading_income_allowance

    def get_value_by_hmrc_constant(self, hmrc_constant):
        tax_year = self.tax_year
        query = (
            self.query_builder()
            .select(tax_year)
            .where(f'"HMRC constant" = "{hmrc_constant}"')
            .build()
        )
        result = self.sql.fetch_one_value(
            query
        )  # Could be formatted as a float, a ccy, etc.

        return result
