#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    if type(obj) == a_class or issubclass(object, a_class):
        return True
    return False
