#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a+') as file:
        file.write(text)
        for i in range(len(text)):
            i += 1
    return i
