#!/usr/bin/python3
""" Module that defines a class "BaseGeometry" """


class BaseGeometry:
    """ BaseGeometry class created """
    def area(self):
        """ Raises Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Raises TypeError, if "value" is not type "int" """
        """ Raises ValueError, if "value" is < 0 """
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if (value < 0):
            raise ValueError("<name> must be greater than 0")
