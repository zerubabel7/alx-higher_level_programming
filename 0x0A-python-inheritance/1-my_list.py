#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
