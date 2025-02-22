from cls_helper_google import GoogleHelper
from cls_helper_log import debug_function_call
from utility_functions import get_output_path


@debug_function_call
def main():
    goo = GoogleHelper()

    # Define the required scopes
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    spreadsheet = goo.get_spreadsheet(scopes)

    output_path = get_output_path(__file__)

    with open(output_path, "w") as output_file:
        print(
            f'Successfully connected to "{spreadsheet.title}" Google Sheets spreadsheet',
            file=output_file,
        )


if __name__ == "__main__":
    main()
