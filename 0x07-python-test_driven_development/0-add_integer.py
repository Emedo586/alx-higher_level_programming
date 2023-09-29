#!/usr/bin/python3
"""Define an integer addition function."""
def add_integer(a, b=98):
    """"Return the integer addition of a and b."""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an interger")
    return (int(a) + int(b))
