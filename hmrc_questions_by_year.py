from useful_functions import to_valid_method_name
from sqlite_helper import SQLiteTable


class HMRC_QuestionsByYear(SQLiteTable):
    def __init__(self, tax_year):
        super().__init__("hmrc_questions_by_year")
        self.tax_year = tax_year

    def get_questions(self):
        query = (
            self.query_builder()
            .select("Question", f"{self.tax_year}")
            .where(f'"{self.tax_year}"<> ""')
            .build()
        )

        questions = [
            [
                row[0],
                (split := row[1].split(","))[0],
                (split[1] if len(split) > 1 else None),
                "get_" + to_valid_method_name(row[0]),
                (split[2] if len(split) > 2 else None),
            ]
            for row in self.sql.fetch_all(query)
        ]

        return questions

    def get_questions_2023_2024X(self):
        return [
            ["TR 4", "1", "Total"],
            ["TR 4", "1.1", "Total"],
            ["TR 5", "1", "Your spouse's first name"],
            ["TR 5", "2", "Your spouse's last name"],
            ["TR 5", "3", "Your spouse's National Insurance number"],
            ["TR 5", "4", "Your spouse's date of birth"],
            ["TR 5", "5", "Date of marriage"],
            ["TR 6", "2", "Collect small amounts by PAYE"],
            ["TR 6", "3", "Collect by PAYE"],
            ["TR 8", "22", "Declaration"],
            ["SES 1", "1", "Description of business"],
            ["SES 1", "2", "Postcode of your business address"],
            ["SES 1", "7", "Date your accounts are made up to"],
            ["SES 1", "8", "Cash basis (Yes/No)"],
            ["SES 1", "9", "Total"],
            ["SES 1", "10.1", "Trading income allowance"],
            ["SES 2", "1", "Net profit"],
            ["SES 2", "28", "Net business profit for tx purposes"],
            ["SES 2", "31", "Total taxable profits from this business"],
            [
                "SES 2",
                "36",
                "Pay Class 2 NICs voluntarily If your total profits are less than £6,725, put 'X' in the box",
            ],
            ["UKP 1", "1", "Count properties rented out"],
            ["UKP 2", "20", "Total"],
            ["UKP 2", "24", "Total"],
            ["UKP 2", "25", "Total"],
            ["UKP 2", "27", "Total"],
            ["UKP 2", "28", "Total"],
            ["UKP 2", "38", "Total"],
            ["UKP 2", "40", "Total"],
            ["TC 1", "1", "Total"],
            ["TC 1", "4.1", "Total"],
        ]
