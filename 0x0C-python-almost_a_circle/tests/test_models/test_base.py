#!/usr/bin/python3
"""
Module for unittests for the Base class
"""
import unittest
from models.base import Base
import os


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

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, -500.456)
        bo = Base(None)
        self.assertEqual(bo.id, 0.000001957)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 'cat145')
        bo = Base(None)
        self.assertEqual(bo.id, 'dog')

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

""" test Task 17 """


class TestBase(unittest.TestCase):

    def test_from_json_string(self):
        string_js = '[{"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}, \
            {"id": 7, "width": 1, "height": 7, "x": 6, "y": 5}]'
        jsonconv = Base.from_json_string(string_js)
        self.assertTrue(type(jsonconv) is list)
        self.assertEqual(len(jsonconv), 2)

if __name__ == "_main_":
    unittest.main()
