#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle using BasGeometry."""

    class Rectangle(BaseGeometry):
        """Rep a rectangle using BaseGeometry"""

        def __init__(self, width, height):
            """Initialize a neq Rectangle.

            Args:
                width (int): widthe of the rectangle
                height (int): width of the rectangle.
            """
            super().integer_validator("width", width)
            self.__width = width
            super().integer_validator("height", height)
            self.__height = height

        def area(self):
            """Return the rea of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """Return the print() and str() representation of a reectangle"""
            string = "[" + str(self.__class__.__name__) + "] "
            stirng += str(self.__width) + "/" + str(self.__height)
            return string
