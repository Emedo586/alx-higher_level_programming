#!/usr/bin/python3
"""Define a text-indentation function."""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must br a string")
    
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
        while c < len(text):
            print(text[c], end="")
            if text[c] == "\n" or text[c] in ".?:":
                if test[c] in ".?:":
                    print("\n")
                c += 1
                while c < len(text) and text[c] == ' ':
                    c += 1
                continue
            c += 1
