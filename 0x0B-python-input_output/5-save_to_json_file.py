#!/usr/bin/python3
""" importing json """
import json
"""

reads a text file

"""
def save_to_json_file(my_obj, filename):
    """ save to file json """
    with open(filename, 'w') as f:
        json_string = json.dump(my_obj, f)
