#!/usr/bin/python3
'''this module contains the addition function'''


def add_integer(a, b=98):
    '''this function does the addition of 2 arg
    args:
       a (union[int, float]): first number
       b (union[int, float], optional): second number
    returns:
       the result of the addition
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type (b) is not int and type (b) is not float:
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b    
