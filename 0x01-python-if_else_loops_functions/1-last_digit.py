#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number;
if (number < 0):
    number *= -1
n = number
l = n % 10

if l > 5:
    print("Last digit of {} is {} and is greater than 5".format(x, l))
elif l == 0:
    print("Last digit of {} is {} and is 0".format(x, l))
elif l < 6 and not(0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(x, l))
