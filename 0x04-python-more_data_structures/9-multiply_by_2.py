#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dict = {}
        t = {}
        for key, value in a_dictionary.items():
            nvalue = value * 2
            t = {key: nvalue}
            dict.update(t)
        return (dict)
    return None
