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
