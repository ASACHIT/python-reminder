import sys
from plyer import notification


def no_argv_passed():
    print("😩 Ahh, Arguments were not properly passed.🥺")
    print("""Command format - python remind.py <time in h,m,s> <"task"> ✨""")


def remind_me():
    # checks if command arguments were passed or not
    try:
        time = sys.argv[1]
        task = sys.argv[2]
    except IndexError:
        no_argv_passed()
        exit()

    # converts input time to second
    time_unit, number = time[-1], time[-2]
    if time_unit == "h":
        remind_after = int(number) * 60 * 60
    elif time_unit == "m":
        remind_after = int(number) * 60
    elif time_unit == "s":
        remind_after = int(number)
    else:
        no_argv_passed()
        exit()

    print(f"😃 Reminder Set For {task} After {remind_after} Seconds🕐 From Now !")

    import time

    time.sleep(remind_after)
    notification.notify(
        title="Reminder",
        message=task,
        app_name="py Reminder",
        app_icon="icon/clock.ico",
        ticker="reminder",
        timeout=20
    )


if __name__ == "__main__":
    remind_me()
