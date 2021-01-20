#!/usr/bin/python3
"""

reads a text file

"""
def write_file(filename="", text=""):
    """write a file and returns number of chars """
    with open(filename, 'w') as f:
        return f.write(text)
