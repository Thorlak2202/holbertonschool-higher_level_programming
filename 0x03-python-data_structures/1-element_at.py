#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    if idx > i or idx < 0:
        return None
    else:
        return my_list[idx]
