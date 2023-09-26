#!/usr/bin/python3
"""this is to define a class Square."""


class Square:
    """this is to represent a square."""

    def __init__(self, size=0):
        """this is to initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this is to return the current area of the square."""
        return (self.__size * self.__size)
