#!/bin/bash
# A bash script that takes in a URL as an argument, and displays only the status code of the response.
curl -sw '%{http_code}' "$1"