#!/usr/bin/python3
def print_last_digit(number):
    tail_digit = abs(number) % 10
    print("{ }".format(number % 10), end="")
    return (tail_digit)
