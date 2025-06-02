class SQL_Helper:
    def select_sql_helper(self, preferred_helper):
        match preferred_helper:
            case "SQLAlchemy":
                from sqlalchemy_helper import SQLAlchemyHelper

                return SQLAlchemyHelper()
            case "SQLite":
                from cls_helper_sqlite import SQLiteHelper

                return SQLiteHelper()
            case _:
                raise ValueError(f"Unexpected preferred_helper: {preferred_helper}")
