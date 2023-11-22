#!/usr/bin/python3
"""unittest for base.py"""

import unittest
from models.base import Base
import json

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

if __name__ == '__main__':
    unittest.main()
