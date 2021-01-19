#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Return true if object is an instance
of a class
"""


class Rectangle(BaseGeometry):
    """ rectangle class """
    def __init__(self, width, height):
        """initialize data"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """overwrite function"""
        return self.__width * self.__height

    def __str__(self):
        """ returns str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
