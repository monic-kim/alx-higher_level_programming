#!/usr/bin/python3
"""Defines a function thta adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add  new attrbte to an objct


    Args:
        obj (any): object to add an attribute to
        at (str): name of the attribute to add to obj
        value (any): value of att
    Raises:
        TypeError: if the  attribute cannnot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add  new attribute")
    setattr(obj, att, value)
