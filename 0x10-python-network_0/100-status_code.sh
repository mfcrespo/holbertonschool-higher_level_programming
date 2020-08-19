#!/bin/bash
#script sends a request to a URL passed as an argument, displays only the status code of the response
curl "$1" -sI -w '%{http_code}' -o /dev/null
