#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def valid_tests(self):
        # positive testing
        self.assertEqual(max_integer([0, 25, 55, 98]), 98)
        self.assertEqual(max_integer([1, 2, 98, 3]), 98)

    def negatives(self):
    # negative testing
        self.assertEqual(max_integer([-98, -55, -20, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -98, 3]), 3)

    def strings(self):
    # string testing
        self.assertEqual(max_integer("hello"), 'o')
