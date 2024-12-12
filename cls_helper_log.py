from cls_helper_date_time import DateTimeHelper


class LogHelper:
    def __init__(self):
        self.dt = DateTimeHelper()

    def print_date_today(self):
        dt = self.dt
        now = dt.get_date_now()
        print(dt.format_date_with_ordinal(now))

    def print_time(self):
        dt = self.dt
        # Get the current time
        current_time = dt.get_time_now()

        # Print the current time
        print("Current Time:", current_time)

    def tprint(self, msg):
        dt = self.dt
        # Get the current time
        current_time = dt.get_time_now()

        message = f"{current_time}: {msg}"
        print(message)
