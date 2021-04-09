#!/usr/bin/python3
"""importing"""
import urllib.request
import sys


url = sys.argv[1]
mail = sys.argv[2]
email = {'mail': mail}

data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(url, mail)

with urllib.request.urlopen(req) as response:
    info = response.read()
    decoded = info.decode('utf-8')
    print("Your email is: ".format(decoded))