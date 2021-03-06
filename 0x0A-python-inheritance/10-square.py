#!/usr/bin/python3
"""task 10 module"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''class rectangle initialized'''
    def __init__(self, size):
        '''square initializes'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """get the number"""
        return self.__size ** 2
