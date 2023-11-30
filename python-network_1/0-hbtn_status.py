#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib package."""

import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except HTTPError as e:
        print("Error: {}".format(e))
