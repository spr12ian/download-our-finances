from cls_helper_sqlalchemy import SQLAlchemyHelper


class TextToReal:
    def __init__(self):
        self.sql = SQLAlchemyHelper()

    def text_to_real(self):
        real_columns = [
            ["account_balances", "Credit"],
            ["account_balances", "Debit"],
            ["account_balances", "Balance"],
            ["transactions", "Credit"],
            ["transactions", "Debit"],
            ["transactions", "Nett"],
        ]

        for table_name, column_name in real_columns:
            self.sql.text_to_real(table_name, column_name)


def main():
    converter = TextToReal()

    # Convert TEXT to REAL for selected columns
    converter.text_to_real()


if __name__ == "__main__":
    main()
