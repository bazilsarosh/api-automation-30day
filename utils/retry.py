import time

def retry(fn, attempts=3, delay=0.5, exceptions=(Exception,)):
    last = None
    for _ in range(attempts):
        try:
            return fn()
        except exceptions as e:
            last = e
            time.sleep(delay)
    raise last
