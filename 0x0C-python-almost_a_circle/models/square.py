#!/usr/bin/python3
"""Inherits a square from a rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square using rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints info about square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)
