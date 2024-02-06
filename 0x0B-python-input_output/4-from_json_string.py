#!/usr/bin/python3
"""
Module for converting a JSON string to a Python object.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to an object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)

if __name__ == "__main__":
    from_json
