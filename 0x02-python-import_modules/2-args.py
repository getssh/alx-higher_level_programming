#!/usr/bin/python3
import sys


if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
elif len(sys.argv) >= 2:
    print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    count = 1
    while (i < len(sys.argv)):
        print(str(count) + ":" + " " + sys.argv[i])
        i += 1
        count += 1
