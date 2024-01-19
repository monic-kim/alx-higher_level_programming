#!/usr/bin/python3
"""Defines a squareclass"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Rep a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new square

        Args:
           size (int): the sie of new square
           x (int): x coordinate of new square
           y (int): y coordinate of new square
           id (int):identity of new square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """update the square.

        Args:
            *args (ints): new attributes values.
                - 2nd arguments rep size attribute
                - 3rd arguments rep x attribute
                - 4th arguments rep y attribute
            **kwargs (dict): new key pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self,y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    
    def to_dictionary(self):
        """Return the dictionary representations of the Square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width)
