#!/usr/bin/python3
""" import from 7-base_geometry """

Rectangle = __import__('9-rectangle').Rectangle
"""
Return true if object is an instance
of a class
"""


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """initialize data"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ def area"""
        return (self.__size ** 2)

    def __str__(self):
        """ return str"""
        return "[Square] {}/{}".format(self.__size, self.__size)
