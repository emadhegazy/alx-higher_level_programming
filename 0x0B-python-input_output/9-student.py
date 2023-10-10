#!/usr/bin/python3
"""
    this is Module for class Student.
"""


class Student:
    """
        this is a class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            to Initialise Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            to retrieve a dictionary representation of Student.
        """
        return self.__dict__
