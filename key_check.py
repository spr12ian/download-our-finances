from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper
from cls_helper_log import debug_function_call


l = LogHelper(__file__)
# l.set_level_debug()
l.debug(__file__)


@debug_function_call
def main():
    goo = GoogleHelper()

    # Define the required scopes
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    spreadsheet = goo.get_spreadsheet(scopes)

    l.print(
        f'Successfully connected to "{spreadsheet.title}" Google Sheets spreadsheet'
    )


if __name__ == "__main__":
    main()
