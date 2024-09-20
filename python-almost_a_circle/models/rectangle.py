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
            (id) used to call __init__ logic from super class
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
            return (self.__width)

        @property
        def height(self):
            """ Retrieves the height of the rectangle
            Returns the height of the rectangle """
            return (self.__height)

        @property
        def x(self):
            """ Retrieves the x-coordinate of the rectangle
            Returns the x-coordinate of the rectangle """
            return (self.__x)

        @property
        def y(self):
            """ Retrieves the y-coordinate of the rectangle
            Returns the y-coordinate of the rectangle """
            return (self.__y)

        @width.setter
        def width(self, value):
            """ Sets the width of the rectangle """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if (width <= 0):
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """ Sets the height of the rectangle """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if (height <= 0):
                raise ValueError("height must be > 0")
            self.__height = height

        @x.setter
        def x(self, value):
            """ Sets the x-coordinate of the rectangle """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if (x < 0):
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """ Sets the y-coordinate of the rectangle """
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if (y < 0):
                raise ValueError("y must be >= 0")
            self.__y = value
