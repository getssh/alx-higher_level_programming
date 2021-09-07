#!/usr/bin/python3

alpha = ""
for i in range(97, 123):
    if (chr(i) == "q" or chr(i) == "e"):
        continue	
    alpha += chr(i)
print(alpha, end="")

