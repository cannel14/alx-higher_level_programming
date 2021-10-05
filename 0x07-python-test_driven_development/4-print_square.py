#!/usr/bin/python3
'''this module prints squares'''


def print_square(size):
    '''this function prints a square of size(length) size(width)
     args:
       size(int): size of the square
     returns:
       None
    '''

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for n in range(size):
            print('#',end='')
        print()
