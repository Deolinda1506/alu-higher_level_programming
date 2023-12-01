#!/usr/bin/python3
"""
Write a Python script that fetches https://alu-intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
