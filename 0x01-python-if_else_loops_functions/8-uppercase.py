#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = ord(i) - 32
            i = chr(i)
        print("{}".format(i), end='')
    print()
