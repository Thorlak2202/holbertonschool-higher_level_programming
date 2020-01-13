#!/usr/bin/python3
"""
function to print a square
"""


def print_square(size):
    """ prints a square
    Args:
        size (int): must always be an int and cannot be less or equal to 0
    Returns:
        prints a square with '#' symbols
    Errors Raised:
        TypeError: if size is not integer
        ValueError: if size is equal or lesser than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
