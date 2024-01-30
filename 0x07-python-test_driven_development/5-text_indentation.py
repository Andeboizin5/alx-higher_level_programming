#!/usr/bin/python3
"""
Module to print text with indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    
    lines = text.split("\n")
    for line in lines:
        print(line.strip())
