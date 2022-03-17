#!/usr/bin/python3
# Peak module


def find_peak(list_of_integers):
    """Finds peak
    Args:
        list_of_integers (list): list of integers
    """
    len_lst = len(list_of_integers)
    if len_lst < 3:
        return None
    p = list_of_integers[1]
    for i in range(1, len_lst):
        if list_of_integers[i] >= p:
            p = list_of_integers[i]
    return p
