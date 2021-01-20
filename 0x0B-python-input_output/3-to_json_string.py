#!/usr/bin/python3
""" importing json """
import json
"""

reads a text file

"""
def to_json_string(my_obj):
    """encodes string to json """
    json_string = json.dumps(my_obj)
    return json_string