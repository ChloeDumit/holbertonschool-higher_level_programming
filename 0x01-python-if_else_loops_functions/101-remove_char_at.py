#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    if len(str) > n:
        str = str[0:n:] + str[n+1::]
    else:
        return(str)
    return (str)
