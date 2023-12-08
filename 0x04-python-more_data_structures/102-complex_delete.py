#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
