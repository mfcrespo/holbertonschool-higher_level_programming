#!/usr/bin/python3
""" My Module for creating Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance of a square
        Args:
            size (int): size of the square
            x (int): how much to shift the square when printing
            y (int): how much to shift the square when printing
            id (int): number of instances of squares
        """

        super().__init__(size, size, x, y, id)
