#!/usr/bin/python3
""" Module that returns list of available attributes + object methods """


def lookup(obj):
    """ Method: returns availabla attributes and methods list """
    return (dir(obj))
