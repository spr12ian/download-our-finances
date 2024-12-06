from datetime import datetime


def print_time():
    # Get the current time
    current_time = datetime.now().time()

    # Print the current time
    print("Current Time:", current_time)


def tprint(msg):
    # Get the current time
    current_time = datetime.now().time()

    message = f"{current_time}: {msg}"
    print(message)
