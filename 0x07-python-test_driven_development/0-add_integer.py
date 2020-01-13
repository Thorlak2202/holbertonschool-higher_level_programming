#!/usr/bin/python3
"""
function o add integers
"""

def add_integer(a, b=98):
    """ adds two integers
    Args:
        a (int): first value mus be an integer or float
        b (int): 98 if no value is sent
    Returns:
        sum of two integers or float
    Errors Raised:
        TypeError: if a or b are not integers nor float
    """    
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
