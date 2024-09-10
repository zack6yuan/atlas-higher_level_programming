#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ordered_key in sorted(a_dictionary.keys()):
        print(f"{ordered_key}: {a_dictionary[ordered_key]}")
