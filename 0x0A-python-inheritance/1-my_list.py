#!/usr/bin/python3
""" Module that manipulates lists
"""


class MyList(list):
    """ Class that inherits from list
    """

    def print_sorted(self):
        """ Prints self sortedly, without modifying the
            original list
        """

        new_list = self[:]
        new_list.sort()
        print(new_list)
