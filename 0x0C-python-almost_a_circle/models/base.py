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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to file"""
        js_str = '[]'
        js_list = []
        if list_objs is not None:
            for i in list_objs:
                js_list.append(i.to_dictionary())
            if len(js_list) > 0:
                js_str = Base.to_json_string(js_list)
        with open(cls.__name__ + '.json', 'w') as n:
            n.write(js_str)
