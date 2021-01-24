#!/usr/bin/python3
"""importing"""
import json
import os
"""

creating new class


"""


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes data """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """ convert to json string """
        lista = []
        if list_dictionaries is not None:
           lista = json.dumps(list_dictionaries)
           return lista
        else:
            return lista

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file"""
        my_list = []
        fname = cls.__name__ + '.json'
        if (list_objs is not None):
            for ins in list_objs:
                my_list.append(ins.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, 'w') as f:
            f.write(jstr)