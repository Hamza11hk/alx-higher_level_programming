#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        t = 0
        f = 0
        for tp in my_list:
            (w, event) = tp
            t += (w * event)
            f += event
        return (t/f) if f > 0 else 0
    else:
        return (0)

