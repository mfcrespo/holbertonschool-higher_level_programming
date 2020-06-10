#!/usr/bin/python3
"""My Module for creating Rectangle class that inherits from Base
"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """the class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes values that square
        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            id (int): number of square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the __str__ method to return
        [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

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
