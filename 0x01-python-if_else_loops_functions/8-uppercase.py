#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        upper = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upper = ord(str[i]) - 32
        print("{}".format(chr(upper)), end='')
    print("")
