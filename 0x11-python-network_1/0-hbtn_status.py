#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        page = response.read()
    print('Body response:')
    print('\t- type:', type(page))
    print('\t- content:', page)
    print('\t- utf8 content:', page.decode('utf-8'))
