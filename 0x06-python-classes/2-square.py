#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialise a new square.
        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self. __size = size
