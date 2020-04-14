#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the body
of the response
"""
import requests
import sys

if __name__ == "__main__":
    status = requests.get(sys.argv[1])
    try:
        if status.status_code > 400:
            print("Error code: {}".format(status.status_code))
        else:
            print(status.text)
    except:
        pass
