#!/usr/bin/python3
def text_indentation(text):
    enders = ['?', '.', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in enders:
            print(text[i])
        elif text[i] in enders and text[i+1] == ' ':
            text = text.replace(text[i + 1], '\n')
        else:
            print(text[i], end='')
