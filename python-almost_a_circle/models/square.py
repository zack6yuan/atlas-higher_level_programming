#!/usr/bin/python3
""" Module "Square" that inherits from "Rectangle" """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class "Square" that inherits from "Rectangle" class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Method: Initialize Square class
        Attributes:
            (self) reference to new object
            (width) type "int" representing square width
            (height) type "int" representing square height
            (x) type "int" representing x-coordinate of position
            (y) type "int" representing y-coordinate of position
            (id) used to call __init__ logic from super class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Method: method that overloads
        and returns according to format"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ Method: Retrieves the size of the square
        Returns the size of the square """
        return (self.__width)

    @size.setter
    def size(self, value):
        """ Method: Sets the size of the square """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value
