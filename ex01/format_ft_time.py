import datetime
import time

def ftime():
    import datetime
    now = datetime.datetime.now()
    ns = time.clock_gettime(0)
    print(f"Seconds since January 1, 1970: {ns:,.4f} or {ns:.2e} in scientific notation")
    print(now.strftime("%b %d %Y"))

ftime()