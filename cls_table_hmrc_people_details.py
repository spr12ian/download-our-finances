from cls_helper_date_time import DateTimeHelper
from cls_sqlite_table import SQLiteTable


class HMRC_PeopleDetails(SQLiteTable):
    def __init__(self, code=None):
        super().__init__("hmrc_people_details")
        self.code = code

    def fetch_by_code(self, code):
        query = self.query_builder().where(f"Code = '{code}'").build()
        return self.sql.fetch_all(query)

    def get_marital_status(self):
        return self.get_value_by_code_column("Marital status")

    def get_marriage_date(self):
        return self.get_value_by_code_column("Marriage date")

    def get_national_insurance_number(self):
        return self.get_value_by_code_column("NINO")

    def get_receive_child_benefit(self):
        return self.get_value_by_code_column("Receive child benefit")

    def get_refunds_to(self):
        return self.get_value_by_code_column("Refunds to")

    def get_spouse_code(self):
        return self.get_value_by_code_column("Spouse code")

    def get_taxpayer_residency_status(self):
        return self.get_value_by_code_column("Taxpayer residency status")

    def get_uk_marriage_date(self):
        marriage_date = self.get_marriage_date()
        if marriage_date is None:
            return None
        else:
            return DateTimeHelper().ISO_to_UK(self.get_marriage_date())

    def get_unique_tax_reference(self):
        return self.get_value_by_code_column("UTR")

    def get_utr_check_digit(self) -> str:
        utr_check_digit = self.get_value_by_code_column("UTR check digit")
        if not utr_check_digit:
            utr_check_digit = ""
        return utr_check_digit

    def get_value_by_code_column(self, column_name):
        if self.code:
            query = (
                self.query_builder()
                .select(column_name)
                .where(f'"Code" = "{self.code}"')
                .build()
            )
            result = str(self.sql.fetch_one_value(query))
        else:
            result = None

        return result
