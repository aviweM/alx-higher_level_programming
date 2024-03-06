#!/usr/bin/python3


"""Find a Peak in a List"""


def find_peak(list_of_integers):

    """Find a Peak in a list

    Args:
        list_of_integers
    Returns:
        value or None
    """
    loint = list_of_integers
    if loint == []:
        return None
    total = len(loint)
    if total == 1:
        return loint[0]
    elif total == 2:
        return max(loint)
    middle = int(total / 2)
    peak = loint[middle]
    if peak > loint[middle - 1] and peak > loint[middle + 1]:
        return peak
    elif peak < loint[middle - 1]:
        return find_peak(loint[:middle])
    else:
        return find_peak(loint[middle + 1:])
