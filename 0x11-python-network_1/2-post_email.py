#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        utf = html.decode('utf-8')
    print(utf)
