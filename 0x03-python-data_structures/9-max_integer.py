#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    _max = 0
    for i in range(len(my_list) - 1):
        if (my_list[i] > my_list[i + 1]):
            _max = my_list[i]
            my_list[i + 1] = my_list[i]
        else:
            _max = my_list[i + 1]
    return _max
