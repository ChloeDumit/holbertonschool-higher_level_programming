#!/usr/bin/python3
"""

reads a text file

"""


def read_file(filename=""):
    """ reads file """
    with open(filename) as f:
        for line in f:
            print(line, end="")
        print()
