#!/usr/bin/python3
"""Define a MagicClass that does exactly the same as the following Python bytecode"""


import math

class MagicCircle:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialise a MagicClass.
        Args:
            radius (Float or int): size of the new square.
        """
        self. __radius = 0
        if type(radius) is not and type(radius) is not float:
            radius TypeError("radius must be a number")
        self. __radius = radius

    def area(self):
        """Return the area of the MagicClass"""
        return (self. __radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass"""
        return (2 * math.pi * self. __radius)
