from flimit.time import time_limit, TimeLimitException
import time

def test_time_limit():
    @time_limit(1)
    def f():
        time.sleep(2)
    
    try:
        f()
    except TimeLimitException:
        return
    else:
        assert False

def test_time_nolimit():
    @time_limit(2)
    def f():
        time.sleep(1)
    
    try:
        f()
        time.sleep(2)
    except TimeLimitException:
        assert False
    else:
        assert True
