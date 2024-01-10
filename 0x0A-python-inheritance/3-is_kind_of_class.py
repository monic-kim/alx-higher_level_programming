#!/usr/bin/python3
"""Defines a class and inherited class-chcking function"""

def is_kind_of_class(obj, a_class):

    """
    checks if an instance or inherited instance of a class

    Args:
       obj (any): object to check
       a_class (type):the class to match the type
    Returns: True- if obj is an instance of a class
    Otherwise - False
    """
    if isinstance (obj, a_class):
        return True
    return False
