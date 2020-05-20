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

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the current size of the object
           If called with a value, the setter function overwrites the
           current size with the size passed in
        Returns:
            size of the current object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Resets the size of the object with the value called
        Args:
            value (int): the new size of the square object
        Raises:
            TypeError: When the value passed in is not an integer
            ValueError: When the value passed in is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
                print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
