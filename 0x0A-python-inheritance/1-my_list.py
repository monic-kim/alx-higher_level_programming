#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """Implemens sorted printing for the the builtin list class
    """
    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
