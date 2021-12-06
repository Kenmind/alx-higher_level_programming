#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func = fct(*args)
        return func
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
