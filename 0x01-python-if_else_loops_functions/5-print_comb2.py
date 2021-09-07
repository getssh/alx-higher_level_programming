#!/usr/bin/python3


for i in range(0, 100):
    if (i < 99):
        if (i < 10):
            i = str(i)
            i = i.zfill(2)
        print(i, end=", ")
print(i)
