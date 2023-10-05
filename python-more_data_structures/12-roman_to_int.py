#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    num = 0
    for letter in roman_string:
        if letter == 'I':
            num += 1
        if letter == 'V':
            num += 5
        if letter == 'X':
            num += 10
        if letter == 'M':
            num += 1000
        if letter == 'D':
            num += 500
        if letter == 'C':
            num += 100
        if letter == 'L':
            num += 50
    return (num)
