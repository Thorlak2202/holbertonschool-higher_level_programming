#!/usr/bin/python3

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class Testrectangle(unittest.TestCase):
    """ """

    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_subclass(self):
        self.assertTrue( issubclass(Rectangle, Base))

    def test_parameters(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 5)
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

"""Task 3 """
def test_string(self):
    with self.assertRaises(TypeError):
        R1 = Rectangle(1.01, 3)
    with self.assertRaises(TypeError):
        R1 = Rectangle(1.01, 3)

    def test_type_param(self):
        """Task 3 """

        """ WIDTH TESTING """
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
            raise TypeError()
        with self.assertRaises(ValueError):
            R2 = Rectangle(-234234242, 45)
            raise ValueError()
        with self.assertRaises(TypeError):
            R3 = Rectangle("", 4)
            raise TypeError()
        with self.assertRaises(TypeError):
            R4 = Rectangle(True, 4)
            raise TypeError()

        """ HEIGHT TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1.76)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, "Hello")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, -4798576398576)
            raise ValueError()

        """ X TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1.50)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 7, -4798576398576)
            raise ValueError()

        """ Y TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1, 1.53)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, 5, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()

    def test_str(self):
        """Task #6"""
        string = "[Rectangle] (1) 0/0 - 1/1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            R1 = Rectangle(1, 1, )
        print(R1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base_nb__objects = 0
        string = "[Rectangle] (12) 2/1 - 4/6"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            R1 = Rectangle(4, 6, 2, 1, 12)
        print(R1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base_nb__objects = 0
        string = "[Rectangle] (1) 1/0 - 5/5"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            R2 = Rectangle(5, 5, 1)
        print(R2)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    """TASK 8"""
    def test_rectangle_update(self):
        """
        Test a rectangle with *args
        """
        instance_rectangle = Rectangle(1, 1, 1, 1)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        instance_rectangle.update(3)
        self.assertEqual(instance_rectangle.id, 3)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (3) 1/1 - 1/1")
        instance_rectangle.update(width=7)
        self.assertEqual(instance_rectangle.width, 7)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (3) 1/1 - 7/1")
        instance_rectangle.update(height=6)
        self.assertEqual(instance_rectangle.height, 6)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (3) 1/1 - 7/6")
        instance_rectangle.update(x=2)
        self.assertEqual(instance_rectangle.x, 2)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (3) 2/1 - 7/6")
        instance_rectangle.update(y=3)
        self.assertEqual(instance_rectangle.y, 3)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (3) 2/3 - 7/6")
        instance_rectangle_1 = Rectangle(5, 5, 5, 5)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (2) 5/5 - 5/5")
        instance_rectangle_1.update(*[10])
        self.assertEqual(instance_rectangle_1.id, 10)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (10) 5/5 - 5/5")
        instance_rectangle_1.update(*[10, 9])
        self.assertEqual(instance_rectangle_1.width, 9)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (10) 5/5 - 9/5")
        instance_rectangle_1.update(*[10, 9, 8])
        self.assertEqual(instance_rectangle_1.height, 8)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (10) 5/5 - 9/8")
        instance_rectangle_1.update(*[10, 9, 8, 7])
        self.assertEqual(instance_rectangle_1.x, 7)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (10) 7/5 - 9/8")
        instance_rectangle_1.update(*[10, 9, 8, 7, 6])
        self.assertEqual(instance_rectangle_1.y, 6)
        self.assertEqual(instance_rectangle_1.__str__(), "[Rectangle] (10) 7/6 - 9/8")


    """TASK 9"""
    def test_update_kwargs(self):
        """
        Test a rectangle with **kwargs
        """
        instance_rectangle = Rectangle(1, 1, 1, 1)
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        instance_rectangle.update(**{'height': 10})
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (1) 1/1 - 1/10")
        instance_rectangle.update(**{'width': 9, 'x': 8})
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (1) 8/1 - 9/10")
        instance_rectangle.update(**{'y': 1, 'width': 2, 'x': 3, 'id': 89})
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (89) 3/1 - 2/10")
        instance_rectangle.update(**{'x': 1, 'height': 2, 'y': 3, 'width': 4})
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        instance_rectangle.update(**{'wow': 3, 'hey': 'wow'})
        self.assertEqual(instance_rectangle.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        instance_rectangle.update({'x': 10, 'height': 8})
        self.assertIs(type(instance_rectangle.id), dict)


"""Test 13"""


def test_to_dict(self):
        """ """
        r = Rectangle(10, 2, 1, 9)
        self.assertIs(type(r.to_dictionary()), dict)
        self.assertEqual(r.to_dictionary(), {'x': 1, 'y': 9,
                                             'id': 1, 'height': 2,
                                             'width': 10})

if __name__ == "_main_":
    unittest.main()
