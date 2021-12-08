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
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2\
                or type(value[0]) is not int or value[0] < 0\
                or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square to stdout with #"""
        if self.__size == 0:
            print("")
            return
        [print("") for loop in range(0, self.position[1])]
        for loop in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
