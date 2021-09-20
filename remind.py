import sys

import pyttsx3
from win10toast import ToastNotifier

# intializing notifier
notification = ToastNotifier()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def remind_me():
    # checks if command arguments were passed or not
    try:
        time = sys.argv[1]
        task = sys.argv[2]
    except IndexError:
        print("😩 Ahh! No command Arguments were passed !🥺")
        print("""Command format - python remind.py <time in h,m,s> <"task"> ✨""")
        exit()

    # converts input time to second
    time_unit, number = time[-1], time[-2]
    if time_unit == "h":
        remind_after = int(number) * 60 * 60
    elif time_unit == "m":
        remind_after = int(number) * 60
    elif time_unit == "s":
        remind_after = int(number)

    print(f"😃 Reminder Set For {task} After {remind_after} Seconds🕐 From Now !")

    import time
    time.sleep(remind_after)
    speak(f"Hey, you have a reminder set for {task}")

    notification.show_toast(
        threaded=True, title="Reminder ⏰", msg=task, duration=10
    )  # pushes notification


if __name__ == "__main__":
    remind_me()
