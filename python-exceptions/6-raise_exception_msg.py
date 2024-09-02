#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for j in range (x):
        try:
            print("{}".format(my_list[j]), end="")
        except IndexError:
            break
    print()
    return count
