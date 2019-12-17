#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    if i == 0:
        return None
    else:
        my_list = sorted(my_list)
        return my_list[i-1]
