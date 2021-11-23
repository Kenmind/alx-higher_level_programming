#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div.append(True)
        elif my_list[i] % 2 != 0:
            div.append(False)
    return div
