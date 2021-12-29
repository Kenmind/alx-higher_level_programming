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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string
        representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs already set"""
        a = None
        if cls.__name__ == "Square":
            a = cls(1)
        elif cls.__name__ == "Rectangle":
            a = cls(1, 1)
        cls.update(a, **dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        obj_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as n:
                list_output = cls.from_json_string(n.read())
                for i in list_output:
                    obj_list.append(cls.create(**i))
        except Exception:
            pass
        return obj_list
