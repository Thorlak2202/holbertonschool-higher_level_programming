#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as file:
        text = file.read()
    print("{}".format(text))
