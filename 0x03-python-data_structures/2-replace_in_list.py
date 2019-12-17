#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = len(my_list)
    if idx > i or idx < 0:
        new_list = my_list
        return new_list
    else:
        new_list = my_list
        my_list[idx] = element
        return new_list
