#!/usr/bin/python3
"""
===========================
the module with class MyList
===========================
"""


class MyList(list):
    """the Class with method print_sorted"""
    pass

    def print_sorted(self):
        """the Methot that sorted a list"""

        print(sorted(list(self)))
