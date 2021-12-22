#!/usr/bin/python3
""" returns a json representation of an object"""


def class_to_json(obj):
    """returns a json representation of the obj object
    Args:
        obj: object
    """
    return obj.__dict__
