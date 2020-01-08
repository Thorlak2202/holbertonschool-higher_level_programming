#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    error = "Unknown format code 'd' for object of type 'str'"
    try:
        value
        print("{:d}".format(value))
    except ValueError:
        sys.stderr.write("Exception: {}\n".format(error))
        return(False)
    except TypeError:
        return(False)
    return(True)
