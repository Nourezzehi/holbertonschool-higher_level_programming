#!/usr/bin/python3
"""unittest for base.py"""

import unittest
from models.base import Base 

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

if __name__ == '__main__':
    unittest.main()