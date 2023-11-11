#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for m in set(my_list):
        result += m
    return (result)
