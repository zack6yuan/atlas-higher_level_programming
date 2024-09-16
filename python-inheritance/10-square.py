#!/usr/bin/python3
""" Module that defines a class "Square"
that inherits from Rectangle (9-rectangle.py) """


class Square(Rectangle):
    """ Class "Square" is created"
    inherits from "Rectangle """
    def __init__(self, size):
        """ instantiation with "size" """
        self.integer_validator("size", size):
        self.__size = size

    def area(self):
        """ Retreives the area
        Returns the area """
        return (self.__size * self.__size)
