#!/usr/bin/python3
"""Defines a student class """


class Student:
    """represents a student """
    def __init__(self, first_name, last_name, age):
        """__int__:initializes a constructor
        Args:
            self.first_name:first name
            self.last_name: last name
            self.age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a dictionary representation of a student """
        return self.__dict__
