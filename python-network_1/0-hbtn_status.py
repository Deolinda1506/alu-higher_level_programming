#!/usr/bin/python3
"""
Fetches content from a specified URL using the urllib package.
"""
import urllib.request

def fetch_content(url):
    """
    Fetches content from the given URL using urllib.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        bytes: The content fetched from the URL.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
    return content

if __name__ == '__main__':
    # Fetch content from https://intranet.hbtn.io/status
    url1 = 'https://intranet.hbtn.io/status'
    content1 = fetch_content(url1)

    # Display the fetched content
    print("Body response:")
    print("\t- type: {}".format(type(content1)))
    print("\t- content: {}".format(content1))
    print("\t- utf8 content: {}".format(content1.decode("utf-8")))

    # Fetch content from http://0.0.0.0:5050/status
    url2 = 'http://0.0.0.0:5050/status'
    content2 = fetch_content(url2)

    # Display the fetched content
    print("\nBody response for {}: ".format(url2))
    print("\t- type: {}".format(type(content2)))
    print("\t- content: {}".format(content2))
    print("\t- utf8 content: {}".format(content2.decode("utf-8")))

