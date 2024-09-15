#!/usr/bin/python3
""" Module that returns "True" if object is class instance, else "False" """


def is_same_class(obj, a_class):
    """ Method: returns value based on instance of class """
    return (type(obj) is (a_class))
