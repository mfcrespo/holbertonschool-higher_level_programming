#!/usr/bin/python3
""" My Module for converting from JSON to Python
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    Args:
        filename (str): filename to read from
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return(json.load(f))
