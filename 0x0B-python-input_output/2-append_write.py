#!/usr/bin/python3
"""
This module has a function that appends a string at the end of a text file (UTF8) 
and returns the number of characters added
"""

def append_write(filename="", text=""):
    """"Appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)