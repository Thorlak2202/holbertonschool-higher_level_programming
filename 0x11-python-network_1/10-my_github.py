#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the body
of the response
"""
import requests
import sys

if __name__ == "__main__":
    user = (sys.argv[1], sys.argv[2])
    status = requests.get('https://api.github.com/user', auth=user)
    print(status.json().get("id"))
