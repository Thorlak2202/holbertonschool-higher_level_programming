#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == 0:
            return my_list
        elif i != search:
            new_list.append(i)
        else:
            new_list.append(replace)
    return(new_list)
