#!/usr/bin/python3
""" My module for writing to files
"""


def write_file(filename="", text=""):
    """ Appends text to the end of a file
    Args:
        filename (str): the file to append to
        text (str): the text to append
    """
    with open(filename, mode='w', encoding="UTF=8") as f:
        return(f.write(text))
