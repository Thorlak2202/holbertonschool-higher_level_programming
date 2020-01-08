#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            my_list
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print('')
    return(j)
