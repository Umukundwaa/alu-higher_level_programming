#!/usr/bin/python3
"""Defines a class Square with property getter and setter for size"""


class Square:
    """Square class with private size, getter, setter, and area method"""

    def __init__(self, size=0):
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
