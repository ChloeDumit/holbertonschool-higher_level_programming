#!/usr/bin/python3
"""
A class that inherits from other
"""


class MyList(list):
    """ define class my list inheriting list
    """
    def print_sorted(self):
        """
        print a sorted list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
