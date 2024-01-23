#!/usr/bin/python3
"""Defines a square with a private instance attribute"""


class Square:
    """Class that defines a square with a private instance attribute: size"""

    def __init__(self, size):
        """Instantiates a Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
