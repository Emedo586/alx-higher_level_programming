#!/usr/bin/python3
import sys


def safe_Function(fet, *args):
    try:
        result = fet(*args)
        return (result)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
