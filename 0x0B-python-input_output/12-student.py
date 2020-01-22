#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or type(attrs) != list:
            return self.__dict__
        for i in attrs:
            if type(i) != str:
                return self.__dict__
        return {a: self.__dict__[a] for a in self.__dict__ if a in attrs}
