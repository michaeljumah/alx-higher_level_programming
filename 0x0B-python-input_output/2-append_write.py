#!/usr/bin/python3
"""Defines  a function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """a function that appends a string with utf-8.
    Args:
        filename (str):the file to be appended
        text (str): the characters to append to the file
    Returns:
         the number of characters added
    """
    with open(filename, 'a', encoding = 'utf-8') as f:
        return f.write(text)
