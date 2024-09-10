#!/usr/bin/python3
""" This is a module that prints the first and last name from input """


def say_my_name(first_name, last_name):
    """ Method: prints first and last name from input """
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
