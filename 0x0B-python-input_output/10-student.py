#!/usr/bin/python3
""" My class module
"""


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        """initializes data """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation
            of student
        """
        dic = {}
        if type(attrs) is not list:
            return(self.__dict__)
        else:
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return(dic)
