#!/bin/bash
# A bash script that takes in a URL as an argument, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"