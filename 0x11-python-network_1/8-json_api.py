#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    values = {'q': q}

    req = requests.post(url, data=values)
    try:
        data = req.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError as e:
        print("Not a valid JSON")
