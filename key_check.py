from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper


l = LogHelper(__name__)
# l.setLevelDebug()
l.debug(__file__)


@LogHelper.log_execution_time
def main():
    goo = GoogleHelper()

    # Define the required scopes
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    spreadsheet = goo.get_spreadsheet(scopes)


if __name__ == "__main__":
    main()
