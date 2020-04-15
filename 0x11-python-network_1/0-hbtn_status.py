#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as status:
        response = status.read()
        print("Body Response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
