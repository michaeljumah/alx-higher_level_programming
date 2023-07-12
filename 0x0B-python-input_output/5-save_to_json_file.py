#!/usr/bin/python3
"""Defines a function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation:
    Args:
        my_obj (obj):data to manipulate
        filename (str):file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
