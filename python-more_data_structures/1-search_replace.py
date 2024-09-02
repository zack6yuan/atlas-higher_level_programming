#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for i in my_list:
        list2.append(replace if i == search else i)
    return (list2)
