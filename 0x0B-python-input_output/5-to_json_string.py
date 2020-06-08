#!/usr/bin/python3
""" Documentation for a to_json_string function
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
    Args:
        my_obj (object): object ot turn into JSON
    """
    return(json.JSONEncoder().encode(my_obj))
