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

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

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

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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

    def __str__(self):
        """overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes with *args or **kwargs
        Args:
            *args (list): argument list without key
            **kwargs (dict): argument list with key
        """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.width = kwargs['width']
                    if i == 'height':
                        self.height = kwargs['height']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """ that returns the dictionary representation of a Rectangle
        """

        new_dict = {}
        attrs = ["id", "width", "height", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict
