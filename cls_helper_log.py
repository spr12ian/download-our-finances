from cls_helper_date_time import DateTimeHelper


class LogHelper:
    def __init__(self):
        self.dt = DateTimeHelper()

    def print_date_today(self):
        dt = self.dt
        print(dt.get_date_today())

    def print_time(self):
        dt = self.dt

        time_now = dt.get_time_now()

        print("Current Time:", time_now)

    def tprint(self, msg):
        dt = self.dt

        time_now = dt.get_time_now()

        message = f"{time_now}: {msg}"
        print(message)
