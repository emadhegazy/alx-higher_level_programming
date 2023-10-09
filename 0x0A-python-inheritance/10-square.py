#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
the module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """the Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """the method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """the rectangle area"""

        return self.__size ** 2
