from abc import ABC, abstractmethod
import queue
import threading
from threading import Event
import asyncio
import time

from utils import run_forever


class BaseTask(ABC):
    """
    Base class for all tasks.

    Should be inherited by all tasks.

    Methods:
        run(): Runs the task.
        is_runnable(): Returns True if the task is runnable.
    """
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def is_runnable(self):
        pass

    def __init__(self):
        super().__init__()
        self.evt = Event()

    def cancel_task(self):
        self.evt.set()

class EventLoop(threading.Thread):
    """
    Runs the event loop.
    """
    def __init__(self, taskQueue: queue.Queue[BaseTask] = None, daemon=True, *args, **kwargs):
        if not taskQueue:
            taskQueue = queue.Queue()
        threading.Thread.__init__(self, daemon=daemon, *args, **kwargs)
        self.task_queue = taskQueue

    def get_queue(self):
        return self.task_queue

    @run_forever
    def run(self):
        current_task = self.task_queue.get()
        if current_task.is_runnable():
            current_task.run()
        else:
            self.task_queue.put(current_task)
            time.sleep(0.1)
