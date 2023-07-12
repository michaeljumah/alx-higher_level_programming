#!/usr/bin/python3
"""Defines  a function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """appends a string with utf-8 at the end of the file.
    Args:
        filename (str):the file to be appended
        text (str): the characters to append to the file
    """
    with open(filename, 'a', encoding = 'utf-8') as f:
        return f.write(text)
