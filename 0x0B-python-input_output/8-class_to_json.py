#!/usr/bin/python3
"""Module for converting an object of a class to a JSON-compatible dictionary."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object."""
    return obj.__dict__
