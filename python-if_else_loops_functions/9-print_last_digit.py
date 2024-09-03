#!/usr/bin/python3
def print_last_digit(number):
    tail_digit = abs(number) % 10
    print("{}".format(tail_digit), end="")
    return (tail_digit)
