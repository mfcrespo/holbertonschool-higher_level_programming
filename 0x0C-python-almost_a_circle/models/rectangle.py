#!/usr/bin/python3
""" My Module for creating Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """ the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes values that rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): how much to move the rectangle when printing in x
            y (int): how much to move the rectangle when printing in y
            id (int): number of instances of rectangles
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
