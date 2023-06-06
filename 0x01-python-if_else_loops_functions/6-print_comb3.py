#!/usr/bin/python3
for i in range(10):
    for x in range(i + 1, 10):
        print("{}".format(str(i) + str(x)), end="")
        if int(str(i) + str(x)) < 89:
            print(", ", end="")
print("")
