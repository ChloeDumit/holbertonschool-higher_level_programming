#!/usr/bin/python3
""" importing json """
import json
"""

reads a text file

"""


def from_json_string(my_str):
    """ from json to string """
    json_string = json.loads(my_str)
    return json_string
