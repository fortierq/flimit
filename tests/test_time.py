from flimit.time import limit_time, TimeLimitError
import time

def test_limit_time():
    @limit_time(1)
    def f():
        time.sleep(2)
    
    try:
        f()
    except TimeLimitError:
        return
    else:
        assert False

def test_time_nolimit():
    @limit_time(2)
    def f():
        time.sleep(1)
    
    f()
    time.sleep(2)
