#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self._height = height
        self._width = width

    def area(self):
        return(self._height * self._width)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self._width, self._height))


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("Size", size)
        self._size = size

    def area(self):
        return(self._size**2)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self._size, self._size))
