#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(0, -1)
    print(r1.id)

    r2 = Rectangle(-7, 10)
    print(r2.id)

    r3 = Rectangle(-1, -5, -9, -8, 12)
    print(r3.id)
