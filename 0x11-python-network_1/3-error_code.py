#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the body
of the response
"""
from urllib import request, parse, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as status:
            response = status.read()
            print(response.decode("utf-8"))
    except error.HTTPError as raised_error:
        print("Error code: {}".format(raised_error.code))
