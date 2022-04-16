from contextlib import contextmanager
import resource
import os, psutil


@contextmanager
def limit_memory(octets: int):
    """Decorator to limit memory usage of a function. Raise MemoryError when the limit is exceeded.

    Args:
        octets (int): Maximum number of octets the function can allocate.
    
    Raises:
        MemoryError: When the function reaches the limit.
    """

    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    soft_new = get_memory() + octets
    if soft == -1 or soft_new < soft:
        resource.setrlimit(resource.RLIMIT_AS, (soft_new, hard))
    try:
        yield
    finally:
        pass


def get_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss  # octets 
