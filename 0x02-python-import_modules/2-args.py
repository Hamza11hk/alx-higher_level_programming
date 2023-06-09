#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    if amount <= 1:
        print("0 argument.")
    else:
        if amount == 2:
            print("{:d} argument:".format(amount - 1))
        else:
            print("{:d} arguments:".format(amount - 1))
        for i in range(1, amount):
            print("{:d}: {}".format(i, sys.argv[i]))
