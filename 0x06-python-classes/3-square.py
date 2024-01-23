#!/usr/bin/python3
"""Defines a square with size validation and area calculation"""


class Square:
    """Class that defines a square with size validation and area calculation"""

    def __init__(self, size=0):
        """Instantiates a Square with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Private method to validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
