#!/usr/bin/python3
""" Module that defines a rectangle based on "0-rectangle.py" """


class Rectangle:
    """ Class "Rectangle" """
    """ Raises TypeError: if width is not type "int" """
    """ Raises ValueError: if width is < 0 """
    def __init__(self, width=0, height=0):
        """ New rectangle is created """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        """ Raises TypeError: if width is not type int """
        """ Raises ValueError: if width < 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        """ Raises TypeError: if height is not type int """
        """ Raises ValueError: if height < 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
