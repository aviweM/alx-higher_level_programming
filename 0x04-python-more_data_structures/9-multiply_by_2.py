#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return ({b: a_dictionary[b] * 2 for b in a_dictionary})
