#!/usr/bin/python3
"""Documentation for defines a square"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """On instantation, gives the size and position of the square
           size must be integer or position must be a tupla with two integers,

        Args:
            size (int, optional): The size of the square object
            position (tuple, optional): the position of the object when printed
        Raises:
            ValueError: When the value passed in is less than 0
            TypeError: When the value passed in is not an integer or
            tupla´s integers
        """

        self.size = size
        self.position = position

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
            or a tuple´s integers
            ValueError: When the value passed in is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the current position of the square object"""
        return self.__position

    @position.setter
    def position(self, value):
        """Resets the position of the square object
        Args:
            value (tuple): a tuple of two integers defining the position
        Raises:
            TypeError: when the value passed is not an integer or a two integer
            tuplet
            ValueError: when the value passed is less than 0
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for height in range(self.__position[1]):
                print()

        for rows in range(self.__size):
            for spaces in range(self.__position[0]):
                print(' ', end='')
            for columns in range(self.__size):
                print('#', end='')
            print()
