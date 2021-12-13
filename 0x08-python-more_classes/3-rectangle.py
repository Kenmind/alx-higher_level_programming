#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Defines private instance attribute"""
    def __init__(self, width=0, height=0):
        """Instantiates the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 and self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """prints the rectangle"""
        if self.width == 0 and self.height == 0:
            return ""
        new = []
        for i in range(self.height):
            for j in range(self.width):
                new.append('#')
            if i != self.height - 1:
                new.append("\n")
        return "".join(new)
