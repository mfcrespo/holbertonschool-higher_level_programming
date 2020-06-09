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
            x (int): the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id (int): number of rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def size(var_size, value):
        """ Validates and handles all error messages of height or width
        Args:
            var_size (str): the variable name of size
            value (int): the value associated with var_size
        """

        size = ["width", "height"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var_size))
        if var_size in size and value <= 0:
            raise ValueError("{} must be > 0".format(var_size))

    @property
    def width(self):
        """Getter of the width attribute
        Returns:
            the width of the instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute
        Args:
            value (int): value to set to width
        """

        self.size("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute
        Returns:
            the height of the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute
        Args:
            value (int): the value to set the height to
        """

        self.size("height", value)
        self.__height = value

    @staticmethod
    def coordinate(var_coord, value):
        """ Validates and handles all error messages
        Args:
            var_coord (str): the variable name
            value (int): the value associated with var_coord
        """

        coord = ["x", "y"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var_coord))
        if var_coord in coord and value < 0:
            raise ValueError("{} must be >= 0".format(var_coord))

    @property
    def x(self):
        """Getter for the x attribute
        Returns:
            the x attribute of the instance
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute
        Args:
            value (int): the value to set the x attribute to
        """

        self.coordinate("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute
        Returns:
            the y attribute of the instance
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the y attribute
        Args:
            value (int): the value to set the y attribute to
        """

        self.coordinate("y", value)
        self.__y = value

    def area(self):
        """ that returns the area value of the Rectangle instance
        """

        return self.width * self.height

    def display(self):
        """that prints in stdout the Rectangle instance with the character #
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(' ', end="")
            for j in range(self.width):
                print('#', end="")
            print()
