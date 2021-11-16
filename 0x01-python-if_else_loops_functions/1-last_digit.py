#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_neg = number % -10
last_pos = number % 10
if number >= 0 and last_pos > 5:
    print("The last digit of {} is {} and is\
 greater than 5".format(number, last_pos))
elif number >= 0 and last_pos > 0 and last_pos < 6:
    print("Last digit of {} is {} and is less \
than 6 and not 0".format(number, last_pos))
elif number >= 0 and last_pos == 0:
    print("Last digit of {} is {} and is less than \
6 and is 0".format(number, last_pos))
elif number < 0 and last_neg == 0:
    print("Last digit of {} is {} and is less than 6\
 and is 0".format(number, last_neg))
elif number < 0 and last_neg < 0:
    print("Last digit of {} is {} and is less than 6\
 and not 0".format(number, last_neg))
