#!/usr/bin/python3
""" This is a module that defines a rectangle based on "1-rectangle.py" """


class Rectangle:
    """ Class "Rectangle" """
    """ Raises TypeError: if width is not type "int" """
    """ Raises ValueError: if width < 0 """
    def __init__(self, width=0, height=0):
        """ New rectangle is created """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ Retreives the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        """ Raises TypeError: if width is not type "int" """
        """ Raises ValueError: if (width < 0) """
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
        """Sets the height of the rectangle """
        """ Raises TypeError: if height is not type "int" """
        """ Raises ValueError: if (height < 0) """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Retrieves the area of the rectangle """
        """ Returns the area of the rectangle """
        return (self.__size ** 2)

    def perimeter(self)
        """ Retrieves the perimeter of the rectangle """
        """ Returns the perimeter of the rectangle """
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        else:
            return (self.__width + self.__height) * 2
