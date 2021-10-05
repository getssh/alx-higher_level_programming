#!/usr/bin/python3
"""program to print a string with splilters"""


def text_indentation(text):
    """function to print text
    """
    if type(text) != str:
        raise TypeError("text must be string")
    for alpha in text:
        print(alpha, end="")
        if alpha == '.' or alpha == '?' or alpha == ':':
            print("\n\n", end="")
