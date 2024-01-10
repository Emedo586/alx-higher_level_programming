#!/bin/bash
#Bash script that takes in a URL,sends request and displays body size of the response.
curl -s "$1" | wc -c
