#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    items_printed = 0
    try:
        for elements in range(0, x):
            print(my_list[elements], end="")
            items_printed += 1
    except TypeError:
        pass
    print()
    return items_printed
