#!/usr/bin/python3
i = 0
j = 0
k = 0
l = 0


class Square:
    """this is a class"""
    def __init__(self, size=0, position=(0, 0)):
        try:
            self.__size = size
            self.__position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
                print("position must be a tuple of 2 positive integers")
                raise TypeError
        self.__position(value)

    def my_print(self):
        if self.__size != 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')
        else:
            print("")
