#!/usr/bin/python3
"""

reads a text file

"""
def append_write(filename="", text=""):
    """write a file and returns number of chars """
    with open(filename, 'a') as f:
        return f.write(text)
