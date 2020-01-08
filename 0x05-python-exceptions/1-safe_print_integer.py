#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value
        print("{:d}".format(value))
    except ValueError:
        return(False)
    except TypeError:
        return(False)
    return(True)
