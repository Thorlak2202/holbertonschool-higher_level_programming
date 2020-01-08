#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if a != 0 and b != 0:
            result = a / b
        else:
            result = None
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return(result)
