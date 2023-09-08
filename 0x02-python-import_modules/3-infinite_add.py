#!/usr/bin/python3
#  -Program that prints the result of the addition of all arguments
def add_arg(argv):
    counter = len(argv) - 1
    if counter == 0:
        print("{:d}".format(counter))
        return
    else:
        i = 1
        add = 0
        while i <= counter:
            add += int(argv[i + 1])
            print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
