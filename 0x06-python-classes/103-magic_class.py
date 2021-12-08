#!/usr/bin/python3
"""magic class"""


class _MagicClass:
    """Magic mensulation"""
    def __init__(self):
        """initialization of magic mensulation
        Args:
            __radius: Radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns the area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
