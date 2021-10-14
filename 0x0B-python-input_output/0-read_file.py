#!/usr/bin/python3
"""module task 0"""

def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding= 'utf-8') as f:
        txt = f.read()
    print(txt, end=' ')
