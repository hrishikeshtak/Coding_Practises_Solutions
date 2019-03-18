#!/usr/bin/python3


def fact(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    return n * fact(n-1)


for _ in range(int(input())):
    print(fact(int(input())))
