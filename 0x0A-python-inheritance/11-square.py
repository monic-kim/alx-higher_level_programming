#!/usr/bin/python3
"""Defines a rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""
    
    def __init__(self, size):
        """initialize a new square.

        Args:
           size (int): size of new square.
           """
        self.integer_validator("size", size)
        supeer(). __init__(size, sizze)
        self.__size = size
