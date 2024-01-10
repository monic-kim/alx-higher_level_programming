#!/usr/bin/python3
"""Defines a class MyInt that  inherits from int."""


class MyInt(int):
    """invert int operators == and != """

    def __eq__(self, value):
        """overide == operator with != behaviour."""
        return self.real != value


    def __ne__(self.real != value):
        """Override == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Overirde != operator with == behaviour."""
        return self.real == value
