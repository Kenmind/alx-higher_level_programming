#!/usr/bin/python3
"""Defines the base class"""
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """

        with open(cls.__name__ + ".csv", "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csvfile.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        try:
            with open(cls.__name__ + ".csv", "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw_square(turt, x, y, size):
        """Draws a square using a turtle object"""

        turt.showturtle()
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.goto(x, y)
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.hideturtle()

    @staticmethod
    def draw_rect(turt, x, y, width, height):
        """Draws a rectangle using a turtle object"""

        turt.showturtle()
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.goto(x, y)
        for i in range(2):
            turt.forward(width)
            turt.left(90)
            turt.forward(height)
            turt.left(90)
        turt.hideturtle()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("green")
        turt.pensize(2)
        turt.shape("turtle")

        turt.color("beige")
        for rect in list_rectangles:
            Base.draw_rect(turt, rect.x, rect.y, rect.width, rect.height)

        turt.color("blue")
        for sq in list_squares:
            Base.draw_square(turt, sq.x, sq.y, sq.size)
        turtle.exitonclick()
