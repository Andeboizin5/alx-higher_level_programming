#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A subclass of list that provides a method to print the list sorted."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
