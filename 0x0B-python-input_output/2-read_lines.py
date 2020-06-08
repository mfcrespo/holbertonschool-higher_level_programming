#!/usr/bin/python3
""" My module for reading files
"""


def read_lines(filename="", nb_lines=0):
    """ Reads a certain amount of lines from a file
    Args:
        filename (str): the file to read
        nb_lines (int): the numer of line to read
    """
    linecount = 0
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            if nb_lines == linecount and nb_lines > 0:
                break
            else:
                print(line, end="")
            linecount += 1
