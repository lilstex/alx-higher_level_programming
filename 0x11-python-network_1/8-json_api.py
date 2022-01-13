#!/usr/bin/python3
""" This Python script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user 
    with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    data = {"q": letter}
    r = requests.post(url, data)
    try:
        if r.json() == {}:
            print("No result")
        print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")