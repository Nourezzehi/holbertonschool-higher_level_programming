#!/usr/bin/python3
"""unittest for base.py"""

import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_instantiation_with_id_none(self):
        obj = Base()
        self.assertEqual(obj.id, 3)

    def test_instantiation_with_id_provided(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_incrementing_id_across_instances(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_valid_input(self):
        input_data = [{'key': 'value'}, {'another_key': 'another_value'}]
        result = Base.to_json_string(input_data)
        expected_result = json.dumps(input_data)
        self.assertEqual(result, expected_result)

    def test_save_to_file(self):
            r1 = Rectangle(10, 7, 2, 8)
            r2 = Rectangle(2, 4)
            s1 = Square(5)
            Base.save_to_file([r1, r2, s1])
            filename = "Base.json"
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            expected_data = [
                r1.to_dictionary(),
                r2.to_dictionary(),
                s1.to_dictionary()
            ]
            self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
