#!/usr/bin/python3
import sys


def safe_Function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as i:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
