#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """inherits of base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""

        id = super().__init__(id)
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    @property
    def x(self):
        """x-get_method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x-set_method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y-get_method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y-set_method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def height(self):
        """height-get_method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height-get_method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """width-get_method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width-set_method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def area(self):
        """rectangle's area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """prints the rectangle"""
        for i in range(self.__y):
            print()
        for h in range(self.__height):
            for w in range(self.__width + self.__x):
                if w < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()
