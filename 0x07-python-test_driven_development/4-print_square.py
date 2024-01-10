#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
"""Prints a square with # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
