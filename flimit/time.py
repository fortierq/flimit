import signal
from contextlib import contextmanager


class TimeLimitError(Exception): 
    pass


@contextmanager
def limit_time(seconds : int):
    """Decorator to limit time usage of a function. Raise TimeLimitError when the limit is exceeded.

    Args:
        seconds (int): Maximum computation time of the function, in seconds.
    
    Raises:
        TimeLimitError: When the function reaches the limit.
    """

    def signal_handler(signum, frame):
        raise TimeLimitError
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
