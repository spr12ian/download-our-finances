from cls_sqlite_table import SQLiteTable


class HMRC_Businesses(SQLiteTable):
    def __init__(self, business_name):
        super().__init__("hmrc_businesses")
        self.business_name = business_name

    def get_business_description(self):
        business_description = self.__get_value_by_business_name("Business description")

        return business_description

    def get_business_name(self):
        return self.business_name

    def get_business_postcode(self):
        business_description = self.__get_value_by_business_name("Business postcode")

        return business_description

    def __get_value_by_business_name(self, column_name):
        business_name = self.business_name
        query = (
            self.query_builder()
            .select(column_name)
            .where(f'"Business name" = "{business_name}"')
            .build()
        )

        result = self.sql.fetch_one_value(query)

        if result is None:
            raise ValueError(
                f"Could not find '{column_name}' for business {business_name}"
            )

        return result
