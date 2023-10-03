#!/usr/bin/python3
"""s is to define a class LockedClass"""


class LockedClass:
    """
    this is to Prevent the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """this is to create new instances of Locked Class."""

        self.first_name = "first_name"
