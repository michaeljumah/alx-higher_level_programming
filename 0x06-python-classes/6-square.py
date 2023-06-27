#!/usr/bin/python3

"""Define a class square."""

class Square:
    """class variable size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current position of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current size of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets positions"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    def myprint(self):
        """Print the square with the # char"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(""* self.__position[0] + *self.size)
