#!/usr/bin/pyhton3
def values(i):
    if i == 'I':
            return 1
    elif i == 'V':
            return 5
    elif i == 'X':
            return 10
    elif i == 'L':
            return 50
    elif i == 'C':
            return 100
    elif i == 'D':
            return 500
    elif i == 'M':
            return 1000
    return -1

def roman_to_int(roman_string):
    res = 0
    i = 0

    while i < len(roman_string):
        s1 = values(roman_string[i])
        if i + 1 < len(roman_string):
            s2 = values(roman_string[i + 1])
            if s1 >= s1:
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return (res)