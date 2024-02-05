#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """Empty class representing base geometry."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value to be a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
