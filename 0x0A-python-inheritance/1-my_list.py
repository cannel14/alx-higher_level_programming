#!/usr/bin/python3
"""task 1 module"""

class MyList(list):


    def print_sorted(self):
        """print sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
