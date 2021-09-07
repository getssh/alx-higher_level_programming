#!/usr/bin/python3


def uppercase(str):
    store = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            store += chr(ord(i) - 32)
            continue
        store += i
    print(store)
