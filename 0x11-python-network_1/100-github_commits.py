#!/usr/bin/python3
""" This Python script prints 10 commits (from the most recent to oldest) 
    of the repository “rails” by the user “rails”
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    r = requests.get(url)
    try:
        for i in range(10):
            print("{}: {}").format(r.json()[i].get("commit").get("sha"), 
                r.json()[i].get("commit").get("author").get("name"))
    except:
        pass