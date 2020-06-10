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
