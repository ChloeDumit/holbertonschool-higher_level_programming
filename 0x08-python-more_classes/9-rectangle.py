#!usr/bin/python3
"""
Create a rectangle class
"""


class Rectangle:
        """ Create an empty rectangle class"""

        number_of_instances = 0
        print_symbol = "#"

        def __init__(self, width=0, height=0):
            """ Initialize data"""

            self.width = width
            self.height = height
            Rectangle.number_of_instances += 1

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__height = value

        @property
        def width(self):
            return(self.__width)

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        def area(self):
            """Calculates Area"""
            return (self.__height * self.__width)

        def perimeter(self):
            """Calculates Perimeter"""
            if self.__width == 0 or self.__height == 0:
                return 0
            else:
                return (self.__height + self.__width) * 2

        def __str__(self):
            """ str func"""
            result = ""

            if self.__width == 0 or self.__height == 0:
                return result
            else:
                for i in range(self.__height):
                    for j in range(self.__width):
                        result = result + str(self.print_symbol)
                    result = result + '\n'
                result = result[:-1]
                return result

        def __repr__(self):
            """ repr func"""
            return "Rectangle(" + str(self.__width) + \
                "," + str(self.__height) + ")"

        def __del__(self):
            """ delete instance """
            print("Bye rectangle...")
            Rectangle.number_of_instances -= 1

        @staticmethod
        def bigger_or_equal(rect_1, rect_2):
            """ check which rectangle is bigger"""
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() < rect_2.area():
                return rect_2
            elif rect_1.area() == rect_2.area():
                return rect_1
            else:
                return rect_1

        @classmethod
        def square(cls, size=0):
            """ define square """
            return cls(size, size)
