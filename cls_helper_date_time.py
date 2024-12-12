from datetime import datetime


class DateTimeHelper:
    # Function to determine the ordinal suffix
    def get_ordinal_suffix(self, day):
        if 10 <= day % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return suffix

    # Function to format date with ordinal day
    def format_date_with_ordinal(self, date):
        day = date.day
        suffix = self.get_ordinal_suffix(day)
        return date.strftime(f"%A, %B {day}{suffix}, %Y")

    def get_date_today(self):
        now=datetime.now()
        return self.format_date_with_ordinal(now)

    def get_time_now(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
