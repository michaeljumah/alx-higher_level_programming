#!/usr/bin/python3
"""Defines a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ saves_to_json_file writes an Object to a text file
    Args:
        my_obj (obj): any object
        filename (str):file name
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
