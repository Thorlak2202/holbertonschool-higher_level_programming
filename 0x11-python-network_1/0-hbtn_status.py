#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as status:
        response = status.read()
        print("Body Response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))
