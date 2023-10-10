#!/usr/bin/python3
"""getter method"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")"""
        self.__size = size

    def size(self):
        """getter"""

        return self.__size

    def size(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of a square"""

        return self.__size ** 2
