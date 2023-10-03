#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    l = 0
    while l < len(text) and text[l] == ' ':
        l += 1

    while l < len(text):
        print(text[l], end="")
        if text[l] == "\n" or text[l] in ".?:":
            if text[l] in ".?:":
                print("\n")
            l += 1
            while l < len(text) and text[l] == ' ':
                l += 1
            continue
        l += 1

