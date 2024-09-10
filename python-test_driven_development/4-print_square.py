#!/usr/bin/python3
""" This is a module that prints a square with the character "#" """


def print_square(size):
    """ Method: prints square with character "#" """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if not isinstance(size, float):
        raise TypeError("size must be an integer")
    for x in range(size):
        print("#" * size)
