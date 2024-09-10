#!/usr/bin/python3
""" This is a module that defines a rectangle based on "8-rectangle.py" """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method: New rectangle is created """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Method: Retrieves the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Method: Sets the width of the rectangle """
        """ Raises TypeError: if width is not type "int" """
        """ Raises ValueError: if (width < 0) """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method: Retrieves the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Method: Sets the height of the triangle """
        """ Raises TypeError: if height is not type "int" """
        """ Raises ValueError: if (value < 0) """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method: Retrieves the area of the rectangle """
        """ Returns the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Method: Retrieves the perimeter of the rectangle """
        """ Returns the perimeter of the rectangle """
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ Method: Retrieves str of rectangle """
        """ Returns str of rectangle """
        if ((self.width == 0) or (self.height == 0)):
            return ""  # empty string
        rec_str = ""
        for x in range(self.__height):
            for y in range(self.__width):
                rec_str += str(self.print_symbol)
            if x < self.__height - 1:
                rec_str += "\n"
        return (rec_str)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method: prints message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method: Returns the biggest rectangle based on area """
        """ Raises TypeError: if rect_1 is not an instance of Rectangle """
        """ Raises TypeError: if rect_2 is not an instance of Rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
