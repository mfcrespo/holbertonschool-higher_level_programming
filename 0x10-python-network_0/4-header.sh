#!/bin/bash
#script takes in a URL as an argument, sends a GET request to the URL, displays the body of the response
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
