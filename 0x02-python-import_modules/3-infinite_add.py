#!/usr/bin/python3
#  -Program that prints the result of the addition of all arguments
if __name__ == "__main__":
    import sys
    sum = 0
    counter = len(sys.argv) - 1
    for i in range(counter):
        sum = sum + int(sys.argv[i + 1])
        print(sum)
