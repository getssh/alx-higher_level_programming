#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw = my_list[:]
    for i in range(len(my_list)):
        if (nw[i] == search):
            nw[i] = replace
    return nw
