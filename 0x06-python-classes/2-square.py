#!/usr/bin/python3
"""Documentation for defines a square"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0):
        """On instantation, gives the size of the square
           size must be an integer, otherwise raise a TypeError
           exception with the message size must be an integer
        Args:
            size (int, optional): The size of the square object
        Raises:
            ValueError: When the value passed in is less than 0
            TypeError: When the value passed in is not an integer
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
