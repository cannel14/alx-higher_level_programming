#!/usr/bin/python3
"""creating class square"""
def ___init__(self, size=0):
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
