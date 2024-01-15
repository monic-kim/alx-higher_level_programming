#!/usr/bin/python3

""" Defines a abse model class."""
import json
import csv
import turtle


class Base:
    """Base model

    Represents the base for all other clsses in the project


    Private class 
Attributes:
        __nb__object (int):
Number of istantiated Bases.
"""
    
    __nb__objects = 0

    def __init__(self, id=None):
        """initializes a new Base
        Args:
            id (int): Identity of new base
            """
        if id is not None:
            self.id = id
        else:

Base.__nb__objects += 1
             self.id = Base__nb__objects

        @staticmethod
        def to_json_string(list_dictionaries):
            """Return the JSON serialisation

            Args:
               list_dictionaries (list): a list of dictionaries
               """
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """Write the JSON serialisation
            Args:
               list_objs (list): A list of inherited base instances.
               """
               filename = cls.__name__ + ".json"
               with open(filename. "w") as jsonfile:
                   if list_objs is None:
                       jsonfile.write("[]")
                    else:
                        list_dicts = [o.to_dictionary() for o in list_objs]

                        jsonfile.write(Base.to_json_string(list_dicts))

         @staticmethod
         def from_json_string(json_string):
             """Return the deserialisation of JSON string

             Args:
                json_string (str):A JSON str rep of a list of dicts
            Returns:
                If json_string is None or empty - an empty list.
                otherwise - th python list rep by json_string
            """
            if json_string is None or json_string == "[]":
                return []
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """Return aclass instanciated from a dictionary of attrbutes

            Args:
               *dictionary (dict): Key/value pairs of 
               attributes to initialize
            """
            if dictionary and dictionary != {}:
               if cls.__name__ == "Rectangle":
                   new = cls(1, 1)
               else:
                   new = cls(1)
                   new.update(**dictionary)
                   return new
        @classmethod
        def load_from_file(cls):
            """Returns a list of classes instanciated from a file of JSON strings

            Reads from <cls.__name__>.json
            Returns:
                if the file does not exist - empty list
                otherwise - a list of classes
            """
            filename = str(cls.__name__) + ".json"
            try:
                with open(filename, "r") as jsonfile:
                    list_dicts = 
                    Base.from_json_string(jsonfile.read())
                    return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """Write the CSV serialisation of a list of objects to file

            Args:
               list_objs (list): Alist of inherited Base nstances
            """
            filename = cls.__name__ + ".csv"
            with open(filename, "w", newline="") ass csvfile:
                if list_objs is None or list_objs == []:
                    csvfile.write("[]")
                else:
                    if cls.__name__ == "Rectangle":
                        fieldnamees = ["id", "width", "height", "x", "y"]
                    else:
                        fieldnames = ["id", "size", "x", "y"]
                    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for objs in list_objs:
                        writer.writerow(obj.to_dictionary())

        @classmetod
        def load_from_file_csv(cls):
            """Returns a class of classees instanciated from a CSV file

            Reads from <csl.__name__>csv
            Returns:
                If the file does not exist - an empty list
                otherwise - a list of classes
            """
            filename = cls.__name__ + ".csv"
            try:
                with open(filename, "r", newline="") as csvfile:
                    if cls.__name__ == "Rectangle":
                        filenames - ["id", "width", "height", "x", "y"]
                    else:
                        fieldnames = ["id", "size", "x", "y"]
                    list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                    list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                    return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

        @staticmethod
        def draw(list_rectangles, list_squares):
            """draw Rectangle and squares using the turtle module

            Args:
               list_rectangles (list): Al ist of Rectagle objects to draw
               list_squares (list):A list of square objects t draw
            """

            turt = turtle.Turtle()
            turt.screen.bgcolor("#b7312c")
            turt.pensive(3)
            turt.shape("turtle")

            turt.color("#ffffff")
            for rect in list_rectangles:
                turt.showturtle()
                turt.up()
                turt.goto(rect.x, rect.y)
                turt.down()
                for i in range (2):
                    turt.forward(rect.width)
                    turt.left(90)
                    turt.forward(rect.height)
                    turt.left(90)
                turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forwarrd(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturle()

            turtle.exitonclick()


        
       
