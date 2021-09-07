#!/usr/bin/python3


for num1 in range(0, 10):
    num2 = num1 + 1
    for num3 in range(num2, 10):
        if (num1 == 8):
            break
        print("{}{}".format(num1, num3), end=", ")
print("89")
