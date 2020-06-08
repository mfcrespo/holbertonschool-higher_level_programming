#!/usr/bin/python3
""" My module for converting from JSON
"""
import json


def from_json_string(my_str):
    """ Converts JSON string into a Python object
    Args:
        my_str (str): a JSON string to convert
    """
    return(json.loads(my_str))
