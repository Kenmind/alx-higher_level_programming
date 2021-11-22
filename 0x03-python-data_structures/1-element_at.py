#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        i = my_list[idx]
        idx = my_list.index(i)
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return(my_list[idx])
