#!/usr/bin/python3

w = int(input())
if w <= 3:
    print("NO")
else:
    print("YES") if w & 1 == 0 else print("NO")
