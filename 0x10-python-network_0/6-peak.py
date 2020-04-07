#!/usr/bin/python3
""" Function to find a peak """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        middle = len(list_of_integers) // 2
        if (list_of_integers[middle] >= list_of_integers[middle + 1]) and \
                (list_of_integers[middle] >= list_of_integers[middle - 1]):
            return list_of_integers[middle]
