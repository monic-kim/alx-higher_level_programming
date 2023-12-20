#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        Args:
            size (int):
        self.size = size

    def size(self):
        return (self.__size)

    def size (self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.___size * self.__size)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self.other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() <= other.area()
    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
