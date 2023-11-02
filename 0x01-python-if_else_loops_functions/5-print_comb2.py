#!/usr/bin/python3
for u in range(0, 100):
    if u == 99:
        print(99)
        break
    print("{:02d}, ".format(u), end="")
