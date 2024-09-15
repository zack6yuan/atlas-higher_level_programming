#!/usr/bin/python3
""" Module that returns the list of available attributes and methods of a object """


def lookup(obj):
    """ Method: returns availabla attributes and methods list """
    return (dir(obj))
