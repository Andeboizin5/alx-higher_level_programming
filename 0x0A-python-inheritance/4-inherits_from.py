#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class, otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) != a_class

