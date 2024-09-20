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
