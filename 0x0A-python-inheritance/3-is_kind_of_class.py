#!/usr/bin/python3
"""class

"""


def is_kind_of_class(obj, a_class):
    """fun to find out
    bal hal
    """
    if type(obj) == a_class or issubclass(object, a_class):
        return True
    return False
