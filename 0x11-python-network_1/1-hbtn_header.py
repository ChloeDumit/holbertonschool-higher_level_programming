#!/usr/bin/python3
"""importing"""
import urllib.request
import sys


url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    info = response.info()
    print(info.get('X-Request-Id'))
