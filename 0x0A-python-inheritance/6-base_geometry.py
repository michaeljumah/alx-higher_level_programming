#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Public instance method are:Returns area"""
    def area(self):
        raise Exceptions('area() is not implemented')
