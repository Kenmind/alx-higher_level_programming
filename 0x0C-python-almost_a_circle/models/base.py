#!/usr/bin/python3
"""Defines the base class"""
import json


class Base:
    """base project class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """prints the json string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
