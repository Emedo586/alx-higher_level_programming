#!/usr/bin/python3
#  -Program that prints the result of the addition of all arguments
if __name__ == "__main__":
    """Print the addition of all arguments"""
    import sys
    # Arguments passed to the script
    args = sys.argv[1:]
    # Variable for storing the sum of the arguments
    sum_of_args = 0
    for arg in args:
        sum_of_args += int(arg)
    # Print the result of the addition
    print(sum_of_args)
