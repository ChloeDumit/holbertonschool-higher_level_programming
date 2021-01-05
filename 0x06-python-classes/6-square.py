#!/usr/bin/python3
class Square:
    """create class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def position(self, value):
        """set position"""
        if type(value) is not tuple or len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__positon = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        if self.position:
            if self.__size > 0:
                print("\n" * self.__position[1], end="")
                for a in range(self.size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
