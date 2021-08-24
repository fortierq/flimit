import sys

from flimit.memory import limit_memory, get_memory


def test_memory_error():
    memory = get_memory()

    @limit_memory(1)
    def f():
        L = [0 for _ in range(2*10**6//sys.getsizeof(0))]  # allocate 2 Mo
    
    try:
        f()
    except MemoryError:
        return
    else:
        assert False


def test_memory_noerror():
    memory = get_memory()

    @limit_memory(1)
    def f():
        L = [0 for _ in range(10**5//sys.getsizeof(0))]  # allocate 100 Ko
    
    f()
