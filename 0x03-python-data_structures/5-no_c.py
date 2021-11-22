#!/usr/bin/python3
def no_c(my_string):
    n_string = [n for n in my_string if n != 'c' and n != 'C']
    return ("".join(n_string))
