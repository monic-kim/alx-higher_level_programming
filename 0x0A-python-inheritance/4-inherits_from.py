#!/usr/bin/python3
"""Defines aninherited class checking function"""

def inherits_from(obj, a_class):
    """ checks if an object is an instance of a class.

    Args:
        obj (any): object to chck
        a_class (type): the clas to match the type of obj to

    Returns:
           True - if obj is an nherited instance of a_clas
           othewise - False
    """
    if  issubclass(type(obj),a_class) and type(obj) != a_class:
        return True
    return False
