#!/usr/bin/python3
"""Defines a class Square with size validation and area method"""


class Square:
    """Square class with private size and method to calculate area"""

    def __init__(self, size=0):
        # Validate size type
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Validate size value
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
