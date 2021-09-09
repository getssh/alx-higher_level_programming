#!/usr/bin/python3
import sys


def argNone():
    print("0 arguments.")


def argOne():
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))


def argMore():
    print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    count = 1
    while (i < len(sys.argv)):
        print(str(count) + ":" + " " + sys.argv[i])
        i += 1
        count += 1
if len(sys.argv) == 1:
    argNone()
elif len(sys.argv) == 2:
    argOne()
elif len(sys.argv) >= 2:
    argMore()
