#!/usr/bin/python3
"""
Returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """ look up"""
    return list(dir(obj))
