#!/usr/bin/python3
class Square:
    """creates class"""
    def __init__(self, size=0):
        """initializes data"""
        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates area"""
        return int(self.__size) * int(self.__size)
