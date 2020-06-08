#!/usr/bin/python3
""" My module for reading a file
"""


def number_of_lines(filename=""):
    """ Returns the number of lines in a file
    Args:
        filename (str): the file to read
    """
    linecount = 0
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            linecount += 1
    return linecount
