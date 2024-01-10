#!/usr/bin/python3
"""Defines a name printing function."""


def say_my_name(first_name, last_name=""):
    """prints a name

    Args:
        first_name (str): First name to ptint
        last_name: Last name to print
    Raises:
        TypeError: if either of first or last anem are not stirngs
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
