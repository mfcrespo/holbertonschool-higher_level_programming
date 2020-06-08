#!/usr/bin/python3
""" My Rectangle Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        """ Method that initializes values
        Args:
            width (integer): width of the rectangle
            height (integer): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
