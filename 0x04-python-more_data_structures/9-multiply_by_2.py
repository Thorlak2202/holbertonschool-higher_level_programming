#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    duplicate = a_dictionary.copy()
    for double in duplicate:
        duplicate[double] = duplicate[double] * 2
    return duplicate
