from cls_helper_date_time import DateTimeHelper
from functools import wraps
import time

# Use this snippet:
# from cls_helper_log import LogHelper
# l = LogHelper()
# LogHelper.debug_enabled = True
# l.clear_debug_log()

# To time functions wrap them like this:
# @LogHelper.log_execution_time


class LogHelper:
    LOG_FILE = "debug.log"
    debug_enabled = False

    def __init__(self):
        self.dt = DateTimeHelper()

    def clear_debug_log(self):
        with open(self.LOG_FILE, "w") as file:
            pass

    def debug(self, string):
        if self.debug_enabled:
            with open(self.LOG_FILE, "a") as file:
                file.write(f"{string}\n")

    def debug_date_today(self):
        if self.debug_enabled:
            with open(self.LOG_FILE, "a") as file:
                file.write(f"{self.get_date_today()}\n")

    def get_date_today(self):
        dt = self.dt
        return dt.get_date_today()

    @staticmethod
    def log_execution_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if LogHelper.debug_enabled:
                start_time = time.time()
                print(f"Starting '{func.__name__}' at {time.ctime(start_time)}")

            result = func(*args, **kwargs)

            if LogHelper.debug_enabled:
                end_time = time.time()
                print(f"Finished '{func.__name__}' at {time.ctime(end_time)}")

                execution_time = end_time - start_time
                print(f"Execution time: {execution_time:.2f} seconds")

            return result

        return wrapper

    def print_date_today(self):
        print(self.get_date_today())

    def print_time(self):
        dt = self.dt

        time_now = dt.get_time_now()

        print("Current Time:", time_now)

    def tdebug(self, msg):
        if self.debug_enabled:
            dt = self.dt

            time_now = dt.get_time_now()

            message = f"{time_now}: {msg}"
            print(message)

    def tprint(self, msg):
        dt = self.dt

        time_now = dt.get_time_now()

        message = f"{time_now}: {msg}"
        print(message)
