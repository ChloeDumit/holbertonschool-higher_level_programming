#!/usr/bin/python3
""" importing json """
import json
"""

reads a text file

"""


def load_from_json_file(filename):
    """ creates an object from json """
    with open(filename, 'r') as f:
        json_string = json.load(f)
        return json_string
