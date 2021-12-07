#!/usr/bin/python3
"""module contains class Square"""


class Square:
    """Instantiates a private instance attribute
    with no type/value verification"""
    def __init__(self, size):
        """Initializes a square.
        Arg:
            size: size of the square
        """
        self.__size = size
