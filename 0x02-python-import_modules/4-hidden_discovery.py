#!/usr/bin/python3
#  To prints all the names defined by the compiled module hidden_4.pyc
if __name__ == "__main__":
    """"Print all hidden directories"""
    import hidden_4
    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
