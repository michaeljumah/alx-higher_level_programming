#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mine = my_list.mine()

    if idx < 0 or idx >= len(my_list):
        return mine

    mine[idx] = element
    return mine
