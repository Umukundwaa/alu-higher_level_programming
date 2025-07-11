#!/usr/bin/python3
"""Defines a class Square with private size and validation"""


class Square:
    """Square class with private size attribute and validation"""

    def __init__(self, size=0):
        # Validate size type
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Validate size value
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
