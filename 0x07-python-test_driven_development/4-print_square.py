#!/usr/bin/python3
def print_square(size):
"""Define a text-indentation function."""
if not isinstance(size, int):
    raise TypeError("size must be an integer")
if size < 0:
    raise ValueError("size must be >= 0")

for i range(size):
    [print("", end="") for j in range(size)]
print("")
