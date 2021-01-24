#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base"""
from .base import Base
"""

creating new class


"""


class Rectangle(Base):
    """ class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area function """
        return self.__width * self.__height

    def display(self):
        """ printing function """
        if self.__width == 0 or self.__height == 0:
            print()
        for i in range(self.__y):
            print("" * self.__y)
        for j in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """override str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update arguments """
        attributes = ["id", "width", "height", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attributes[arg], args[arg])

    def to_dictionary(self):
        """ returns a dictionary of a class """
        dic = {'id': self.id,
              'width': self.__width,
              'height': self.__height,
              'x': self.__x,
              'y': self.__y
               }
        return dic
