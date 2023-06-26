#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    rst = []
    for i in range(list_length):
        try:
            rst.append(my_list_1[i] / my_list_2[i])
            continue
        except ZeroDivisionError:
            print("division by 0")
            rst.append(0)
        except TypeError:
            print("wrong type")
            rst.append(0)
        except IndexError:
            print("out of range")
            rst.append(0)
        finally:
            pass
    return rst
