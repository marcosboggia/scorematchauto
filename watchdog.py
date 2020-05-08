from queue import Queue, Empty
from kthread import KThread
import functools
from time import sleep
from cv2 import imwrite
from gui_automation import ForegroundHandler
from uuid import uuid1
from os import makedirs
from db import add_failed


FINISHED_MSG = 'finished'

handler = ForegroundHandler()
# Create debug folder
debug_folder = 'images/debug/'
makedirs(debug_folder, exist_ok=True)

timer = Queue()


def timed(run_id, deadline=60):
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal deadline
            t = KThread(target=func, args=args, kwargs=kwargs)
            t.start()
            while True:
                try:
                    response = timer.get(timeout=deadline)
                    if response == FINISHED_MSG:
                        return True
                    elif type(response) == int:
                        deadline = response
                except Empty:
                    print(" Failed!")
                    imwrite(debug_folder + f'{str(uuid1())}.jpg', handler.screenshot())
                    add_failed(run_id)
                    if t.is_alive():
                        t.kill()
                    return False
        return wrapper
    return inner_decorator


def report_success(msg=" Success!"):
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sleep(1)  # Some wait time between actions
            if func(*args, **kwargs):
                print(msg)
                sleep(1)  # Some wait time between actions
                timer.put(FINISHED_MSG)
                return
            else:
                return
        return wrapper
    return inner_decorator
