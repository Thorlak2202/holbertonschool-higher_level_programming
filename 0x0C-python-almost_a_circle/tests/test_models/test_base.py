#!/usr/bin/python3
"""
Module for unittests for the Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


def test_pep8_conformance_base(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


"""=======task1======="""


class TestBaseClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    def test_id_string(self):
        bo = Base("st")
        self.assertEqual(bo.id, "st")
        bo = Base("st2")
        self.assertEqual(bo.id, "st2")

    def test_id_float(self):
        bo = Base(0.5)
        self.assertEqual(bo.id, 0.5)
        bo = Base(2.4)
        self.assertEqual(bo.id, 2.4)


"""========END TASK 1======"""
"""========TASK 10 ========"""


class TestSquare(unittest.TestCase):
    def test_id(self):
        S1 = Square(1)
        S2 = Square(1, 2)
        S3 = Square(1, 2, 3)
        S4 = Square(1, 2, 3, 4)
        self.assertEqual(S2.x, 2)
        self.assertEqual(S3.y, 3)
        self.assertEqual(S4.id, 4)

    def test_ValueError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 14, -5)

    def test_TypeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("22")
            Square(True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "yup")
            Square(10, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 11, "hi")
            Square(10, 15, False)

    def test_str(self):

        Base._Base__nb_objects = 0
        S1 = Square(3)
        S2 = Square(3, 4)
        S3 = Square(3, 4, 5)
        self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 3")
        self.assertEqual(S2.__str__(), "[Square] (2) 4/0 - 3")
        self.assertEqual(S3.__str__(), "[Square] (3) 4/5 - 3")
"""=======END TASK 10 ======="""

"""=======TASK 15 ========"""


def test_dictionary(self):
        """Comment"""
        re1 = Rectangle(10, 7, 2, 8, 70)
        dictionary = re1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

        def test_dictionary_empty(self):
            """Comment"""
        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, "[]")

        obj = None
        json_dictionary = Base.to_json_string(obj)
        self.assertEqual(json_dictionary, "[]")

"""========TASK 15 ========"""
"""======= TASK 17 ========="""


def test_from_json_string(self):
    string_js = '[{"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}, \
        {"id": 7, "width": 1, "height": 7, "x": 6, "y": 5}]'
    jsonconv = Base.from_json_string(string_js)
    self.assertTrue(type(jsonconv) is list)
    self.assertEqual(len(jsonconv), 2)

"""====== END TASK 17 ======"""

if __name__ == "_main_":
    unittest.main()
