from cls_helper_date_time import DateTimeHelper
from functools import wraps
import logging
import time

# https://docs.python.org/3/library/logging.html?form=MG0AV3

DEBUG_FILE = "debug.log"
logging.basicConfig(filename=DEBUG_FILE, level=logging.INFO)

logger = logging.getLogger(__name__)
logger.debug(__file__)

# Use this snippet:
# from cls_helper_log import LogHelper
# l = LogHelper()
# LogHelper.debug_enabled = True
# l.clear_debug_log()

# To time functions wrap them like this:
# @LogHelper.log_execution_time


class LogHelper:
    debug_enabled = False

    def __init__(self, name):
        self.logger = logging.getLogger(name)

        self.dt = DateTimeHelper()

    def clear_debug_log(self):
        with open(self.LOG_FILE, "w") as file:
            pass

    def debug(self, msg):
        self.logger.debug(msg)

    def debug_date_today(self):
        if self.debug_enabled:
            with open(DEBUG_FILE, "a") as file:
                file.write(f"{self.get_date_today()}\n")

    def get_date_today(self):
        dt = self.dt
        return dt.get_date_today()

    def info(self, msg):
        self.logger.info(msg)

    @staticmethod
    def log_execution_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            # print(f"Starting '{func.__name__}' at {time.ctime(start_time)}")

            result = func(*args, **kwargs)

            end_time = time.time()
            # print(f"Finished '{func.__name__}' at {time.ctime(end_time)}")

            execution_time = end_time - start_time
            logger.info(
                f"Function '{func.__name__}' executed in {execution_time:.2f} seconds"
            )

            return result

        return wrapper

    def print_date_today(self):
        logger.info(self.get_date_today())

    def print_time(self):
        dt = self.dt

        time_now = dt.get_time_now()

        logger.info("Current Time:", time_now)

    def tdebug(self, msg):
        if self.debug_enabled:
            dt = self.dt

            time_now = dt.get_time_now()

            message = f"{time_now}: {msg}"
            logger.info(message)

    def tprint(self, msg):
        dt = self.dt

        time_now = dt.get_time_now()

        message = f"{time_now}: {msg}"
        logger.info(message)

    def warning(self, msg):
        self.logger.warning(msg)
