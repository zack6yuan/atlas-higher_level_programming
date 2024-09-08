#!/usr/bin/python3
""" Module that defines a class "square" """


class Square:
    """ Class "square" with instantation size """
    def __init__(self, size=0):
        """ Raises Type Error: if size is not type "int" """
        """ Raises ValueError: if size < 0 """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """ Returns the area of the square """
        return (self.__size ** 2)
