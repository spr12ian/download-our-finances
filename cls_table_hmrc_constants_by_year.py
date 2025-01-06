from cls_sqlite_table import SQLiteTable
from utility_functions import string_to_float


class HMRC_ConstantsByYear(SQLiteTable):
    def __init__(self, tax_year):
        super().__init__("hmrc_constants_by_year")
        self.tax_year = tax_year

    def get_higher_rate_threshold(self):
        higher_rate_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("Higher rate threshold")
        )

        return higher_rate_threshold

    def get_marriage_allowance(self):
        marriage_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Marriage allowance")
        )

        return marriage_allowance

    def get_personal_allowance(self):
        personal_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Personal allowance")
        )
        return personal_allowance

    def get_personal_savings_allowance(self):
        personal_savings_allowance = string_to_float(
            self.__get_value_by_hmrc_constant(
                "Personal savings allowance for basic rate taxpayers"
            )
        )

        return personal_savings_allowance

    def get_property_income_allowance(self):
        property_income_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Property income allowance")
        )
        return property_income_allowance

    def get_savings_basic_rate(self):
        savings_basic_rate = string_to_float(
            self.__get_value_by_hmrc_constant("Savings basic rate")
        )

        return savings_basic_rate

    def get_starting_rate_limit_for_savings(self):
        starting_rate_limit_for_savings = string_to_float(
            self.__get_value_by_hmrc_constant("Starting rate limit for savings")
        )

        return starting_rate_limit_for_savings

    def get_trading_income_allowance(self):
        trading_income_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Trading income allowance")
        )
        return trading_income_allowance

    def __get_value_by_hmrc_constant(self, hmrc_constant):
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

        if result is None:
            raise ValueError(
                f"Could not find the HMRC constant '{hmrc_constant}' for tax year {tax_year}"
            )

        return result

    def get_vat_registration_threshold(self):
        vat_registration_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("VAT registration threshold")
        )

        return vat_registration_threshold
