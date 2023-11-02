#!/usr/bin/python3
for u in range(97, 123):
    if chr(u) == 'q' or chr(u) == 'e':
        continue
    print("{}".format(chr(u)), end="")
