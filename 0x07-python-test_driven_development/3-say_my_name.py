#!/usr/bin/python3
"""
function to print names
"""


def say_my_name(first_name, last_name=""):
    """ prints a name
    Args:
        first_name (str): first name must always be str
        last_name (str): last name or empty if nothing is sent
    Returns:
        prints the name
    Errors Raised:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
