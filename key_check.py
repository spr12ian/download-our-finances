from cls_helper_google import GoogleHelper
from cls_helper_log import LogHelper


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


# # Example usage
# @log_execution_time
# def example_function():
#     time.sleep(2)  # Simulate a function that takes 2 seconds to run


# example_function()
