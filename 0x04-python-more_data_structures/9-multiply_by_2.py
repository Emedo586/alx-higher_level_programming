#!/usr/bin/python
def multiply_by_2(a_dictionary):
    new_dict = {}
    for idx in a_dictionary:
        new_dict[idx] = a_dictionary[idx] * 2
    return new_dict
