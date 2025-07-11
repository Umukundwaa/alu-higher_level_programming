#!/usr/bin/python3
"""Defines a Square class that supports comparison operations."""


class Square:
    """Represents a square that can be compared by area."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """== comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= comparison based on area."""
        return self.area() >= other.area()
