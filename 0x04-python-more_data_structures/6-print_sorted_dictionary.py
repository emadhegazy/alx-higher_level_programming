#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_orderd = list(a_dictionary.keys())
    list_orderd.sort()
    for i in list_orderd:
        print("{}: {}".format(i, a_dictionary.get(i)))
