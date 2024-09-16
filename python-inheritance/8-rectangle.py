#!/usr/bin/python3
""" Module that defines a class "Rectangle"
    Inherits from "7-base_geometry.py" """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ created class "Rectangle" """
    """ Inherits from "7-base_geometry.py" """
    def __init__(self, width, height):
        """ Method: width and height (positive integers)
        validated by "integer_validator" """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
