#!/usr/bin/python3
"""importing"""
import json
import os
import csv
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to json string """
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file"""
        my_list = []
        fname = cls.__name__ + ".json"
        if list_objs is not None:
            for ins in list_objs:
                my_list.append(cls.to_dictionary(ins))
        json_str = cls.to_json_string(my_list)
        with open(fname, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        my_list = []
        if json_string is None:
            return my_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        if cls.__name__ == 'Square':
            dummy = cls(7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances """
        lista = []
        name = cls.__name__ + ".json"
        if os.path.isfile(name):
            with open(name, 'r') as f:
                readstr = f.read()
                stringread = cls.from_json_string(readstr)
                for i in stringread:
                    lista.append(cls.create(**i))
        return lista

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file """
        my_list = []
        fname = cls.__name__ + ".csv"
        fieldnames = []
        if list_objs is not None:
            for ins in list_objs:
                my_list.append(cls.to_dictionary(ins))
        fieldnames = sorted(list(my_list[0].keys()))
        with open(fname, 'w') as f:
            fwrite = csv.DictWriter(f, fieldnames=fieldnames)
            for l in my_list:
                fwrite.writerow(l)

    @classmethod
    def load_from_file_csv(cls):
        """ instnace from csv file"""
        fname = cls.__name__ + ".csv"
        my_list = []
        dc = {}
        fname = cls.__name__ + '.csv'
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                csvread = csv.reader(f)
                if cls.__name__ == 'Rectangle':
                    keys = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    keys = ['id', 'size', 'x', 'y']
                for row in csvread:
                    aux = 0
                    for i in row:
                        dc[keys[aux]] = int(i)
                        aux += 1
                    my_list.append(cls.create(**dc))
        return my_list