from cls_helper_log import LogHelper
from cls_sqlite_table import SQLiteTable
from utility_functions import string_to_float


class HMRC_ConstantsByYear(SQLiteTable):

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

    def __init__(self, tax_year):
        self.l = LogHelper("HMRC_ConstantsByYear")
        self.l.set_level_debug()
        self.l.debug(__file__)
        self.l.debug(f"tax_year: {tax_year}")
        super().__init__("hmrc_constants_by_year")
        self.tax_year = tax_year

    def get_additional_rate_threshold(self) -> float:
        additional_rate_threshold = self.__get_value_by_hmrc_constant(
            "Additional rate threshold"
        )

        self.l.debug(f"additional_rate_threshold: {additional_rate_threshold}")

        if additional_rate_threshold == "Infinity":
            additional_rate_threshold = float("inf")
        else:
            raise ValueError(
                f'Unexpected additional_rate_threshold: "{additional_rate_threshold}"'
            )

        return additional_rate_threshold

    def get_additional_tax_rate(self) -> float:
        additional_tax_rate = string_to_float(
            self.__get_value_by_hmrc_constant("Additional tax rate")
        )

        self.l.debug(f"additional_tax_rate: {additional_tax_rate}")

        return additional_tax_rate

    def get_basic_rate_threshold(self) -> float:
        basic_rate_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("Basic rate threshold")
        )

        self.l.debug(f"basic_rate_threshold: {basic_rate_threshold}")

        return basic_rate_threshold

    def get_basic_tax_rate(self) -> float:
        basic_tax_rate = string_to_float(
            self.__get_value_by_hmrc_constant("Basic tax rate")
        )

        self.l.debug(f"basic_tax_rate: {basic_tax_rate}")

        return basic_tax_rate

    def get_class_2_weekly_rate(self) -> float:
        class_2_nics_weekly_rate = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 2 weekly rate")
        )

        self.l.debug(f"class_2_nics_weekly_rate: {class_2_nics_weekly_rate}")

        return class_2_nics_weekly_rate

    def get_class_4_lower_profits_limit(self) -> float:
        class_4_lower_profits_limit = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 4 lower profits limit")
        )

        self.l.debug(f"class_4_lower_profits_limit: {class_4_lower_profits_limit}")

        return class_4_lower_profits_limit

    def get_class_4_lower_rate(self) -> float:
        class_4_nics_lower_rate = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 4 lower rate")
        )

        self.l.debug(f"class_4_nics_lower_rate: {class_4_nics_lower_rate}")

        return class_4_nics_lower_rate

    def get_class_4_upper_profits_limit(self) -> float:
        class_4_upper_profits_limit = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 4 upper profits limit")
        )

        self.l.debug(f"class_4_upper_profits_limit: {class_4_upper_profits_limit}")

        return class_4_upper_profits_limit

    def get_class_4_upper_rate(self) -> float:
        class_4_nics_upper_rate = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 4 upper rate")
        )

        self.l.debug(f"class_4_nics_upper_rate: {class_4_nics_upper_rate}")

        return class_4_nics_upper_rate

    def get_higher_rate_threshold(self) -> float:
        higher_rate_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("Higher rate threshold")
        )

        self.l.debug(f"higher_rate_threshold: {higher_rate_threshold}")

        return higher_rate_threshold

    def get_higher_tax_rate(self) -> float:
        higher_tax_rate = string_to_float(
            self.__get_value_by_hmrc_constant("Higher tax rate")
        )

        self.l.debug(f"higher_tax_rate: {higher_tax_rate}")

        return higher_tax_rate

    def get_marriage_allowance(self) -> float:
        marriage_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Marriage allowance")
        )

        self.l.debug(f"marriage_allowance: {marriage_allowance}")

        return marriage_allowance

    def how_many_nic_weeks_in_year(self) -> float:
        nic_weeks_in_year = string_to_float(
            self.__get_value_by_hmrc_constant("NIC weeks in year")
        )

        self.l.debug(f"nic_weeks_in_year: {nic_weeks_in_year}")

        return nic_weeks_in_year

    def get_personal_allowance(self) -> float:
        personal_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Personal allowance")
        )

        self.l.debug(f"personal_allowance: {personal_allowance}")

        return personal_allowance

    def get_personal_savings_allowance(self) -> float:
        personal_savings_allowance = string_to_float(
            self.__get_value_by_hmrc_constant(
                "Personal savings allowance for basic rate taxpayers"
            )
        )

        self.l.debug(f"personal_savings_allowance: {personal_savings_allowance}")

        return personal_savings_allowance

    def get_property_income_allowance(self) -> float:
        property_income_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Property income allowance")
        )

        self.l.debug(f"property_income_allowance: {property_income_allowance}")

        return property_income_allowance

    def get_savings_basic_rate(self):
        savings_basic_rate = string_to_float(
            self.__get_value_by_hmrc_constant("Savings basic rate")
        )

        self.l.debug(f"savings_basic_rate: {savings_basic_rate}")

        return savings_basic_rate

    def get_small_profits_threshold(self):
        small_profits_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("NIC Class 2 small profits threshold")
        )

        self.l.debug(f"small_profits_threshold: {small_profits_threshold}")

        return small_profits_threshold

    def get_starting_rate_limit_for_savings(self):
        starting_rate_limit_for_savings = string_to_float(
            self.__get_value_by_hmrc_constant("Starting rate limit for savings")
        )

        self.l.debug(
            f"starting_rate_limit_for_savings: {starting_rate_limit_for_savings}"
        )

        return starting_rate_limit_for_savings

    def get_trading_income_allowance(self):
        trading_income_allowance = string_to_float(
            self.__get_value_by_hmrc_constant("Trading income allowance")
        )

        self.l.debug(f"trading_income_allowance: {trading_income_allowance}")

        return trading_income_allowance

    def get_vat_registration_threshold(self):
        vat_registration_threshold = string_to_float(
            self.__get_value_by_hmrc_constant("VAT registration threshold")
        )

        self.l.debug(f"vat_registration_threshold: {vat_registration_threshold}")

        return vat_registration_threshold
