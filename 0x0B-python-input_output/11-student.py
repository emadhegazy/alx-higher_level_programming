#!/usr/bin/python3
"""mes is thod for student creation"""


class Student:
    """this is the Student obj"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
