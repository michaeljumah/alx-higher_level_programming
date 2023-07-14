#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """ a private class attribute"""
    __nb_objects = 0
    def __init__(self, id=None):
        """__inti__:class constructo
        Args:
            id (int): any integer
        """
        if id is not None:
            self.id = id
        else:
            self.id = __nb_objectives + 1
