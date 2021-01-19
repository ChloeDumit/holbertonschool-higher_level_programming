#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Return true if object is an instance
of a class
"""


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """initiaize data"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ def area"""
        return (self.__size ** 2)
