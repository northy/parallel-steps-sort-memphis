#!/usr/bin/env python3
# Tests if the output is sorted or not

from sys import stdin

c = -1
for line in stdin:
    x = int(line)
    if x<c :
        print("ERROR")
        exit(1)
    c = x
print("OK")
