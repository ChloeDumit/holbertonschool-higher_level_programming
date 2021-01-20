#!/usr/bin/python3
""" importing json """
import json
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""

reads a text file

"""
if __name__ == "__main__":
    """ add all arguments """
    name = "add_item.json"

    if os.path.isfile(name):
        my_list = load_from_json_file(name)
    else:
        my_list = []
    
    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, name)
