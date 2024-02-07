#!/usr/bin/python3
"""A module for Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square instance."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)

