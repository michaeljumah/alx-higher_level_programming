#!/usr/bin/python3
"""Defines a json to string function"""
import json



def from_json_string(my_str):
    """Returns a python object represented by a json string"""
    return json.loads(my_str)
