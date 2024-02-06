#!/usr/bin/python3
"""
Module for converting an object to a JSON string.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    import json
    return json.dumps(my_obj)

