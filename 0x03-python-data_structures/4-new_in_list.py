#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = len(my_list)
    list_copy = my_list[:]
    if idx >= i or idx < 0:
        return my_list
    else:
        list_copy[idx] = element
        return list_copy
