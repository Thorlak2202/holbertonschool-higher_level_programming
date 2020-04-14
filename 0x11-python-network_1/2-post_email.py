#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response
"""
from urllib import request, parse
import sys

if __name__ == "__main__":

    data = {'email': sys.argv[2]}
    data = parse.urlencode(data).encode()

    with request.urlopen(sys.argv[1], data) as status:
        response = status.read()
        print(response.decode("utf-8"))
