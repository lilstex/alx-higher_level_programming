#!/usr/bin/python3
"""This python script fetches this url 'https://intranet.hbtn.io/status' """
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(content), content, content.decode('utf-8')))