#!/usr/bin/python3
""" Module that defines a class "square" """


class Square:
    """ Class "square" with instantiation "size" """
    def __init__(self, size=0):
        """ Raises ValueError: if size < 0 """
        """ Raises Type Error: if size is not type "int" """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
