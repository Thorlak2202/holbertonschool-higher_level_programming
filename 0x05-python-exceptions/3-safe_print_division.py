#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if a != 0 and b != 0:
            result = a / b
        else:
            result = None
    except ZeroDivisionError:
        return(None)
        pass
    finally:
        print("Inside result: {}".format(result))
    return(result)
