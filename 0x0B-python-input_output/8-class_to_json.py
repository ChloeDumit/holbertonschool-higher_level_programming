#!/usr/bin/python3
""" importing json """
import json
"""

reads a text file

"""
def class_to_json(obj):
    """ returns dictionary description """
    return(obj.__dict__)