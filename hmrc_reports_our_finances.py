from cls_hmrc import HMRC


def print_reports(hmrc_people, tax_year):
    for person in hmrc_people:
        hmrc = HMRC(person, tax_year)
        hmrc.print_reports()


def main():
    # List of people to generate reports for
    hmrc_people = ["S", "B", "C"]

    # Tax year to generate reports for
    tax_year = "2023 to 2024"

    print_reports(hmrc_people, tax_year)


if __name__ == "__main__":
    main()
