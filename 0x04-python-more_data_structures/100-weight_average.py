#!/usr/bin/python3
def weight_average(my_list):
    if len(my_list) == 0:
        return 0

    t_sum = 0
    t_weight = 0

    for score, weight in my_list:
        t_sum += score * weight
        t_weight += weight

    weighted_average = t_sum / t_weight

    return weighted_average
