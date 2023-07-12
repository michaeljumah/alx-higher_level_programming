#!/usr/bin/python3
"""Defines a function that returns an object (Python data structure) represented by a JSON string"""
import json



def from_json_string(my_str):
    """returns an object represented by a json string
    Args:
        my_str (object):python data structure
    """
    return json.loads(my_str)
