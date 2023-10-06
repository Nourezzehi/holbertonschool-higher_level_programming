#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    item = ""
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
            i += 1
            if i == x:
                break
    except IndexError:
        None
    print()
    return i
