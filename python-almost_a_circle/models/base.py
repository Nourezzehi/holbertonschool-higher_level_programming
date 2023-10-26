#!/usr/bin/python3
"""base class"""


class Base:
    """our class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
