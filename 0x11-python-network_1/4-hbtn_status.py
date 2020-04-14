#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    status = requests.get('https://intranet.hbtn.io/status')
    print("Body Response:")
    print("\t- type: {}".format(type(status.text)))
    print("\t- content: {}".format(status.text))
