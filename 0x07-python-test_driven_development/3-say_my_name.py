#!/usr/bin/python3
"""program to print given name"""


def say_my_name(first_name, last_name=""):
    """add to passed values
    Args:
        first_name - first naem
        last_name - last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
