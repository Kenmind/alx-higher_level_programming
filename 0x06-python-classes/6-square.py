#!/usr/bin/python3
"""Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            __size: size of the squre
            __position: position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position for the square"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of a square"""
        return self.__size * self__size

    def my_print(self):
        """prints the square to stdout with #"""
        loop = 0
        if self.__size == 0:
            print("")
        [print("") for loop in range(self.position[1])]
        for loop in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
