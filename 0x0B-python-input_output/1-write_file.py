#!/usr/bin/python3
"""
Writes a string to a text file
"""

def number_of_lines(filename="", text=""):
    """Return the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)