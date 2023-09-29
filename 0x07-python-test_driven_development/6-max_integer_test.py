#!/usr/bin/python3
"""Module tp find the max integer in a list"""
def_max_integer(list=[]):

if len(list) = 0:
    return None
result = list[0]
i = 1
while i < len(list):
    if list[i] > result:
        result = list[i]
    i += 1
    return
