#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as file:
        file.write(text)
        for i in range(len(text)):
            i += 1
    return i
