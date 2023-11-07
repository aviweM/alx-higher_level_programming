#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_n = my_list[0]
    for u in range(len(my_list)):
        if my_list[u] > max_n:
            max_n = my_list[u]
    return (max_n)
