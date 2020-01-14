#!/usr/bin/python3
class Rectangle:
    """this is a class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        if type(height) != int:
            raise TypeError("Height must be an integer")
        self.__width = width
        if type(width) != int:
            raise TypeError("width must be an integer")
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        to_print = []
        if self.__height != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    to_print.append(str(self.print_symbol))
                if i < (self.__height)-1:
                    to_print.append('\n')
        return''.join(to_print)

    def __repr__(self):
        repr_rectangle = []
        repr_rectangle.append("Rectangle(" + str(self.__width))
        repr_rectangle.append(", " + str(self.__height) + ')')
        return ''.join(repr_rectangle)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
