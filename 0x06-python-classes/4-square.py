#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ Retrieves the size of a square"""
    def __init__(self, size=0):
        """initializes Square
        Args:
            __size: the size of square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square
        Args:
        value: size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        self.__size = value

    def area(self):
        """returns the area of square"""
        return self.__size * self.__size
