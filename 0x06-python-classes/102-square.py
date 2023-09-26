#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialise a new square.
        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the square."""
        return (self. __size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self. __size = value

    def area(self):
        """Return current area of the square"""
        return (self. __size * self. __size)

    def __eq__(self, other):
        """Define the == comparison to the square"""
        return self.area() == other.area()

    def __eq__(self, other):
        """Define the == comparison to the square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to the square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the lt comparison to the square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to the square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to the square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to the square"""
        return self.area() >= other.area()
