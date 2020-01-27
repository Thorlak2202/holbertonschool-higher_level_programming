#!/usr/bin/python3
"""
Base class module
"""
import json


class Base:
    """a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON String representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the JSON string representation list"""
        if json_string is None or json_string is "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the list to a file"""
        filename = (cls.__name__) + ".json"
        obj_list = []
        if list_objs is None or len(list_objs) == 0:
            obj_list = []
        else:
            for i in list_objs:
                obj_list.append(i.to_dictionary())
        string_j = Base.to_json_string(obj_list)
        with open(filename, 'w') as file:
            file.write(string_j)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads a file"""
        filename = cls.__name__ + ".json"
        data = []
        try:
            with open(filename) as file:
                data = cls.from_json_string(file.read())
            for i in enumerate(data):
                data[i] = cls.create(**data[i])
        except:
            pass
        return data
