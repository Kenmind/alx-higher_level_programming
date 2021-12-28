#!/usr/bin/python3
"""Inherits a rectangle from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle from base init"""

        # Validate width
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        # validate height
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # validate x
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        # validate y
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter function
        """

        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width attribute
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter function
        """

        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height attribute
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter function
        """

        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x attribute
        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter function
        """

        return self.__y

    @y.setter
    def y(self, y):
        """Sets the x attribute
        """

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Retrieves the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle to stdout using '#'"""

        for i in range(self.__height):
            print("#" * self.__width)
