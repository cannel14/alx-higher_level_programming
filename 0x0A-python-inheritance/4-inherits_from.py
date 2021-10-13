#!/usr/bin/python3
"""task 4 module"""

def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
