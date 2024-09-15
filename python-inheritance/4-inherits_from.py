#!/usr/bin/python3
""" Module that returns "True" if the object is an instance of a 
class that inherited from the specified class, else "False" """


def inherits_from(obj, a_class):
    """ Method: returns value based on instance of class """
    return (issubclass(type(obj), (a_class)) and (type(obj) is not (a_class)))
