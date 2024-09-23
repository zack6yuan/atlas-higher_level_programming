#!/usr/bin/python3
""" Module "Rectangle" that inherits from "Base" """
from models.base import Base


class Rectangle(Base):
    """ Class "Rectangle" that inherits from "Base" class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Method: Initialize Rectangle class
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
        """ Method: Retrieves the width of the rectangle
        Returns the width of the rectangle """
        return (self.__width)

    @property
    def height(self):
        """ Method: Retrieves the height of the rectangle
        Returns the height of the rectangle """
        return (self.__height)

    @property
    def x(self):
        """ Method: Retrieves the x-coordinate of the rectangle
        Returns the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                x-coordinate of the rectangle """
        return (self.__x)

    @property
    def y(self):
        """ Method: Retrieves the y-coordinate of the rectangle
        Returns the y-coordinate of the rectangle """
        return (self.__y)

    @width.setter
    def width(self, value):
        """ Method: Sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Method: Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Method: Sets the x-coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Method: Sets the y-coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method: Retrieves the area of the rectangle
        Returns the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):  # in progress
        """ Method: prints in stdout the Rectangle
        instance with the character "#" """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ Method: returns rectangle properties according to format """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """ Method: assigns arguments to each attribute

        Attributes:
            1st argument: (id) attribute
            2nd argument: (width) attribute
            3rd argument: (height) attribute
            4th argument: (x) attribute
            5th argument: (y) attribute
        """
        list = ["id", "width", "height", "x", "y"]

    def to_dictionary(self):
        """ Method: returns the dictionary
        representation of a Rectangle """
        rectangle_dictionary = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return (rectangle_dictionary)
