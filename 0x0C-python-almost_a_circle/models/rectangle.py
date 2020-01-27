#!/usr/bin/python3
"""
recangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """prints the rectangle"""
        if self.__width != 0 and self.__height != 0:
            for y in range(self.__y):
                print('')
            for i in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print('')
        else:
            print("")

    def __str__(self):
        """overrides the str and represents the rectangle"""
        return \
            ("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
             self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updates attributes of the rectangle based on the args"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary"""
        dictio = {}
        dictio['id'] = self.id
        dictio['width'] = self.width
        dictio['height'] = self.height
        dictio['x'] = self.x
        dictio['y'] = self.y
        return dictio

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
