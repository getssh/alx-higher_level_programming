#!/usr/bin/python3
"""func to add two nums"""


def add_integer(a, b=98):
    """ numbers must be an int or float
    Args:
        a - first number
        b - second number to add
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
