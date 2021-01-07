#!/usr/bin/python3

"""Prints # square
"""

def text_indentation(text):
    """ indented text maker"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i, end='')
            print()
            print()
        else: 
            print(i, end='')
           