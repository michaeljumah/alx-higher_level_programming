#!/usr/bin/python3
"""Defines a function that returns the dictionary description """


def class_to_json(obj):
    """class_to_json:returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj (obj):any obj
    """
    return obj.__dict__
