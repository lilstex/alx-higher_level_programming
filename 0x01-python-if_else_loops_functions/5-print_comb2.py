#!/usr/bin/python3
# 2-print_alphabet.py

"""Prints numbers from 0 to 99."""
for i in range(0, 100):
    if i == 99 :
        print("{}".format(i))
    else:
        print("{:02}, ".format(i), end="")
