#!/usr/bin/python3
""" Module that returns "True" is the object is an instance of a
class that inherited from, the specified class, else "False" """


def is_kind_of_class(obj, a_class):
    """ Method: returns value based on instance of class """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
