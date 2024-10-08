#!/usr/bin/python3
""" Module that defines a class "square" based on "5-square.py" """


class Square:
    """ class "Square" with private instance attribute "size" """
    """ Raises TypeError: if size is not type int """
    """ Raises ValueError: if size < 0 """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Retrieves size of the square """
        """ Returns size of the square """
        return (self.__size)

    @size.setter
    def size(self, value)
        """ Sets the size of the square """
        """ Raises TypeError: if size is not type "int" """
        """ Raises ValueError: if size < 0 """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def posititon(self):
        """ Retrieves the position of the square """
        """ Returns the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Sets the position of the square """
        """ Raises TypeError: if size is not type "int" """
        """ Raises ValueError: if size < 0 """
        if not isinstance(value, tuple)

    def area(self)
        """ Retrieves area of the square """
        """ Returns area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ prints square to stdout with char "#" """
        """ if (size == 0), prints empty line """
        if (self.__size == 0):
            print()
        else: