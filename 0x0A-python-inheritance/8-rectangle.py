#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometrry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeeometry):
    """Rep a rectangle using BaseGeometry."""

    class Rectangle(BaseGeometry):
        """rep a rectangle using BioGeometry"""

        def __init__(self, width, height):
            """initialize a new rectangle.


            Args:
                width (int) : eidth of rectangle
                height (int): heightof new rectangle
            """
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height
