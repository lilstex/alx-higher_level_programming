#!/usr/bin/python3
# 2-print_alphabet.py

"""Prints all numbers from 0 to 98 in decimal and in hexadecimal"""
for i in range(0, 99):
    print("{:d} = {:02x}".format(i, i))
