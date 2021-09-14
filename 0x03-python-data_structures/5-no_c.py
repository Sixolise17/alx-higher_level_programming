#!/usr/bin/python3

def no_C(my_string):
    new_string = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_string = new_string + i
    return new_string
