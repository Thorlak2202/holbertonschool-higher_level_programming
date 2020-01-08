#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        value
        print("{:d}".format(value))
    except ValueError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
    except TypeError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
    return(True)
