import signal
from contextlib import contextmanager

class TimeLimitException(Exception): 
    pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeLimitException
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
