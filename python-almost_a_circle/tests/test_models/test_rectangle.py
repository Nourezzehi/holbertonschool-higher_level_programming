#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):

        self.rectangle = Rectangle(width=5, height=10, x=2, y=3, id=1)

    def test_constructor(self):
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_setters(self):
        self.rectangle.x = 7
        self.assertEqual(self.rectangle.x, 7)
        self.rectangle.y = 8
        self.assertEqual(self.rectangle.y, 8)
        self.rectangle.height = 15
        self.assertEqual(self.rectangle.height, 15)
        self.rectangle.width = 8
        self.assertEqual(self.rectangle.width, 8)

    def test_invalid_setters(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -1
        with self.assertRaises(ValueError):
            self.rectangle.height = 0
        with self.assertRaises(ValueError):
            self.rectangle.width = -2
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid" 
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
        
    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50) 

if __name__ == '__main__':
    unittest.main()
