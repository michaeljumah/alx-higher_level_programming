#!/usr/bin/python3
"""Defines a json to string function"""
import json


def from_json_string(my_str):
    """Return a python object represention of a json string"""
    return json.loads(my_str)
