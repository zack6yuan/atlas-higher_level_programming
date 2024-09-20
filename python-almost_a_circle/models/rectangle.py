#!/usr/bin/python3
""" Module "Rectangle" that inherits from "Base" """
from models.base import Base

class Rectangle(Base):
    """ Class "Rectangle" that inherits from "Base" class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle class

        Attributes:
            (self) reference to new object
            (width) type "int" representing rectangle width
            (height) type "int" representing rectangle height
            (x) type "int" representing x-coordinate of position
            (y) type "int" representing y-coordinate of position
            (id) used to call super class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ Retrieves the width of the rectangle
            Returns the width of the rectangle """
            return self.__width

        @property
        def height(self):
            """ Retrieves the height of the rectangle
            Returns the height of the rectangle """
            return self.__height

        @property
        def x(self):
            """ Retrieves the x-coordinate of the rectangle
            Returns the x-coordinate of the rectangle """
            return self.__x

        @property:
        def y(self):
            """ Retrieves the y-coordinate of the rectangle
            Returns the y-coordinate of the rectangle """
            return self.__y