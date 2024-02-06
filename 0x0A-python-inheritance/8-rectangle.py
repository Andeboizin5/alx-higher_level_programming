#!/usr/bin/python3
"""Module defining a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

