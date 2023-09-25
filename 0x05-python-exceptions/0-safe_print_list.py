#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    total = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
            total += 1
        except indexError:
            break
        print("")
        return (total)
