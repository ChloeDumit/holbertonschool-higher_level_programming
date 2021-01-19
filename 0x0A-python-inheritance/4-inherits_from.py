#!/usr/bin/python3
"""
Return true if object is an instance
of a class
"""


def inherits_from(obj, a_class):
    """
    return True if class is inerited
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
