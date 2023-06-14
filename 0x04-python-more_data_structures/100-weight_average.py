#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mul = 0
        sum_d = 0
        for x in my_list:
            mul += x[0] * x[1]
        for x in my_list:
            sum_d += x[1]
        return mul/sum_d
