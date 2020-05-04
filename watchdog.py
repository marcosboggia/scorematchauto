from queue import Queue, Empty
from kthread import KThread
import functools
from time import sleep
from cv2 import imwrite
from gui_automation import ForegroundHandler
from uuid import uuid1


FINISHED_MSG = 'finished'

fh = ForegroundHandler()
debug_folder = 'images/debug/'

timer = Queue()


def timed(deadline=60):
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
                    imwrite(debug_folder + f'{str(uuid1())}.jpg', fh.screenshot())
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
                timer.put(FINISHED_MSG)
                sleep(1)  # Some wait time between actions
                print(msg)
                return True
            else:
                return False
        return wrapper
    return inner_decorator
