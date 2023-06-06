#!/usr/bin/python3
def uppercase(str):
    t = list(str)
    for i in range(len(t)):
        if (ord(t[i]) > 96 and ord(t[i]) < 123):
            t[i] = chr(ord(t[i]) - 32)
    print("{}".format(("").join(t)))
