#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = (len(my_list))
    for j in range(0, len(my_list)):
        i -= 1
        print("{:d}".format(my_list[i]))
