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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation
        json_string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is 'Rectangle':
            inst = cls(4, 2)
        elif cls.__name__ is 'Square':
            inst = cls(4)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_inst = []
        with open("{}.json".format(cls.__name__), 'r') as f:
            l1 = cls.from_json_string(f.read())

        for item in l1:
            list_inst.append(cls.create(**item))
        return list_inst
