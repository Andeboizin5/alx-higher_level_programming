#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class, otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
