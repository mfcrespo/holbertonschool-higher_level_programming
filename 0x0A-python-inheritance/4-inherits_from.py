#!/usr/bin/python3
""" My Module to test object property
"""


def inherits_from(obj, a_class):
    """ Function that tests if object is an instance of a class
        that inherited (directly or indirectly) from the specified class
    Args:
        obj (object): object to test
        a_class (class): the class to test if obj is a part of
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
