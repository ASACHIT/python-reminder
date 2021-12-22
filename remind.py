import time

from notifypy import Notify
from pytimeparse import parse

from colors import Colorize
from sync import BaseTask, EventLoop
from utils import run_forever


class Notification(Notify):
    """
    Notification for the reminder.
    """
    def __init__(self, title, message):
        super().__init__(disable_logging=True)
        self.title = title
        self.message = message

    def notify(self):
        self.send()


class Task(BaseTask):
    """
    Task is runnable if the time is less than the current time.
    """
    def __init__(self, title, remind_after):
        super().__init__()
        self.task = title
        self.remind_time = time.time() + remind_after
        self.notification = Notification(
            title="Reminder",
            message=f"{title} in {remind_after}",
        )

    def run(self):
        self.notification.notify()

    def is_runnable(self):
        return self.remind_time <= time.time()

    def __str__(self):
        return f"{self.task} in {self.remind_time}"


@run_forever
def main():
    task = Colorize.cyan_input("Enter Task:")
    remind_after = parse(Colorize.blue_input("Enter time: "))


    while remind_after is None:
        Colorize.red_print(
            "Invalid time. Can you try again? (e.g. '5 minutes')")
        remind_after = parse(Colorize.blue_input("Enter time: "))

    task_queue.put(Task(task, remind_after))

    Colorize.green_print("Task succesfully added. ")
    Colorize.green_print(
        "You will be reminded in {} seconds.".format(remind_after))


if __name__ == "__main__":
    loop = EventLoop()
    loop.start()
    loop.join
    task_queue = loop.get_queue()
    main()
