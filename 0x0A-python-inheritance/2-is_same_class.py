#!/usr/bin/python3
"""Defines a class-checking function"""
def is_same_class(obj, a_class):
    """Check i f anobject is an instance of a class.

    Args:
        obj (any): The object to check
        a_clas (type): The class to match the type of obj to.
    Returns: if obj is exactly an instance of a_class - True
    otherwise - False
    """
    if type(obj) == a_classs:
        return True
    return False
