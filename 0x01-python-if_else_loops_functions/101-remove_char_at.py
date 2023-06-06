#!/usr/bin/python3
def remove_char_at(str, n):
    """Deletes the character at the n position of the str
    This function creates a copy of the string, deletes
    a position of the passed string and returns a string
    without the deleted position
    Parameters
    ----------
    str : str
        The string from which the position needs to be removed
    n : int
        The position of the string to be deleted
    Returns
    -------
    str
        The copy of the string without the deleted position
    """

    _new_string = ""

    for i in range(len(str)):
        if i != n:
            _new_string += str[i]

    return _new_string
