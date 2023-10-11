#!/usr/bin/python3
"""prints the square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise with a given size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""

        return self.__position

    def position(self, value):
        """position setter"""

        if not isinstance(value, tuple) and not isinstance(value[0], int)   \
                and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of a square"""

        return self.__size ** 2

    def my_print(self):
        """prints the square"""

        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(end=" ")
                for i in range(self.__size):
                    print('#', end='')
                print()
