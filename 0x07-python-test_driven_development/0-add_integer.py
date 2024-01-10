#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Returns integer addition of a and b
    Float arguments are typecasted to int before addition.
    Raises:Type error :if a and be is not aan integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isintance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
