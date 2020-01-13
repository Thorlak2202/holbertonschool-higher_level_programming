#!/usr/bin/python3
"""
function to indent texts
"""


def text_indentation(text):
    """ indents a text
    Args:
        text : receives a text to indent
    Returns:
        prints text with new lines after characters: ., ? and :
    Errors Raised:
        TypeError: if text is not string
    """
    enders = ['?', '.', ':']
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end='')
        if text[i] in enders:
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' \
                    and (i + 1) < len(text):
                i += 1
        i += 1
    print('\n')
