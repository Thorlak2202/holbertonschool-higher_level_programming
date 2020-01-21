#!/usr/bin/python3
def number_of_lines(filename=""):
    count = len(open(filename).readlines(  ))
    return count
