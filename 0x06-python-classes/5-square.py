#!/usr/bin/python3
i = 0
j = 0


class Square:
    """this is a class"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise TypeError
        except ValueError:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            self.__size = value
        else:
            print("size must be an integer", end="")
            raise TypeError

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print('')
        else:
            print("")
