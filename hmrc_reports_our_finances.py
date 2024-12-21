from cls_hmrc import HMRC


def main():
    # hmrc = HMRC("B", "2023 to 2024")
    # hmrc.print_report()

    hmrc = HMRC("S", "2023 to 2024")
    hmrc.print_report()


if __name__ == "__main__":
    main()
