#!/usr/bin/python3
import sys

if __name__ == '__main__':
    d = sys.argv
    dl = len(d)
    sum = 0

    if dl > 1:
        for i in range(1, dl):
            sum += int(d[i])

    print(sum)
