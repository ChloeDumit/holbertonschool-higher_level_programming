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
        self.sort()
        print(self)
