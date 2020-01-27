#!/usr/bin/python3
"""
Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string representation of a square"""
        return \
            ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
             self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """updates attributes based on the args"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary"""
        dictio = {}
        dictio['id'] = self.id
        dictio['size'] = self.size
        dictio['x'] = self.x
        dictio['y'] = self.y
        return dictio

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size getter"""
        self.width = value
        self.height = value
