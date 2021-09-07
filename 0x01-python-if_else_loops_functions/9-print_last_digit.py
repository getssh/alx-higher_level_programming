#!/usr/bin/python3


def print_last_digit(number):
    if (number < 0):
        number *= -1
    store = ""
    last = int(number) % 10
    print(str(last), end="")

    return (last)
