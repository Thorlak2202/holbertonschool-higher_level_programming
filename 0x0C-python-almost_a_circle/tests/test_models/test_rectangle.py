#!/usr/bin/python3
"""Task 2 """
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrectangle(unittest.TestCase):
    """ """

    def test_subclass(self):
        self.assertTrue( issubclass(Rectangle, Base))

    def test_parameters(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 4)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
                r4 = Rectangle()

if __name__ == "_main_":
   unittest.main()
