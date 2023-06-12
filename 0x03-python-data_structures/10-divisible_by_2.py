#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        v = []
        for i in my_list:
            if i % 2 == 0:
                v.append(True)
            else:
                v.append(False)
        return v
