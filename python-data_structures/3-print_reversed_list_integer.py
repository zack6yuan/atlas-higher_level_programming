#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list[::-1]
    for digit in (reverse):
        print("{:d}".format(digit))
