#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
#    i = 0
#while (i < len(my_string)):
#       new_str.append(my_string[i])

    j = 0
    while (j < len(my_string)):
        if (my_string[j] != "c" and my_string[j] != "C"):
            new_str += my_string[j]
        j += 1
    return new_str
