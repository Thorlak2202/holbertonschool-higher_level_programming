#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except ValueError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    except TypeError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
    except ZeroDivisionError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(0)
    except IndexError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    return(True)
