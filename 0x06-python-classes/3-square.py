#!/usr/bin/python3
"""Defines a square"""


class Square:
    """has public instance area"""
    def __init__(self, size=0):
        """validates the value and type of size
        Args:
        size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the current square"""
        return self.__size * self.__size
