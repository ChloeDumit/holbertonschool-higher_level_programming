#!/usr/bin/python3
"""
Class Square: creates a square class
"""


class Square:
    """creates class"""
    def __init__(self, size=0):
        """initialize data"""
        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
