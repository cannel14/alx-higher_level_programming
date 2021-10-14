#!/usr/bin/python3
"""tsk 8 module"""

def class_to_json(obj):
    """function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an objec"""
    return(obj.__dict__)
