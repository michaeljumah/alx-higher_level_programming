#!/usr/bin/python3
#0-safe_print_list.py

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
        for elements in mylist[:x]:
            print(elements, end=' ')
            items_printed += 1
    except IndexError:
        pass
    finally:
        print()
    return items_printed
