#!/usr/bin/python3
"""Defines a square with size validation, area calculation, and printing"""


class Square:
    """Class that defines a square with size validation, area calculation, and printing"""

    def __init__(self, size=0):
        """Instantiates a Square with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (int): The new value for the size attribute.
        """
        self.__size = value
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

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
