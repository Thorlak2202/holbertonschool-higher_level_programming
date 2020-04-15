#!/usr/bin/python3
"""
Python script that takes your Github
credentials (username and password)
and uses the Github API to display
your id
"""
import requests
import sys

if __name__ == "__main__":
    user = (sys.argv[1], sys.argv[2])
    status = requests.get('https://api.github.com/user', auth=user)
    print(status.json().get("id"))
