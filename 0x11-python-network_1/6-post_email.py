#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response
"""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}

    status = requests.post(sys.argv[1], data)
    print(status.text)
