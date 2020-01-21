#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as file:
        count = len((file).readlines(  ))
        return count
