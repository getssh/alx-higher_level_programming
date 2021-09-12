#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divBy2 = [new % 2 == 0 for new in my_list]
    return divBy2
