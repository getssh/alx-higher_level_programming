#!/usr/bin/python3

alpha = ""
low = 122
cap = 90
num = int(1)
while (num < 27):
    if (num % 2 != 0):
        print(chr(low), end="")
    else:
        print(chr(cap), end="")
    low -= 1;
    cap -= 1;
    num += 1;
