#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the argument list passed to the program
    The program takes the arguments starting from the second
    and prints the number of arguments and their value
    """
    import sys
    n = len(sys.argv)
    if n == 1:
        print("{:d} arguments.".format(n - 1))
    elif n == 2:
        print("{:d} argument:".format(n - 1))
    else:
        print("{:d} arguments:".format(n - 1))
    for i in range(1, n):
        print("{:d}: {:s}".format(i, sys.argv[i]))
