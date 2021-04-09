#!/usr/bin/python3
"""importing"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    r = r.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
