#!/usr/bin/python3
"""
creates a square using a class
"""


class square():
    """
    class to create a sqyare
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def perimeter_of_my_square(self):
        """find the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """add custom string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
