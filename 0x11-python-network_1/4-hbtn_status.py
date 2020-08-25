#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    req = requests.get("http://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:{}".format(type(req.text)))
    print("\t- content:{}".format(req.text))
