#!/usr/bin/python3
""" My Module for creating a base class
"""
import json


class Base:
    """ This class will be the “base” of all other classes in this project
    Attributes:
        __nb_objects (private class attribute): the number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor: f id is not None, assign the public
            instance attribute id with this argument value - you can
            assume id is an integer and you don’t need to test the type of it
            public instance attribute id
        Args:
            id (int): The number to assign to self.id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of representations of an instances
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation json_string
        Args:
            json_string (str): string to turn into Python object
        """

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list of objects): objects to turn into
        """

        filename = "{}.json".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list += [obj.to_dictionary()]

        json_list = Base.to_json_string(obj_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary of values to make into an instance of
                               Square or Rectangle
        """

        if "size" in dictionary:
            c1 = cls(1)
        else:
            c1 = cls(1, 1)

        c1.update(**dictionary)

        return c1

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """

        from_filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(from_filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_of_dicts = cls.from_json_string(raw_json)
            for d in list_of_dicts:
                instance_list += [cls.create(**d)]
        except FileNotFoundError:
            pass
        return instance_list
