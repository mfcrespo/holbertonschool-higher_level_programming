#!/bin/bash
#script sends a request to a URL passed as an argument, displays only the status code of the response
curl -s -I "$1" -o /dev/null -w '%{http_code}'
