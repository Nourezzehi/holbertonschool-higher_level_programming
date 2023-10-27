#!/usr/bin/python3
"""base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
