#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for a, i in enumerate(new_list):
        if i == search:
            new_list[a] = replace
    return new_list
