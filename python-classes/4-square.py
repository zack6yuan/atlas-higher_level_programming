#!/usr/bin/python3
""" Module that defines a class "square" """


class Square:
    """ Class "square" with instantation "size" """
    """ Raises TypeError: if size is not type int """
    """ Raises ValueError: if size < 0 """
    def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    self.__size = size

@property
def size(self, value):
    """ Retrieves size of the square """
    """ Returns size of the square """
    return (self.__size)

@size.setter
def size(self, value):
    """ Sets the size of the square """
    """ Raises Type Error: if size is not type "int" """
    """ Raises ValueError: if size < 0 """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    self.__size = value

def area(self):
    """ Retrieves area of the square """
    """ Returns area of the square """
    return (self.__size ** 2)
