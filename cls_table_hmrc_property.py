from cls_helper_log import LogHelper
from cls_sqlite_table import SQLiteTable


class HMRC_Property(SQLiteTable):

    def __get_value_by_postcode_column(self, column_name):

        postcode = self.postcode
        if postcode:
            query = (
                self.query_builder()
                .select(column_name)
                .where(f'"Property postcode" = "{postcode}"')
                .build()
            )
            self.l.debug(f"query: {query}")
            result = str(self.sql.fetch_one_value(query))
        else:
            raise ValueError(f"Unexpected postcode: {postcode}")

        return result

    def __init__(self, postcode):
        self.l = LogHelper("HMRC_Property")
        self.l.set_level_debug()
        self.l.debug(__file__)
        self.l.debug(f"postcode: {postcode}")
        super().__init__("hmrc_property")
        self.postcode = postcode

    def fetch_by_postcode(self, postcode):
        query = self.query_builder().where(f"postcode = '{postcode}'").build()
        return self.sql.fetch_all(query)

    def get_property_postcode(self) -> str:
        return self.postcode

    def get_property_owner_code(self) -> str:
        return self.__get_value_by_postcode_column("Property owner code")

    def get_property_ownership_share(self) -> float:
        return self.__get_value_by_postcode_column("Property ownership share")

    def get_property_joint_owner_code(self) -> str:
        property_joint_owner_code = self.__get_value_by_postcode_column(
            "Property joint owner code"
        )
        self.l.debug(f'property_joint_owner_code: "{property_joint_owner_code}"')
        return property_joint_owner_code

    def is_let_jointly(self) -> bool:
        return self.get_property_joint_owner_code() != ""