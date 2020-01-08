#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            my_list
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print('')
            return(i)
    print('')
    return(x)
