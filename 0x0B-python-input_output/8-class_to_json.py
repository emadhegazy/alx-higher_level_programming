#!/usr/bin/python3
"""
this is the Module for class_to_json method.
"""


def class_to_json(obj):
    """
        will return dictionary representation with simple data structure.
    """
    return obj.__dict__
