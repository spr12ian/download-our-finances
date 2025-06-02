from our_finances.classes.log_helper import LogHelper
from sqlalchemy_helper import valid_sqlalchemy_name
from cls_sqlite_table import SQLiteTable
from utility_functions import string_to_float
from functools import lru_cache


class HMRC_OverridesByYear(SQLiteTable):

    def __init__(self, person_code, tax_year) -> None:
        self.l = LogHelper("HMRC_OverridesByYear")
        self.l.set_level_debug()
        self.l.debug(__file__)
        self.l.debug(f"person_code: {person_code}")
        self.l.debug(f"tax_year: {tax_year}")
        super().__init__("hmrc_overrides_by_year")
        self.person_code = person_code
        self.tax_year = tax_year
        self.tax_year_col = valid_sqlalchemy_name(tax_year)

    def _get_value_by_override(self, override) -> str:
        self.l.debug("_get_value_by_override")
        person_code = self.person_code
        tax_year = self.tax_year
        tax_year_col = self.tax_year_col
        query = (
            self.query_builder()
            .select(tax_year_col)
            .where(f'"person_code" = "{person_code}" AND "override" = "{override}"')
            .build()
        )
        self.l.debug(query)
        result = self.sql.fetch_one_value(
            query
        )  # Could be formatted as a float, a ccy, etc.

        if result is None:
            raise ValueError(
                f"Could not find the override '{override}' for person {person_code}, tax year {tax_year}"
            )

        return result

    @lru_cache(maxsize=None)
    def deduct_trading_expenses(self) -> bool:
        deduct_trading_expenses = self._get_value_by_override(
            "Deduct trading expenses"
        )

        self.l.debug(f"deduct_trading_expenses: {deduct_trading_expenses}")

        return deduct_trading_expenses == "Yes"

    @lru_cache(maxsize=None)
    def use_trading_allowance(self) -> bool:
        self.l.debug("use_trading_allowance")
        try:
            value = self._get_value_by_override("Use trading allowance")
        except ValueError as e:
            self.l.error(f"ValueError: {e}")
            raise

        use_trading_allowance = value.lower() == "yes"

        self.l.debug(f"use_trading_allowance: {use_trading_allowance}")

        return use_trading_allowance
