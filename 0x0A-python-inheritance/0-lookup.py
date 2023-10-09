#!/usr/bin/python3

"""Defines the lookup function of an object attribute."""


def lookup(obj):
    """Returns a list of available attritubes of an object."""
    return (dir(obj))
