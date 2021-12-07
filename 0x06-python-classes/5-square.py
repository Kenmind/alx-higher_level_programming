#!/usr/bin/python3
"""Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initializes a square
        Args:
            __size: size of the squre
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square
        Args:
            value: size to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size * self__size

    def my_print(self):
        """prints the square to stdout with #"""
        loop = 0
        if self.__size == 0:
            print("")
        else:
            for loop in range(self.__size):
                print('#' * self.__size)
