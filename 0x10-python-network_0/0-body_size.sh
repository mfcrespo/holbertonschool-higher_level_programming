#!/bin/bash
#script takes in a URL, sends a request to URL, displays the size of the body of the response
curl -w '%{size_download}\n' -so /dev/null "$1"
